import pandas as pd


class logger:
    """
    Concept: Lean Waterfall Process
    Inspired by: 
    (0) g's efficiency fixation
    (1) adina's idea to output the waterfall as a pandas df 
    (instead of going back and forth sa doc / sheet! efficient!!!!)
    (2) pandas-logger package
    (3) towardsdatascience.com/the-unreasonable-effectiveness-of-method-chaining-in-pandas-15c2109e3c69
    """
    def __init__(self, *functions):
        self.f_set = functions
        self.result = {}
        self.counter = 0
        print("Logger created.")

    def log(self, df, statement = None):
        
        if statement is None:
            statement = "Step {}".format(self.counter)
        self.result[statement] = {}
        for f in self.f_set:
            self.result[statement][f.__name__] = f(df)
            self.counter = self.counter + 1
        return df.copy()

    def getResults(self):
        return pd.DataFrame.from_dict(self.result, orient = "index")


def setcols(df, fn=lambda x: x.columns.map('_'.join), cols=None):
    """
    Sets the column of the data frame to the passed column list.
    (pandas .pipe friendly)

    This function is directly from: 
    towardsdatascience.com/the-unreasonable-effectiveness-of-method-chaining-in-pandas-15c2109e3c69
    """
    if cols:
        df.columns = cols
    else:
        df.columns = fn(df)
    return df