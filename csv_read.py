# %%
# pip freeze >> requirements.txt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.dates as mdates

# Working with the flights dataset
df = sns.load_dataset('flights')

# Exploring the data
# df.head()
# df.info()
# df.shape
# df[df.year.isna()]
# [i for i in df.month.unique()]
# min(df.passengers)
# max(df.passengers)

# Manipulating the columns
df['month_year'] = df['month'].astype(str) + '-' + df['year'].astype(str)
df['date'] = pd.to_datetime(df['month_year'], format='%b-%Y')
df.drop(columns = ['month_year'], inplace=True)
# df.loc[df['date'] < '1950-08']

# Average number of passengers per month over all years
df.groupby('month').agg({'passengers':'mean'}).sort_values('passengers')

# Average number of passengers per year over all months
df.groupby('year').agg({'passengers':'mean'}).sort_values('passengers')

# Plot passengers by date -----------------------------------

# Convert dates to numbers to create line of best fit
datesAsNums = mdates.date2num(df['date'])
slope, intercept = np.polyfit(datesAsNums, df['passengers'], 1)
line = slope * datesAsNums + intercept

# Create plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['date'], slope * datesAsNums + intercept, color='red', label='Best Fit Line')
ax.scatter(df['date'], df['passengers'])
plt.xlabel('Date of flight.')
plt.ylabel('Number of passengers.')
plt.title('Number of passengers flying on a given date.')
plt.show()
# %%
