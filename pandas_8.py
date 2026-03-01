# pyright: reportGeneralTypeIssues=false
r"""
Lesson 17 — Dropping, Filling, and Grouping Data
Codemy.com — Instructor: John Elder

This lesson covers:
- Dropping rows and columns with missing data
- Using thresholds to control drop behavior
- Filling missing values with constants or statistics
- Grouping data with groupby()
- Aggregation functions: sum, mean, min, max, std, var, count, describe
- Counting unique values and value frequencies

Notes:
- This version is adapted for VS Code.
- VS Code requires print() to display DataFrames.
- dog_data.csv must be in the same folder as this script.
"""

# ========================== Imports ===============================
import pandas as pd
import numpy as np

# ====================== Dropping Missing Data ======================
print("Creating DataFrame with missing values...")
stuff = {
    "A": [1, 2, 3],
    "B": [4, np.nan, 6],
    "C": [7, 8, 9],
    "D": [10, 11, 12]
}
my_df = pd.DataFrame(stuff)
print(my_df)

print("\nDrop rows with missing data (not permanent):")
print(my_df.dropna(inplace=False))

print("\nDrop columns with missing data (not permanent):")
print(my_df.dropna(axis=1, inplace=False))

print("\nDrop columns with threshold (thresh=1 keeps all, thresh=2 removes B):")
print(my_df.dropna(thresh=2, axis=1))

# ====================== Filling Missing Data =======================
print("\nFill missing values with constant 41:")
print(my_df.fillna(value=41))

print("\nFill missing values with column mean:")
print(my_df.fillna(my_df["B"].mean()))

print("\nFill missing values with column min:")
print(my_df.fillna(my_df["B"].min()))

print("\nFill missing values with column max:")
print(my_df.fillna(my_df["B"].max()))

print("\nFill missing values with column sum:")
print(my_df.fillna(my_df["B"].sum()))

# ====================== Grouping Data ==============================
print("\nCreating DataFrame for grouping...")
stuff = {
    "Corporation": ["Apple", "Google", "Meta", "Apple", "Google", "Meta"],
    "Employees": ["John", "April", "Wes", "Aspen", "Beth", "Steph"],
    "Salary": [200, 220, 190, 130, 120, 150]
}
my_df = pd.DataFrame(stuff)
print(my_df)

print("\nGroup by Corporation:")
company = my_df.groupby("Corporation")
print(company)

print("\nSum of grouped data:")
print(company.sum())

print("\nMean salary per corporation:")
print(company.mean(numeric_only=True))

print("\nMax values per corporation:")
print(company.max(numeric_only=True))

print("\nStandard deviation:")
print(company.std(numeric_only=True))

print("\nVariance:")
print(company.var(numeric_only=True))

print("\nCount of entries per corporation:")
print(company.count())

print("\nDescribe grouped data:")
print(company.describe())

# ====================== Unique & Value Counts ======================
print("\nLoading dog_data.csv for unique/value counts...")
my_df = pd.read_csv("dog_data.csv")
print(my_df)

print("\nDogName column:")
print(my_df["DogName"])

print("\nValue counts for DogName:")
print(my_df["DogName"].value_counts())

print("\nValue counts as DataFrame:")
print(pd.DataFrame(my_df["DogName"].value_counts()).head(50))

print("\nUnique Dog Names:")
print(my_df["DogName"].unique())

print("\nUnique Dog Names as DataFrame:")
print(pd.DataFrame(my_df["DogName"].unique()).head(50))

# ========================== Teaching Notes =========================
r"""
Teaching Notes:

1. dropna():
   - dropna() removes rows with missing data.
   - dropna(axis=1) removes columns with missing data.
   - thresh=2 means "keep only columns with at least 2 non-null values".

2. fillna():
   - fillna(value) replaces missing values.
   - fillna(df["Col"].mean()) uses statistics to fill missing values.
   - Common choices: mean, min, max, sum.

3. groupby():
   - df.groupby("Column") groups rows by category.
   - Aggregation functions: sum, mean, min, max, std, var, count, describe.

4. Unique values:
   - df["Col"].unique() returns unique values.
   - df["Col"].value_counts() returns frequency counts.
"""

# ========================== Examples ===============================
r"""
Examples:

df.dropna()
df.dropna(axis=1)
df.dropna(thresh=3)

df.fillna(0)
df.fillna(df["Age"].mean())

group = df.groupby("Team")
group.sum()
group.mean()
group.describe()

df["Name"].value_counts()
df["Breed"].unique()
"""

# ====================== Common Mistakes ============================
r"""
Common Mistakes:

- Forgetting axis:
    dropna() removes rows
    dropna(axis=1) removes columns

- Using thresh incorrectly:
    thresh counts NON-null values, not nulls.

- Expecting groupby() to show results without an aggregation:
    df.groupby("Col")  # shows nothing useful

- Confusing unique() vs value_counts():
    unique() → list of unique values
    value_counts() → frequency of each value
"""

# ========================== Takeaways ==============================
r"""
Key Takeaways:

- dropna() removes missing data; fillna() replaces it.
- groupby() is essential for summarizing categories.
- Aggregation functions reveal patterns in grouped data.
- unique() and value_counts() help explore categorical columns.
"""
