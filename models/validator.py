# models/validator.py
class Validator:
    def validate(self, df):
        return df.filter("Year >= 2024")
