"""
Lesson 07 — NumPy Sorting
Codemy.com — Instructor: John Elder

This lesson covers:
- Sorting numeric, string, and boolean arrays
- Understanding np.sort() vs. ndarray.sort()
- Sorting 2‑D arrays row‑wise
- Reversing sorted arrays (descending order)
- Stability of NumPy’s sorting algorithm
- Extra examples: axis sorting, argsort, and custom sorting patterns

Notes:
- John uses Google Colab; this version is adapted for VS Code.
- Imports must be at the top in script workflow.
"""

# ========================== Imports ===============================
import numpy as np

# ====================== Sorting Numerically =======================
np1 = np.array([6, 7, 4, 9, 0, 2, 1])
print("Original numeric array:", np1)

print("\nSorted ascending:")
print(np.sort(np1))  # returns a new array

# ====================== Reversing (Descending) ====================
np9 = np.sort(np1)
print("\nAscending:", np9)

np9 = np9[::-1]  # reverse using slicing
print("Descending:", np9)

# ====================== Sorting Strings ===========================
np2 = np.array(["John", "Bob", "April", "Aspen", "Sally"])
print("\nOriginal string array:", np2)

print("Sorted alphabetically:")
print(np.sort(np2))

# ====================== Sorting Booleans ==========================
np3 = np.array([True, False, False, True])
print("\nOriginal boolean array:", np3)

print("Sorted booleans (False=0, True=1):")
print(np.sort(np3))

# ====================== Sorting 2-D Arrays =========================
np4 = np.array([
    [6, 7, 1, 9],
    [8, 3, 5, 0]
])

print("\n2-D array sorted row-wise:")
print(np.sort(np4))  # sorts each row independently

# ====================== Extra Examples ============================

# Sort along columns instead of rows
print("\nSort 2-D array by columns (axis=0):")
print(np.sort(np4, axis=0))

# Sort along rows (axis=1) — same as default
print("\nSort 2-D array by rows (axis=1):")
print(np.sort(np4, axis=1))

# Using argsort to get sorted indices
np5 = np.array([50, 10, 40, 20])
print("\nargsort gives sorted indices:")
print(np.argsort(np5))

print("Using argsort to sort manually:")
print(np5[np.argsort(np5)])

# Sorting structured data (key-based sorting)
people = np.array(
    [('John', 25), ('April', 19), ('Bob', 30)],
    dtype=[('name', 'U10'), ('age', 'i4')]
)

print("\nSorting structured array by age:")
print(np.sort(people, order='age'))

# ====================== Sorting Rules =============================
"""
Sorting Rules:
- np.sort() returns a new sorted array.
- arr.sort() sorts the array in-place.
- Sorting is stable: equal elements preserve original order.
- Strings sort alphabetically (lexicographically).
- Booleans sort as integers: False (0) before True (1).
- 2-D sorting defaults to row-wise (axis=1).
- Use axis=0 to sort by columns.
- argsort() returns the indices that would sort the array.
"""

# ========================== Takeaways =============================
"""
Key Takeaways:
- np.sort() is non-destructive; arr.sort() modifies the array.
- Sorting works on numbers, strings, booleans, and structured data.
- Use slicing [::-1] to reverse for descending order.
- Sorting 2-D arrays defaults to row-wise; axis controls direction.
- argsort() is essential for advanced workflows (ranking, ordering).
- NumPy uses stable sorting, which preserves order among equals.
"""
