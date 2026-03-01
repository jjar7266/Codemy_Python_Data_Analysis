# pyright: reportGeneralTypeIssues=false
r"""
Lesson 16 — Changing and Resetting Row Indexes
Codemy.com — Instructor: John Elder

This lesson covers:
- Setting a new index on a DataFrame
- Understanding temporary vs permanent index changes
- Resetting the index
- Removing the old index column
- How inplace=True affects DataFrame operations

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

# ====================== Adding a New Column ========================
print("\nAdding 'Frame Header' column:")
my_df["Frame Header"] = ["Dog 1", "Dog 2", "Dog 3", "Dog 4", "Dog 5"]
print(my_df)

# ====================== Setting a New Index ========================
print("\nSetting index to 'Frame Header' (NOT permanent):")
print(my_df.set_index("Frame Header"))

print("\nOriginal DataFrame unchanged:")
print(my_df)

print("\nSetting index permanently with inplace=True:")
my_df.set_index("Frame Header", inplace=True)
print(my_df)

# ====================== Resetting the Index ========================
print("\nResetting index (NOT permanent):")
print(my_df.reset_index())

print("\nOriginal DataFrame still unchanged:")
print(my_df)

print("\nResetting index permanently:")
my_df.reset_index(inplace=True)
print(my_df)

# ====================== Removing Old Index Column ==================
print("\nDropping the old 'Frame Header' column:")
my_df.drop("Frame Header", axis=1, inplace=True)
print(my_df)

# ========================== Teaching Notes =========================
r"""
Teaching Notes:

1. set_index():
   - my_df.set_index("Column") → returns a new DataFrame
   - my_df.set_index("Column", inplace=True) → permanent change

2. reset_index():
   - my_df.reset_index() → returns DataFrame with index restored to 0..n
   - my_df.reset_index(inplace=True) → permanent reset

3. Why does reset_index() create a new column?
   - Because the old index becomes a normal column unless you drop it.

4. Dropping the old index:
   - my_df.drop("ColumnName", axis=1, inplace=True)

5. Common workflow:
   - Add column → set index → reset index → drop old index column
"""

# ========================== Examples ===============================
r"""
Examples:

df["ID"] = [100, 101, 102, 103]
df.set_index("ID", inplace=True)
df.reset_index(inplace=True)
df.drop("ID", axis=1, inplace=True)
"""

# ====================== Common Mistakes ============================
r"""
Common Mistakes:

- Forgetting inplace=True:
    df.set_index("Col")  # does NOT change df

- Confusing axis:
    axis=0 → rows
    axis=1 → columns

- Resetting index but forgetting to drop the old index column:
    df.reset_index(inplace=True)
    df.drop("old_index", axis=1, inplace=True)

- Using set_index() without understanding it returns a NEW DataFrame:
    df2 = df.set_index("Col")  # df stays unchanged
"""

# ========================== Takeaways ==============================
r"""
Key Takeaways:

- set_index() and reset_index() are reversible.
- inplace=True makes changes permanent.
- reset_index() turns the old index into a column.
- Always drop the old index column if you no longer need it.
"""
