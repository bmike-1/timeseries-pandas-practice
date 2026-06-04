# %%
# pip freeze >> requirements.txt
import pandas as pd
import seaborn as sns

# Working with the flights dataset
df = sns.load_dataset('flights')

# Exploring the data
df.head()
df.info()
df.shape
df[df.year.isna()]
# [i for i in df.month.unique()]

# Manipulating the columns
df['month_year'] = df['month'].astype(str) + '-' + df['year'].astype(str)
df['date'] = pd.to_datetime(df['month_year'], format='%B-%Y') # incorrect format



