"""
Lesson 02 — NumPy Slicing
Codemy.com — Instructor: John Elder

This lesson covers:
- Basic slicing of 1‑D NumPy arrays
- Negative indexing
- Step slicing
- Slicing entire arrays with steps
- Slicing 2‑D arrays (rows, columns, sub‑matrices)
- Extracting individual elements

Notes:
- John uses Google Colab; this version is adapted for VS Code.
- Imports must be at the top in script workflow.
"""

# ========================== Imports ===============================
import numpy as np

# ====================== Create Base Array =========================
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# ====================== Basic Slicing =============================
# Return 2, 3, 4, 5
# Slice 1:5 returns index 1 up to (but not including) index 5
print(np1[1:5])
np2 = np1[1:5]
print(np2)

# Expected:
# [2 3 4 5]
# [2 3 4 5]

# ====================== Slice to End ==============================
# 3: means start at index 3 and go to the end
print(np1[3:])

# Expected:
# [4 5 6 7 8 9]

# ====================== Negative Slicing ==========================
# -3:-1 means start 3 from the end, stop 1 from the end (not including -1)
print(np1[-3:-1])

# Expected:
# [7 8]

# ====================== Slicing with Steps ========================
print(np1[1:5])     # normal slice
print(np1[1:5:3])   # step of 3

# Expected:
# [2 3 4 5]
# [2 5]

# ====================== Whole Array with Steps ====================
print(np1)
print(np1[::2])     # every other element

# Expected:
# [1 2 3 4 5 6 7 8 9]
# [1 3 5 7 9]

# ====================== 2‑D Array Slicing =========================
np2 = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

print(np2)

# Expected:
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]

# Pull out a single item (8)
print(np2[1, 2])

# Expected:
# 8

# Slice from first row, columns 1 to 3 (2, 3)
print(np2[0:1, 1:3])

# Expected:
# [[2 3]]

# Slice from both rows, columns 1 to 3 (2,3 and 7,8)
print(np2[0:2, 1:3])

# Expected:
# [[2 3]
#  [7 8]]

# ========================== Takeaways =============================
# - Slicing in NumPy works like Python lists but is more powerful.
# - Slices are always [start:stop] where stop is NOT included.
# - Negative indices count from the end of the array.
# - Steps allow skipping elements: [start:stop:step].
# - 2‑D slicing uses [row_slice, column_slice].
# - NumPy slicing returns views, not copies (important later).

