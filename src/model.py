import pandas as pd

data = pd.read_csv("data\\train.csv")
home_dfs = dict(tuple(data.groupby('home_id')))
#print(home_dfs)

#how to access:
home_1 = pd.DataFrame(home_dfs['home_1'])
print(home_1)
