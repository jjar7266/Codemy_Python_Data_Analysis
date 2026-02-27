"""
Lesson 09 — NumPy Filtering (Boolean Masking)
Codemy.com — Instructor: John Elder

This lesson covers:
- Filtering arrays using boolean index lists
- Building boolean masks manually
- Using conditions to generate masks
- Filtering with multiple conditions
- Shorthand boolean expressions
- Why boolean masks are the foundation of NumPy + Pandas filtering

Notes:
- John uses Google Colab; this version is adapted for VS Code.
- Imports must be at the top in script workflow.
"""

# ========================== Imports ===============================
import numpy as np

# ====================== Basic Boolean Filtering ====================
np1 = np.array([1,2,3,4,5,6,7,8,9,10])

# Filter out the first two items
mask = [True, True, False, False, False, False, False, False, False, False]
print("Original array:", np1)
print("Filtered (first two items):", np1[mask])

# ====================== Building Masks Manually ====================
filtered = []
for item in np1:
    if item % 2 == 0:
        filtered.append(True)
    else:
        filtered.append(False)

print("\nManual even-number mask:", filtered)
print("Even numbers:", np1[filtered])

# ====================== Any Logic for Filtering ====================
filtered = []
for item in np1:
    if item > 5:
        filtered.append(True)
    else:
        filtered.append(False)

print("\nManual mask for values > 5:", filtered)
print("Values > 5:", np1[filtered])

# ====================== Shorthand Boolean Masks ====================
mask = np1 % 2 == 1
print("\nOdd numbers using shorthand mask:", np1[mask])

# ====================== Extra Examples =============================

# Filter values between 3 and 8
mask = (np1 >= 3) & (np1 <= 8)
print("\nValues between 3 and 8:", np1[mask])

# Filter values NOT equal to 5
mask = np1 != 5
print("Values not equal to 5:", np1[mask])

# Filter using OR logic
mask = (np1 < 3) | (np1 > 8)
print("Values < 3 OR > 8:", np1[mask])

# Filtering 2-D arrays
np2 = np.array([
    [1, 5, 3],
    [8, 2, 7],
    [4, 9, 6]
])

mask = np2 > 5
print("\n2-D mask (values > 5):")
print(mask)
print("Filtered values:", np2[mask])

# ====================== Filtering Rules ============================
"""
Filtering Rules:
- Boolean masks must be the same length/shape as the array.
- True means "keep this element"; False means "discard it".
- Masks can be built manually or generated using conditions.
- Conditions use elementwise operators: ==, !=, >, <, >=, <=.
- Combine conditions with & (AND), | (OR), ~ (NOT).
- Boolean masks are the foundation of Pandas filtering.
"""

# ========================== Takeaways =============================
"""
Key Takeaways:
- Boolean masks are the most powerful and common way to filter arrays.
- np.where gives indices; boolean masks give values directly.
- Masks can be built manually, but condition-based masks are cleaner.
- Combine conditions with &, |, and ~ for advanced filtering.
- Filtering works identically for 1-D and 2-D arrays.
"""
