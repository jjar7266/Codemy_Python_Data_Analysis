"""
Lesson 05 — NumPy Shape and Reshape
Codemy.com — Instructor: John Elder

This lesson covers:
- Understanding array shape (1‑D, 2‑D, 3‑D)
- Reshaping arrays into new dimensions
- Flattening arrays using reshape(-1)
- Rules for reshape validity
- How reshape interacts with memory (views vs. copies)
- How to reshape safely in real data workflows

Notes:
- John uses Google Colab; this version is adapted for VS Code.
- Imports must be at the top in script workflow.
"""

# ========================== Imports ===============================
import numpy as np

# ====================== 1-D Array Shape ===========================
np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("np1 shape:", np1.shape)   # (12,)

# ====================== 2-D Array Shape ===========================
np2 = np.array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12]
])
print("np2 shape:", np2.shape)   # (2, 6)

# ====================== Reshape to 2-D ============================
np3 = np1.reshape(3, 4)
print("\nReshaped to 3x4:")
print(np3)
print("np3 shape:", np3.shape)

# ====================== Reshape to 3-D ============================
np4 = np1.reshape(2, 3, 2)
print("\nReshaped to 2x3x2:")
print(np4)
print("np4 shape:", np4.shape)

# ====================== Flatten to 1-D ============================
np5 = np4.reshape(-1)
print("\nFlattened to 1-D using reshape(-1):")
print(np5)
print("np5 shape:", np5.shape)

# ====================== Flatten to 2-D ============================
np6 = np4.reshape(-1, 2)
print("\nFlattened to 2-D (rows auto-calculated):")
print(np6)
print("np6 shape:", np6.shape)

# ====================== Extra Examples ============================

# Auto-calc rows using -1
np7 = np1.reshape(-1, 6)
print("\nAuto-calc rows (reshape(-1, 6)):")
print(np7)

# Auto-calc columns using -1
np8 = np1.reshape(4, -1)
print("\nAuto-calc columns (reshape(4, -1)):")
print(np8)

# Reshape returns a VIEW when possible
reshaped_view = np1.reshape(3, 4)
print("\nReshape returns a view (when memory layout allows):")
print("reshaped_view.base is np1:", reshaped_view.base is np1)

# Modify reshaped_view to show linkage
reshaped_view[0, 0] = 999
print("\nAfter modifying reshaped_view:")
print("reshaped_view:", reshaped_view)
print("np1 (reflects change):", np1)

# Force a copy if needed
reshaped_copy = np1.reshape(3, 4).copy()
print("\nreshaped_copy.base is None (independent):", reshaped_copy.base is None)

# ====================== Reshape Rules =============================
"""
Reshape Rules:
1. Total number of elements must remain the same.
   Example: 12 elements → valid shapes include:
   - (3, 4)
   - (2, 6)
   - (2, 3, 2)
   - (12,)
   - (1, 12)
   - (12, 1)

2. Only ONE dimension may be -1.
   NumPy will auto-calculate that dimension.

3. reshape() returns a VIEW when possible.
   If memory layout is incompatible, it returns a COPY.

4. reshape(-1) is the fastest way to flatten an array.
"""

# ========================== Takeaways =============================
"""
Key Takeaways:
- shape tells you the dimensionality of an array.
- reshape changes the view of the data without changing the data itself.
- reshape returns a view when possible (fast), otherwise a copy.
- reshape(-1) is the universal flattening tool.
- Only one dimension can be -1.
- The total number of elements must remain constant.
- Understanding shape/reshape is essential for:
  - machine learning model inputs
  - image processing
  - Pandas reshaping (wide ↔ long)
  - batch processing in deep learning
"""
