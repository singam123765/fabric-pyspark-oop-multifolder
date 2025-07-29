# models/cleaner.py
class Cleaner:
    def clean(self, df):
        return df.dropna()
