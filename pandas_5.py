# pyright: reportGeneralTypeIssues=false
r"""
Lesson 14 — Adding and Removing Columns and Rows
Codemy.com — Instructor: John Elder

This lesson covers:
- Adding new columns to a DataFrame
- Adding default values, lists, and NaN
- Using insert() to control column position
- Using assign() to create new DataFrames
- Removing columns and rows with drop()
- inplace=True vs inplace=False

Notes:
- This version is adapted for VS Code.
- VS Code requires print() to display DataFrames.
- dog_data_short.csv must be in the same folder as this script.
"""

# ========================== Imports ===============================
import pandas as pd
import numpy as np

# ====================== Load CSV File ==============================
print("Loading dog_data_short.csv...")
my_df = pd.read_csv("dog_data_short.csv")
print(my_df)

# ====================== Adding Columns =============================

print("\nAdding Gender column from list:")
gender_list = ["Male", "Female", "Male", "Male", "Female"]
my_df["Gender"] = gender_list
print(my_df)

print("\nAdding default True values (Alive/Dead):")
my_df["Alive/Dead"] = [True] * len(my_df)
print(my_df)

print("\nAdding NaN values (ShowDogs):")
my_df["ShowDogs"] = [np.nan] * len(my_df)
print(my_df)

print("\nAdding Adopted column using insert() at position 1:")
my_df.insert(1, "Adopted", [True] * len(my_df), allow_duplicates=True)
print(my_df)

print("\nAdding Horse column using assign() (creates new DataFrame):")
my_df2 = my_df.assign(Horse=[False] * len(my_df))
print(my_df2)

print("\nOriginal DataFrame remains unchanged:")
print(my_df)

# ====================== Removing Columns ===========================

print("\nAttempting to drop ShowDogs (not inplace):")
print(my_df.drop("ShowDogs", axis=1))

print("\nDropping ShowDogs inplace:")
my_df.drop("ShowDogs", axis=1, inplace=True)
print(my_df)

print("\nRunning again to show ShowDogs is gone:")
print(my_df)

# ====================== Removing Rows ==============================

print("\nDropping row with index 3 (not inplace):")
print(my_df.drop(3, axis=0))

print("\nOriginal DataFrame still intact:")
print(my_df)

# ========================== Teaching Notes =========================
r"""
Teaching Notes:

1. Adding columns:
   - my_df["NewCol"] = values → adds a column
   - insert() lets you choose the exact position
   - assign() returns a *new* DataFrame

2. Default values:
   - [True] * len(df) → repeats True for every row
   - [np.nan] * len(df) → fills with NaN

3. Removing columns/rows:
   - drop("col", axis=1)
   - drop(index, axis=0)
   - inplace=True modifies the DataFrame permanently

4. assign():
   - my_df.assign(NewCol=values)
   - Does NOT change my_df unless you reassign it

5. Common patterns:
   - Add → inspect → drop → inspect
"""

# ========================== Examples ===============================
r"""
Examples:

df["Age"] = [1,2,3,4]
df.insert(0, "ID", [100,101,102,103])
df2 = df.assign(Score=[10,20,30,40])
df.drop("Age", axis=1, inplace=True)
df.drop(2, axis=0)
"""

# ====================== Common Mistakes ============================
r"""
Common Mistakes:

- Using Colab paths in VS Code:
    pd.read_csv("/content/file.csv") → FileNotFoundError

- Forgetting print() in VS Code:
    df   # does nothing

- Adding a list that doesn't match DataFrame length:
    ValueError: Length of values does not match length of index

- Confusing inplace:
    df.drop("Col") → does NOT remove column
    df.drop("Col", inplace=True) → removes it
"""

# ========================== Takeaways ==============================
r"""
Key Takeaways:

- Adding columns is simple with assignment, insert(), or assign().
- inplace=True permanently changes the DataFrame.
- assign() creates a new DataFrame and leaves the original untouched.
- drop() removes rows or columns depending on axis.
"""
