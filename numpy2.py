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
print(np1[1:5])
np2 = np1[1:5]
print(np2)

# ====================== Slice to End ==============================
print(np1[3:])

# ====================== Negative Slicing ==========================
print(np1[-3:-1])

# ====================== Slicing with Steps ========================
print(np1[1:5])
print(np1[1:5:3])

# ====================== Whole Array with Steps ====================
print(np1)
print(np1[::2])

# ====================== 2‑D Array Slicing =========================
np2 = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

print(np2)
print(np2[1, 2])
print(np2[0:1, 1:3])
print(np2[0:2, 1:3])

# ========================== Takeaways =============================
# - Slicing in NumPy works like Python lists but is more powerful.
# - Slices are always [start:stop] where stop is NOT included.
# - Negative indices count from the end of the array.
# - Steps allow skipping elements: [start:stop:step].
# - 2‑D slicing uses [row_slice, column_slice].
# - NumPy slicing returns views, not copies (important later).