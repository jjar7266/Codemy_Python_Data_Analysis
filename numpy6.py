"""
Lesson 06 — NumPy Array Iteration
Codemy.com — Instructor: John Elder

This lesson covers:
- Iterating through 1‑D, 2‑D, and 3‑D NumPy arrays
- Nested loops vs. NumPy's nditer()
- How iteration works across dimensions
- Why manual iteration is rarely used in real NumPy workflows
- Performance considerations and vectorization principles

Notes:
- John uses Google Colab; this version is adapted for VS Code.
- Imports must be at the top in script workflow.
"""

# ========================== Imports ===============================
import numpy as np

# ====================== Iterating 1-D Arrays ======================
np1 = np.array([1, 2, 3, 4, 5])
print("1-D array:", np1)

print("\nIterating 1-D array:")
for x in np1:
    print(x)

# ====================== Iterating 2-D Arrays ======================
np2 = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

print("\nIterating 2-D array (nested loops):")
for row in np2:
    for value in row:
        print(value)

# ====================== Iterating 3-D Arrays ======================
np3 = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

print("\nIterating 3-D array (triple nested loops):")
for block in np3:
    for row in block:
        for value in row:
            print(value)

# ====================== Using np.nditer() =========================
print("\nIterating with np.nditer():")
for value in np.nditer(np3):
    print(value)

# ====================== Extra Examples ============================

# Iterating with index tracking
print("\nIterating with index using np.ndenumerate():")
for idx, value in np.ndenumerate(np3):
    print(f"Index {idx} -> {value}")

# Iterating with modification (requires flags)
np4 = np.array([1, 2, 3, 4])
print("\nModifying array during iteration using nditer:")
for x in np.nditer(np4, op_flags=['readwrite']):
    x[...] = x * 10  # type:ignore
print("Modified np4:", np4)

# Flattening before iteration
print("\nIterating over flattened array:")
for x in np3.flatten():
    print(x)

# ====================== Performance Notes =========================
"""
Important:
- Manual iteration in NumPy is slow compared to vectorized operations.
- Prefer vectorized math (ufuncs) instead of loops.
- np.nditer() is useful for:
  - inspecting values
  - debugging
  - working with unknown dimensions
  - modifying arrays in-place
- For real data work, avoid Python loops whenever possible.
"""

# ========================== Takeaways =============================
"""
Key Takeaways:
- 1-D arrays iterate like Python lists.
- 2-D and 3-D arrays require nested loops unless using nditer().
- np.nditer() provides a clean, dimension-agnostic way to iterate.
- np.ndenumerate() gives both index and value.
- Iteration is rarely needed in real NumPy workflows because vectorized
  operations are dramatically faster.
- Use iteration mainly for debugging, inspection, or special cases.
"""
