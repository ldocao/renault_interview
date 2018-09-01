import pandas as pd

class Revenue:
    PATH = "/Users/ldocao/Documents/Personnel/Recherche emploi/data science/2018 10 04 Renault/datav0.5p-final.txt"
    SEP = " "

    def __init__(self):
        self.data = pd.read_csv(self.PATH, sep=self.SEP)


    def clean(self):
        self._remove_specific_dates()
        self._replace_date()
        self._translate_to_english()
        self._remove_unknown_car_model()
        return self.data

    def _remove_specific_dates(self):
        """Remove date that looks like XX/XX/XXXX, see issue #1"""
        is_specific = self.data["Date"].str.contains("/", na=False)
        self.data = self.data[~is_specific]
        

    def _replace_date(self):
        self.data = self.data.rename(columns={"Date": "is_weekend"}) #inplace will be deprecated in pandas 1.0
        self.data = self.data.replace({"week": False, "weekend": True})
        

    def _translate_to_english(self):
        """Replace French words to English to uniformize data"""
        FRENCH_TO_ENGLISH = {"noir": "black",
                             "jaune": "yellow",
                             "rouge": "red",
                             "bleu": "blue",
                             "vert": "green"}
        self.data = self.data.replace(FRENCH_TO_ENGLISH)

    def _remove_unknown_car_model(self):
        is_unknown = self.data["Model"] == "Talisman"
        self.data = self.data[~is_unknown]
