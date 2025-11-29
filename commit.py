import pandas as pd

# Load the dataframe
df = pd.read_csv('train.xlsx - train.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())
