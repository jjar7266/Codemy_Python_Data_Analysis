"""
Lesson 11 — Pandas Manual DataFrames
Codemy.com — Instructor: John Elder

This lesson covers:
- Creating a Pandas DataFrame manually
- Using NumPy to generate random data
- Assigning custom row and column labels
- Understanding how DataFrames relate to Series
- Displaying DataFrames in VS Code vs. Colab

Notes:
- John uses Google Colab; this version is adapted for VS Code.
- VS Code does NOT auto-display DataFrames — print() is required.
- A DataFrame is a collection of Series objects arranged as rows/columns.
"""

# ========================== Imports ===============================
import pandas as pd
import numpy as np
from numpy.random import rand

# ====================== Create Random Data =========================
my_data = rand(4, 3)   # 4 rows, 3 columns
print("Raw NumPy data:")
print(my_data)

# ====================== Create Row/Column Labels ===================
my_rows = ["A", "B", "C", "D"]
my_cols = ["Monday", "Tuesday", "Friday"]

# ====================== Create the DataFrame =======================
my_df = pd.DataFrame(my_data, my_rows, my_cols)

print("\nPandas DataFrame:")
print(my_df)

# VS Code will NOT auto-display objects without print()
print("\nFormatted DataFrame (same as above):")
print(my_df)

# ========================== Teaching Notes =========================
"""
Teaching Notes:

1. A DataFrame is a 2‑D labeled table.
   - Think: "Excel spreadsheet" or "SQL table".

2. Structure:
   - Rows have labels (index)
   - Columns have labels
   - Each column is a Pandas Series

3. DataFrame creation:
   pd.DataFrame(data, row_labels, col_labels)

4. Data source:
   - Can be NumPy arrays, lists of lists, dictionaries, or CSV files.
   - Here we use NumPy's rand() to generate random numbers.

5. VS Code difference:
   - Colab auto-displays DataFrames.
   - VS Code requires print(my_df) to show output.
"""

# ========================== Examples ===============================
"""
Examples:

Given:
data = [[1,2],[3,4]]
rows = ["R1","R2"]
cols = ["C1","C2"]

df = pd.DataFrame(data, rows, cols)

df looks like:

     C1  C2
R1    1   2
R2    3   4

df["C1"] → Series of column C1
df.loc["R2"] → row labeled R2
df.iloc[0] → first row by position
"""

# ====================== Common Mistakes ============================
"""
Common Mistakes:

- Forgetting print() in VS Code → nothing appears.
- Mismatched row/column label lengths:
    pd.DataFrame(data, ["A","B"], ["X","Y","Z"]) → ERROR
- Assuming DataFrames auto-format in terminal — they do not.
- Using wrong order of arguments:
    pd.DataFrame(data, columns, index) → incorrect
"""

# ========================== Takeaways ==============================
"""
Key Takeaways:

- A DataFrame is the core structure of Pandas.
- It combines labeled rows + labeled columns + NumPy speed.
- Each column is a Series; the DataFrame is a collection of Series.
- Manual DataFrames help you understand structure before loading CSVs.
- Next steps: selecting rows/columns, filtering, and DataFrame math.
"""
