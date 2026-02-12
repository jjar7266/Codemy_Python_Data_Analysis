"""
Lesson 01 — Python Intro to Data Analysis
Codemy.com — Instructor: John Elder

This lesson covers:
- Basic Python lists
- Introduction to NumPy arrays
- Array creation methods (arange, zeros, full)
- Multi-dimensional arrays
- Converting Python lists to NumPy arrays

Notes:
- John uses Google Colab; this version is adapted for VS Code.
- Imports must be at the top in script workflow.
"""

# ========================== Imports ===============================
import numpy as np

# ========================== Python Lists ==========================
my_list = [1, 2, 3, 4, 5, "John", True]
my_list2 = [6, 7, 8, my_list]

# ========================== NumPy Arrays ==========================
np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np1)
print(np1[2])

# Shape (similar to len(), but for arrays)
print(np1.shape)

# ========================== Arange ================================
np2 = np.arange(10)
print(np2)

# Step values
np3 = np.arange(0, 10, 2)
print(np3)

# ========================== Zeros =================================
np4 = np.zeros(10)
print(np4)

# Multi-dimensional zeros
np5 = np.zeros((5, 10))
print(np5)

# ========================== Full ==================================
np6 = np.full((10,), "Joe")
print(np6)

# Multi-dimensional full
np7 = np.full((2, 10), "Joe")
print(np7)

# Convert Python list to NumPy array
my_list3 = [0, 1, 2, 3, 4, 5]
np8 = np.array(my_list3)
print(np8)
print(my_list3)

# ========================== Takeaways =============================
# - NumPy arrays are typed and more efficient than Python lists.
# - np.arange() works like range() but returns an array.
# - np.zeros() and np.full() are useful for initializing data structures.
# - Multi-dimensional arrays are created by passing tuples for shape.