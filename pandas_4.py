"""
Lesson 13 — Pulling Data From DataFrames
Codemy.com — Instructor: John Elder

This lesson covers:
- Selecting rows with loc and iloc
- Selecting columns by label and position
- Using head() and tail()
- Inspecting DataFrame structure and statistics
- Counting unique values and frequencies
- Grouping and aggregating data

Notes:
- John uses Google Colab; this version is adapted for VS Code.
- VS Code requires print() to display DataFrames.
- dog_data.csv must be in the same folder as this script.
"""

# ========================== Imports ===============================
import pandas as pd
import numpy as np

# ====================== Load CSV File ==============================
print("Loading dog_data.csv...")
my_df = pd.read_csv("dog_data.csv")
print(my_df)

# ====================== Pulling Rows ===============================
print("\nRow 0 using loc:")
print(my_df.loc[0])

print("\nRows 0, 2, and 4:")
print(my_df.loc[[0, 2, 4]])

print("\nFirst 5 rows:")
print(my_df.head())

print("\nFirst 9 rows:")
print(my_df.head(9))

print("\nLast 5 rows:")
print(my_df.tail())

print("\nLast 10 rows:")
print(my_df.tail(10))

# ====================== Pulling Columns ============================
print("\nColumn 'DogName' (bracket notation):")
print(my_df["DogName"])

print("\nColumn 'Color' (dot notation):")
print(my_df.Color)

print("\nColumn at index 1 using iloc:")
print(my_df.iloc[:, 1])

print("\nRows 42–899, column 1:")
print(my_df.iloc[42:900, 1])

# ====================== DataFrame Information ======================
print("\nDataFrame info:")
print(my_df.info())

print("\nShape (rows, columns):")
print(my_df.shape)

print("\nNumber of dimensions:")
print(my_df.ndim)

print("\nColumn data types:")
print(my_df.dtypes)

# ====================== Descriptive Statistics =====================
print("\nFull DataFrame statistics:")
print(my_df.describe())

print("\nBreed column statistics:")
print(my_df["Breed"].describe())

print("\nColor column statistics:")
print(my_df["Color"].describe())

print("\nDogName column statistics:")
print(my_df["DogName"].describe())

# ====================== Value Counts ===============================
print("\nColor counts (descending):")
print(my_df["Color"].value_counts())

print("\nColor counts (ascending):")
print(my_df["Color"].value_counts(ascending=True))

print("\nDogName counts (drop NaN):")
print(my_df["DogName"].value_counts())

print("\nDogName counts (include NaN):")
print(my_df["DogName"].value_counts(dropna=False))

print("\nColor relative frequency (percentages):")
print(my_df["Color"].value_counts(normalize=True))

print("\nCount of WHITE dogs:")
print(my_df["Color"].value_counts()["WHITE"])

# ====================== Grouping & Aggregation =====================
print("\nGroup by Color — size():")
print(my_df.groupby("Color").size())

print("\nGroup by Color — count():")
print(my_df.groupby("Color").count())

# ========================== Teaching Notes =========================
"""
Teaching Notes:

1. loc vs iloc:
   - loc uses labels (row names)
   - iloc uses numeric positions

2. Column selection:
   - my_df["Color"] → Series
   - my_df.Color → shorthand (only works for valid names)
   - my_df.iloc[:,1] → column by position

3. head() and tail():
   - head(n) → first n rows
   - tail(n) → last n rows

4. Data inspection:
   - info() → column types + memory usage
   - shape → (rows, columns)
   - describe() → summary statistics

5. value_counts():
   - Counts unique values
   - normalize=True → percentages
   - dropna=False → include NaN

6. groupby():
   - size() → count rows per group
   - count() → count non-null values per column
"""

# ========================== Examples ===============================
"""
Examples:

my_df.loc[5] → row with index 5
my_df.iloc[0:10] → first 10 rows
my_df["Breed"].value_counts() → count breeds
my_df.groupby("Color").size() → number of dogs per color
"""

# ====================== Common Mistakes ============================
"""
Common Mistakes:

- Using Colab paths in VS Code:
    pd.read_csv("/content/file.csv") → FileNotFoundError

- Forgetting print() in VS Code:
    my_df.head()  # must be printed

- Using dot notation for invalid column names:
    my_df.Dog Name → ERROR
    Use my_df["Dog Name"]

- Confusing loc and iloc:
    loc uses labels, iloc uses numbers
"""

# ========================== Takeaways ==============================
"""
Key Takeaways:

- loc and iloc are the core tools for selecting rows and columns.
- head(), tail(), info(), and describe() are essential for exploring data.
- value_counts() and groupby() reveal patterns and distributions.
- Understanding DataFrame pulling is the foundation for filtering, cleaning, and analysis.
"""
