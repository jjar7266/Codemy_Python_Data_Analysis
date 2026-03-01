# pyright: reportGeneralTypeIssues=false
r"""
Lesson 15 — Conditional Selection in Pandas
Codemy.com — Instructor: John Elder

This lesson covers:
- Boolean comparisons in Pandas
- Filtering rows using ==, !=, <, >, <=, >=
- Using boolean masks to return matching data
- AND (&) and OR (|) conditions
- Selecting specific columns after filtering
- Counting matches with len()

Notes:
- This version is adapted for VS Code.
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

# ====================== Basic Boolean Comparison ===================
print("\nBoolean comparison (my_df == 'BROWN'):")
print(my_df == "BROWN")

print("\nReturn actual data matching 'BROWN':")
print(my_df[my_df == "BROWN"])

print("\nReturn only the Color column where value == 'BROWN':")
print(my_df[my_df == "BROWN"]["Color"])

print("\nReturn Color and DogName where value == 'BROWN':")
print(my_df[my_df == "BROWN"][["Color", "DogName"]])

# ====================== Column-Specific Comparison =================
print("\nRows where Color == 'BROWN':")
print(my_df[my_df["Color"] == "BROWN"])

# ====================== Multiple Conditions (AND) ==================
print("\nRows where Color == 'BROWN' AND Breed == 'MIXED':")
brown_mixed = my_df[(my_df["Color"] == "BROWN") & (my_df["Breed"] == "MIXED")]
print(brown_mixed)

print("\nCount of rows matching both conditions:")
print(len(brown_mixed))

# ====================== Multiple Conditions (OR) ===================
print("\nRows where Color == 'BROWN' OR Breed == 'MIXED':")
brown_or_mixed = my_df[(my_df["Color"] == "BROWN") | (my_df["Breed"] == "MIXED")]
print(brown_or_mixed)

print("\nCount of rows matching OR condition:")
print(len(brown_or_mixed))

print("\nDog names from rows matching OR condition:")
print(brown_or_mixed["DogName"])

# ========================== Teaching Notes =========================
r"""
Teaching Notes:

1. Boolean masks:
   - my_df == "BROWN" → DataFrame of True/False
   - my_df[mask] → returns only rows where mask is True

2. Column-specific filtering:
   - my_df["Color"] == "BROWN"
   - my_df[my_df["Color"] == "BROWN"]

3. AND vs OR:
   - AND uses &  → both conditions must be True
   - OR uses |   → either condition can be True
   - Parentheses are required:
       (cond1) & (cond2)

4. Selecting columns after filtering:
   - my_df[mask]["Column"]
   - my_df[mask][["Col1", "Col2"]]

5. Counting matches:
   - len(my_df[mask])
"""

# ========================== Examples ===============================
r"""
Examples:

df[df["Age"] > 10]
df[(df["Color"] == "BLACK") & (df["Breed"] == "LAB")]
df[(df["Weight"] < 20) | (df["Age"] > 12)]
df[df["Name"] == "FIDO"]["Breed"]
"""

# ====================== Common Mistakes ============================
r"""
Common Mistakes:

- Forgetting parentheses:
    df[df["Color"] == "BROWN" & df["Breed"] == "MIXED"] → ERROR

- Using 'and'/'or' instead of & and |:
    df[(cond1) and (cond2)] → ERROR

- Forgetting print() in VS Code:
    df[df["Color"] == "BROWN"]  # does nothing

- Using a single bracket for multiple columns:
    df[["Col1", "Col2"]]  ← correct
    df["Col1", "Col2"]    ← incorrect
"""

# ========================== Takeaways ==============================
r"""
Key Takeaways:

- Boolean masks are the foundation of DataFrame filtering.
- Use ==, !=, <, >, <=, >= for comparisons.
- Use & for AND and | for OR (with parentheses).
- You can filter rows and then select specific columns.
- len() gives you the number of matching rows.
"""
