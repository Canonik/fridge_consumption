import pandas as pd

df = pd.read_csv("data/test.csv")


print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

print(df.info())
