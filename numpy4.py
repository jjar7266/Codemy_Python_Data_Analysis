"""
Lesson 04 — NumPy Arrays: Copy vs View
Codemy.com — Instructor: John Elder

This lesson covers:
- The difference between a NumPy *view* and a *copy*
- How views share memory with the original array
- How copies create independent data
- How slicing behaves (views by default)
- How reshaping often returns a view
- How to check memory ownership using `.base`
- When to use views vs. copies in real data workflows

Notes:
- John uses Google Colab; this version is adapted for VS Code.
- Imports must be at the top in script workflow.
"""

# ========================== Imports ===============================
import numpy as np

# ====================== Base Array ================================
np1 = np.array([1, 2, 3, 4, 5])
print("Original np1:", np1)

# ====================== Creating a View ===========================
# A view shares memory with the original array.
np2 = np1.view()

print("\nView created:")
print("np1:", np1)
print("np2 (view):", np2)

# Modify original
np1[0] = 41

print("\nAfter modifying np1:")
print("np1:", np1)
print("np2 (view reflects change):", np2)

# ====================== Creating a Copy ===========================
# A copy does NOT share memory with the original.
np3 = np1.copy()
# Alternative: np3 = np.array(np1)

print("\nCopy created:")
print("np1:", np1)
print("np3 (copy):", np3)

# Modify original again
np1[0] = 99

print("\nAfter modifying np1 again:")
print("np1:", np1)
print("np3 (copy does NOT change):", np3)

# ====================== Memory Checks =============================
print("\nMemory checks:")
print("np2 is a view (shares memory):", np2.base is np1)
print("np3 is a copy (owns its data):", np3.base is None)

# ====================== Slicing Creates a View ====================
slice_view = np1[1:4]
print("\nSlice view (np1[1:4]):", slice_view)

np1[1] = 777
print("After modifying np1:")
print("np1:", np1)
print("slice_view (reflects change):", slice_view)

# ====================== Forcing a Copy from a Slice ===============
slice_copy = np1[1:4].copy()
np1[1] = 123

print("\nSlice copy (independent):", slice_copy)
print("np1:", np1)

# ====================== Reshape Often Returns a View ==============
reshaped = np1.reshape(5, 1)
print("\nReshaped array:")
print(reshaped)
print("Reshaped shares memory:", reshaped.base is np1)

# Modify reshaped to show linkage
reshaped[0, 0] = 555
print("\nAfter modifying reshaped:")
print("reshaped:", reshaped)
print("np1 (reflects change):", np1)

# ====================== Helper Function for Debugging =============
def inspect(arr, name):
    print(f"{name}: {arr}, base -> {arr.base}")

print("\nInspecting arrays:")
inspect(np1, "np1")
inspect(np2, "np2 (view)")
inspect(np3, "np3 (copy)")
inspect(slice_view, "slice_view")
inspect(slice_copy, "slice_copy")
inspect(reshaped, "reshaped")

# ========================== Takeaways =============================
# - A *view* shares memory with the original array.
# - A *copy* creates a completely independent array.
# - Slicing produces a view unless explicitly copied.
# - Reshaping often returns a view (depends on memory layout).
# - Modifying the original modifies all views.
# - Copies remain unchanged when the original changes.
# - Use .base to check whether an array owns its data.
# - Views are fast and memory-efficient; copies are safer but heavier.
# - Understanding this is essential for Pandas, ML preprocessing, and large datasets.
