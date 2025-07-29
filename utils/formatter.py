# utils/formatter.py
class Formatter:
    def format_columns(self, df):
        return df.withColumnRenamed("Product", "product").withColumnRenamed("Year", "year")
