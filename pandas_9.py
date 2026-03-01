# pyright: reportGeneralTypeIssues=false
r"""
Lesson 18 — Functions, Apply(), Lambdas, and Sorting
Codemy.com — Instructor: John Elder

This lesson covers:
- Creating custom functions and applying them to DataFrame columns
- Using apply() with named functions and lambda expressions
- Formatting numeric output
- Applying functions to multiple columns
- Sorting DataFrames by numeric and string values
- Understanding ascending vs descending sorts

Notes:
- This version is adapted for VS Code.
- VS Code requires print() to display DataFrames.
"""

# ========================== Imports ===============================
import pandas as pd
import numpy as np

# ====================== Create DataFrame ===========================
print("Creating DataFrame...")
stuff = {
    "Corporation": ["Apple", "Google", "Meta", "Apple", "Google", "Meta"],
    "Employees": ["John", "April", "Wes", "Aspen", "Beth", "Steph"],
    "Salary": [200, 220, 190, 130, 120, 150]
}
my_df = pd.DataFrame(stuff)
print(my_df)

# ====================== Apply Function to Column ===================
print("\nApplying function to multiply salary by 1000:")

# First version: numeric multiplication (original Codemy lesson step 1)
def times1000(x):
    return x * 1000

print(my_df["Salary"].apply(times1000))


# Second version: formatted with commas (originally reused the same name "times1000")
# NOTE: In the Codemy video, this function was also named times1000, which overwrote the first one.
# To avoid VS Code redeclaration warnings, we rename it here.
def times1000_formatted(x):
    return format(x * 1000, ",d")

print("\nApplying formatted version:")
print(my_df["Salary"].apply(times1000_formatted))

print("\nConvert formatted salary to DataFrame:")
print(pd.DataFrame(my_df["Salary"].apply(times1000_formatted)))

print("\nAppending formatted salary back to DataFrame:")
my_df["Salary"] = my_df["Salary"].apply(times1000_formatted)
print(my_df)

# ====================== Apply Function to Names ====================
print("\nApplying function to add last names:")

def namer(x):
    if x == "John":
        return "John Elder"
    elif x == "April":
        return "April Elder"
    else:
        return x

print(my_df["Employees"].apply(namer))

# ====================== Lambda Functions ===========================
print("\nUsing lambda to format salary again:")
print(my_df["Salary"].apply(lambda x: format(int(x.replace(",", "")) * 1000, ",d")))

print("\nConvert lambda output to DataFrame:")
print(pd.DataFrame(my_df["Salary"].apply(lambda x: format(int(x.replace(",", "")) * 1000, ",d"))))

print("\nAppending lambda output back to DataFrame:")
my_df["Salary"] = my_df["Salary"].apply(lambda x: format(int(x.replace(",", "")) * 1000, ",d"))
print(my_df)

# ====================== Apply to Multiple Columns ==================
print("\nApplying function to multiple columns:")

def names(x):
    return f"Codemy: {x}"

print(my_df[["Corporation", "Employees"]].apply(names))

print("\nConvert multi-column apply to DataFrame:")
print(pd.DataFrame(my_df[["Corporation", "Employees"]].apply(names)))

print("\nOriginal DataFrame remains unchanged:")
print(my_df)

# ====================== Sorting Data ===============================
print("\nSorting salary ascending (not permanent):")
print(my_df.sort_values("Salary"))

print("\nSorting salary descending (permanent):")
my_df.sort_values("Salary", ascending=False, inplace=True)
print(my_df)

print("\nSorting corporations A → Z:")
print(my_df.sort_values("Corporation"))

print("\nSorting corporations Z → A:")
print(my_df.sort_values("Corporation", ascending=False))

print("\nFinal DataFrame:")
print(my_df)

# ========================== Teaching Notes =========================
r"""
Teaching Notes:

1. apply():
   - apply() runs a function on each value in a Series.
   - Works with named functions or lambda expressions.
   - Great for formatting, cleaning, or transforming data.

2. Lambdas:
   - Inline anonymous functions.
   - Useful for quick one-line transformations.

3. Applying to multiple columns:
   - df[["Col1", "Col2"]].apply(func)
   - func receives each row/column depending on axis.

4. Sorting:
   - sort_values("Col") sorts ascending by default.
   - ascending=False sorts descending.
   - inplace=True makes the sort permanent.
"""

# ========================== Examples ===============================
r"""
Examples:

df["Price"].apply(lambda x: x * 1.07)
df["Name"].apply(lambda x: x.upper())
df.sort_values("Age")
df.sort_values("Age", ascending=False)
df[["First", "Last"]].apply(lambda x: x.str.title())
"""

# ====================== Common Mistakes ============================
r"""
Common Mistakes:

- Forgetting to convert formatted strings back to numbers before math.
- Using apply() when vectorized operations would be faster.
- Expecting sort_values() to be permanent without inplace=True.
- Applying functions to multiple columns without selecting them first.
"""

# ========================== Takeaways ==============================
r"""
Key Takeaways:

- apply() is powerful for custom transformations.
- Lambdas allow quick inline functions.
- Sorting is essential for organizing and analyzing data.
- inplace=True determines whether changes persist.
"""
