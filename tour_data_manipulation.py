# %%
import pandas as pd

# read in tour data
df = pd.read_csv("input_data/tour_data.csv", index_col=False)

# Explore dataset
df.info()
df.head()
len(df.Peak.unique())

# Explore data and unique values and lengths
for col in df.columns:
    print(col)
    print(df[col].unique())
    print(len(df[col].unique()))

# %%
# Column names manipulation ------------------------------------------------------------------

# Peak columns manipulation
# Unsure as to rank/peak/all time peak as, after checking wiki
# It appears just Rank and Peak are available
# To match the current data, i'll remove the All Time Peak column
# I'll then rename Rank to current Rank and highest_all_time_rank
df.drop(columns=["All Time Peak"], axis=1, inplace=True)
df.rename(
    columns={"Rank": "current_rank", "Peak": "highest_all_time_rank"}, inplace=True
)

# For consistency, i will change the column names to be
# - lower case,
# - without unusual characters i.e. \xa0,
# - connected by underscores,
# - without punctuation
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace("\xa0", "_", regex=False)
df.columns = df.columns.str.replace("[\(\).]", "", regex=True)
df.columns = df.columns.str.replace(" ", "_", regex=False)

# %%
# Column data manipulation ------------------------------------------------------------------

# Highest all time rank column clean - replace square brackets, fillnas with current rank, set to int
df["highest_all_time_rank"] = df.highest_all_time_rank.str.replace(
    "\[.*\]", "", regex=True
)
df["highest_all_time_rank"] = df["highest_all_time_rank"].fillna(df["current_rank"])
df["highest_all_time_rank"] = df["highest_all_time_rank"].astype(int)
# df['highest_previous_rank'].case_when(caselist = [
#         (df['highest_previous_rank'].isnull(), df['current_rank'])
#     ]
# )

# Dollar columns clean -  Remove dollars and commas, and remove any bracketed entries
dollar_cols = ["actual_gross", "adjusted_gross_in_2022_dollars", "average_gross"]
for col in dollar_cols:
    df[col] = df[col].str.replace("[$,]", "", regex=True)
    df[col] = df[col].str.replace("\[.\]", "", regex=True)
    df[col] = df[col].astype(int)

# Years column clean
# Check for hyphens, and save years as a list for future use
col_list = []


def clean_years(val):
    if "–" in val:
        start, end = val.split("–")
        return list(range(int(start), int(end) + 1))
    else:
        return [int(val)]


# Apply clean years function
df["years"] = df["years"].apply(clean_years)

# Save file
df.to_csv("tour_data_clean.csv", index=False)
