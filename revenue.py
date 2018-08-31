import pandas as pd

class Revenue:
    PATH = "/Users/ldocao/Documents/Personnel/Recherche emploi/data science/2018 10 04 Renault/datav0.5p-final.txt"
    SEP = " "

    def __init__(self):
        self.data = pd.read_csv(self.PATH, sep=self.SEP)


    def clean(self):
        self._replace_date()
        return self.data


    def _replace_date(self):
        self.data = self.data.rename(columns={"Date": "is_weekend"}) #inplace will be deprecated in pandas 1.0
        self.data = self.data.replace({"week": False, "weekend": True})
        
