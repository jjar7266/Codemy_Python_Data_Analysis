"""
Lesson 03 — NumPy Universal Functions (ufuncs)
Codemy.com — Instructor: John Elder

This lesson covers:
- What universal functions (ufuncs) are
- Applying math operations element‑wise to NumPy arrays
- Square root, absolute value, exponential
- Min/Max operations
- Sign function
- Logarithms
- Broadcasting with scalars
- Ufuncs on 2‑D arrays
- Memory‑efficient operations using `out=`

Notes:
- John uses Google Colab; this version is adapted for VS Code.
- Imports must be at the top in script workflow.
- VS Code will show warnings for invalid math (sqrt/log of negatives).
"""

# ========================== Imports ===============================
import numpy as np

# Optional: suppress warnings for invalid values (sqrt/log of negatives)
np.seterr(invalid='ignore', divide='ignore')

# ====================== Create Base Array =========================
np1 = np.array([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Base array:", np1)

# ====================== Square Root ===============================
print("\nSquare root:")
print(np.sqrt(np1))   # negative values → nan

# ====================== Absolute Value ============================
print("\nAbsolute value:")
print(np.absolute(np1))

# ====================== Exponential ===============================
print("\nExponential:")
print(np.exp(np1))

# ====================== Min / Max ================================
print("\nMin/Max:")
print("Max value:", np.max(np1))

# ====================== Sign Function =============================
print("\nSign function (-1, 0, 1):")
print(np.sign(np1))

# ====================== Logarithms ================================
print("\nNatural log:")
print(np.log(np1))    # negative/zero → nan or -inf

# ====================== Ufuncs on 2-D Arrays ======================
np2 = np.array([
    [1, 4, 9],
    [16, 25, 36]
])

print("\n2-D array:")
print(np2)

print("\nSquare root of 2-D array:")
print(np.sqrt(np2))

print("\nExponential of 2-D array:")
print(np.exp(np2))

print("\nSign of 2-D array:")
print(np.sign(np2))

# ====================== Broadcasting Examples =====================
print("\nBroadcasting examples:")
print("Add 10:", np1 + 10)
print("Multiply by 2:", np1 * 2)
print("Cubed:", np.power(np1, 3))

# ====================== Memory-Efficient Ufuncs ===================
print("\nMemory-efficient ufunc with 'out=' parameter:")
result = np.empty_like(np1)
np.abs(np1, out=result)
print(result)

# ====================== Combined Transformations ==================
print("\nCombined transformations (log(abs(x) + 1)):")
print(np.log(np.abs(np1) + 1))

# ========================== Takeaways =============================
# - Universal functions (ufuncs) apply operations element‑wise across arrays.
# - They are extremely fast because they are implemented in C.
# - Ufuncs replace Python loops and enable vectorized computing.
# - Broadcasting allows operations between arrays and scalars.
# - Ufuncs work on any dimensionality (1‑D, 2‑D, n‑D).
# - Invalid values (sqrt/log of negatives) produce warnings, not crashes.
# - The `out=` parameter allows memory‑efficient operations.
# - Ufuncs are foundational for Pandas, SciPy, and machine learning workflows.

# Master list of universal functions:
# https://numpy.org/doc/stable/reference/ufuncs.html