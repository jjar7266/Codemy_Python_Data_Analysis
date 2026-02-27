"""
Lesson 08 — NumPy Searching (np.where)
Codemy.com — Instructor: John Elder

This lesson covers:
- Using np.where() to locate values in arrays
- Returning index positions
- Extracting matching values using boolean masks
- Searching for multiple matches
- Searching with conditions (even, odd, greater than, etc.)
- How np.where behaves with 1-D and 2-D arrays
- Extra examples: boolean masks, chaining conditions, and advanced filtering

Notes:
- John uses Google Colab; this version is adapted for VS Code.
- Imports must be at the top in script workflow.
"""

# ========================== Imports ===============================
import numpy as np

# ====================== Basic Searching ===========================
np1 = np.array([1,2,3,4,5,6,7,8,9,10])

x = np.where(np1 == 3)
print("Index where value == 3:", x[0])
print("Value at that index:", np1[x])

# ====================== Multiple Matches ==========================
np1 = np.array([1,2,3,4,5,6,7,8,9,10,3])

x = np.where(np1 == 3)
print("\nIndices where value == 3:", x)
print("Values at those indices:", np1[x])

# ====================== Even Numbers ==============================
y = np.where(np1 % 2 == 0)
print("\nIndices of even numbers:", y)
print("Even numbers:", np1[y])

# ====================== Odd Numbers ===============================
y = np.where(np1 % 2 == 1)
print("\nIndices of odd numbers:", y)
print("Odd numbers:", np1[y])

# ====================== Greater Than Condition ====================
y = np.where(np1 > 5)
print("\nIndices where value > 5:", y)
print("Values > 5:", np1[y])

# ====================== Extra Examples ============================

# Boolean mask without np.where
mask = np1 > 5
print("\nBoolean mask (np1 > 5):", mask)
print("Filtered using mask:", np1[mask])

# Using np.where with multiple conditions
cond = np.where((np1 > 3) & (np1 < 9))
print("\nValues between 4 and 8:", np1[cond])

# Using np.where to replace values (ternary behavior)
np2 = np.where(np1 % 2 == 0, "Even", "Odd")
print("\nReplacing values with labels (Even/Odd):")
print(np2)

# Searching in 2-D arrays
np3 = np.array([
    [1, 5, 3],
    [3, 8, 3],
    [9, 3, 2]
])

loc = np.where(np3 == 3)
print("\n2-D array indices where value == 3:")
print("Row indices:", loc[0])
print("Col indices:", loc[1])
print("Values:", np3[loc])

# ====================== Searching Rules ===========================
"""
Searching Rules:
- np.where(condition) returns a tuple of index arrays.
- For 1-D arrays, the result is (array_of_indices,).
- For 2-D arrays, the result is (row_indices, col_indices).
- np.where can be used for:
  - locating values
  - filtering values
  - building boolean masks
  - conditional replacement (like a vectorized ternary operator)
- Boolean masks (arr[mask]) are often cleaner than np.where for filtering.
"""

# ========================== Takeaways =============================
"""
Key Takeaways:
- np.where() returns index positions, not values.
- Use arr[indices] to extract the matching values.
- Boolean masks are often the simplest way to filter arrays.
- np.where supports full conditional logic (>, <, ==, %, etc.).
- In 2-D arrays, np.where returns row and column index arrays.
- np.where(condition, A, B) acts like a vectorized if/else.
"""
