"""
Lesson 10 — Pandas Series
Codemy.com — Instructor: John Elder

This lesson covers:
- Creating a Pandas Series from a Python list
- Default integer index vs. custom labels
- Accessing Series values by index number
- Accessing Series values by label
- How Series behave like NumPy arrays + dictionaries

Notes:
- John uses Google Colab; this version is adapted for VS Code.
- VS Code does NOT auto-display objects — print() is required.
- A Series is the building block of a Pandas DataFrame.
"""

# ========================== Imports ===============================
import pandas as pd
import numpy as np

# ====================== Create Series From List ====================
my_list = [5, 9, 12, 27]

# Create a Series with default integer index
my_series = pd.Series(my_list)

print("Series with default index:")
print(my_series)

print("\nPull item at index 1:")
print(my_series[1])   # VS Code requires print()

# ====================== Create Series With Custom Index ============
my_index = ["A", "B", "C", "D"]
my_series2 = pd.Series(my_list, my_index)

print("\nSeries with custom index labels:")
print(my_series2)

# ====================== Create Labels Manually =====================
my_series3 = pd.Series(my_list, ["E", "F", "G", "H"])

print("\nSeries with manually provided labels:")
print(my_series3)

# ====================== Access by Label ============================
print("\nPull item with label 'G':")
print(my_series3["G"])

# ========================== Teaching Notes =========================
"""
Teaching Notes:

1. A Pandas Series is a one-dimensional labeled array.
   - Think: "A column in a spreadsheet" or "A NumPy array with names."

2. A Series has two parts:
   - Values  → the data
   - Index   → the labels (default: 0,1,2,...)

3. Accessing values:
   - By position: series[1]
   - By label:    series["G"]

4. Labels do NOT need to be strings — they can be numbers, dates, etc.

5. VS Code difference:
   - Colab auto-displays objects.
   - VS Code requires print() to show output.

6. Series behave like:
   - NumPy arrays (support vectorized math)
   - Dictionaries (label-based lookup)
"""

# ========================== Examples ===============================
"""
Examples:

Given:
s = pd.Series([10, 20, 30], ["x", "y", "z"])

s["y"] → 20
s[1]   → 20
s.values → array([10, 20, 30])
s.index  → Index(['x','y','z'])
"""

# ====================== Common Mistakes ============================
"""
Common Mistakes:

- Forgetting print() in VS Code → nothing appears in terminal.
- Mixing up index vs. label:
    series[1] is NOT the same as series["1"].
- Creating Series with mismatched lengths:
    pd.Series([1,2,3], ["A","B"]) → ERROR
- Assuming labels must be strings — they can be anything hashable.
"""

# ========================== Takeaways ==============================
"""
Key Takeaways:

- A Series is the foundation of all Pandas data structures.
- It combines NumPy speed with dictionary-style labels.
- Default index is numeric, but custom labels are often more meaningful.
- Access by position (like a list) or by label (like a dict).
- Understanding Series makes DataFrames much easier to learn next.
"""
