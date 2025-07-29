# main.py

# Sample DataFrame
data = [("Fabric", 2024), ("Power BI", None), ("Synapse", 2023)]
df = spark.createDataFrame(data, ["Product", "Year"])

# Instantiate classes
cleaner = Cleaner()
validator = Validator()
formatter = Formatter()

# Execute steps
df_cleaned = cleaner.clean(df)
df_validated = validator.validate(df_cleaned)
df_final = formatter.format_columns(df_validated)

df_final.show()
