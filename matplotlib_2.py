# pyright: reportGeneralTypeIssues=false
r"""
Lesson 22 — Matplotlib: Charts and Graphs (Bars, Lines, Scatter, Box, Hexbin, KDE)
Codemy.com — Instructor: John Elder

This lesson covers:
- Bar charts (stacked, shaded, gridlines, legends)
- Line charts (width, subsets, transparency, sizing)
- Scatterplots with color, size, and colormaps
- Boxplots with size, color, grid, and titles
- Hexbin plots for density visualization
- KDE and density plots
- Using Pandas .plot() as a wrapper around Matplotlib

Notes:
- Adapted for VS Code (plots appear in the interactive window)
- %matplotlib inline is not needed in VS Code
"""

# ========================== Imports ===============================
import pandas as pd
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt

# ========================== Create Data ===========================
print("Creating random DataFrame for Matplotlib bar and line charts...")
my_df = pd.DataFrame(randn(20, 4), columns=["Mon", "Tues", "Wed", "Thur"])
print(my_df.head())

# ========================== Bar Charts ============================
print("\nCreating bar charts...")

my_df.abs().plot(kind="bar")
plt.show()

my_df.abs().plot(kind="bar", stacked=True)
plt.show()

my_df.abs().plot(kind="bar", stacked=True, grid=True)
plt.show()

my_df.abs().plot(kind="bar", stacked=True, alpha=0.5)
plt.show()

my_df.abs().plot(kind="bar", stacked=True, alpha=0.5, title="My Awesome BarChart")
plt.show()

my_df.abs().plot(kind="bar", stacked=True, alpha=0.5, legend=False)
plt.show()

# Second way
my_df.abs().plot.bar()
plt.show()

my_df.abs().plot.bar(stacked=True)
plt.show()

my_df.abs().plot.bar(stacked=True, alpha=0.5)
plt.show()

my_df.abs().plot.bar(stacked=True, alpha=0.5, title="My 2nd BarChart")
plt.show()

my_df.abs().plot.bar(stacked=True, alpha=0.5, legend=False)
plt.show()

my_df.abs().plot.bar(stacked=True, alpha=0.5, grid=True)
plt.show()

# ========================== Line Charts ===========================
print("\nCreating line charts...")

my_df.abs().plot(kind="line")
plt.show()

my_df.abs().plot(kind="line", lw=3)
plt.show()

my_df["Mon"].abs().plot(kind="line")
plt.show()

my_df[["Mon", "Tues"]].abs().plot(kind="line")
plt.show()

my_df.abs().plot(kind="line", figsize=(10, 5))
plt.show()

my_df.abs().plot(kind="line", title="My Not Awesome LineChart")
plt.show()

my_df.abs().plot(kind="line", alpha=0.6)
plt.show()

my_df.abs().plot(kind="line", legend=False)
plt.show()

# Second way
my_df.abs().plot.line(lw=3)
plt.show()

# ========================== New Data for Scatter ==================
print("\nCreating new DataFrame for scatter, box, hexbin, and KDE plots...")
my_df = pd.DataFrame(randn(500, 4), columns=["Mon", "Tues", "Wed", "Thur"])
print(my_df.head())

# ========================== Scatterplots ==========================
print("\nCreating scatterplots...")

my_df.plot(kind="scatter", x="Mon", y="Tues")
plt.show()

my_df.plot(kind="scatter", x="Mon", y="Tues", c="Wed")
plt.show()

my_df.plot(kind="scatter", x="Mon", y="Tues", c="Wed", cmap="seismic")
plt.show()

my_df.plot(kind="scatter", x="Mon", y="Tues", s=my_df["Wed"] * 100, cmap="seismic")
plt.show()

my_df.plot(
    kind="scatter",
    x="Mon",
    y="Tues",
    s=my_df["Wed"] * 100,
    cmap="seismic",
    alpha=0.3
)
plt.show()

my_df.plot(
    kind="scatter",
    x="Mon",
    y="Tues",
    s=my_df["Wed"] * 200,
    cmap="seismic",
    alpha=0.3,
    title="My Groovy Scatterplot",
    legend=True
)
plt.show()

# ========================== Boxplots ==============================
print("\nCreating boxplots...")

my_df.plot(kind="box")
plt.show()

my_df.plot(kind="box", figsize=(10, 5))
plt.show()

my_df.plot(kind="box", figsize=(10, 5), cmap="bwr")
plt.show()

my_df.plot(kind="box", figsize=(10, 5), cmap="bwr", legend=True)
plt.show()

my_df.plot(kind="box", figsize=(10, 5), cmap="bwr", grid=True)
plt.show()

my_df.plot(kind="box", figsize=(10, 5), cmap="bwr", title="Whiskers!")
plt.show()

# Second way
my_df.plot.box()
plt.show()

# ========================== Hexbin Plots ==========================
print("\nCreating hexbin plots...")

my_df.plot(kind="hexbin", x="Mon", y="Tues")
plt.show()

my_df.plot(kind="hexbin", x="Mon", y="Tues", gridsize=10)
plt.show()

my_df.plot(kind="hexbin", x="Mon", y="Tues", C="Wed", gridsize=10)
plt.show()

my_df.plot(kind="hexbin", x="Mon", y="Tues", gridsize=10, cmap="jet")
plt.show()

my_df.plot(kind="hexbin", x="Mon", y="Tues", gridsize=10, grid=True)
plt.show()

my_df.plot(kind="hexbin", x="Mon", y="Tues", gridsize=10, title="My Hexy!")
plt.show()

# Second way
my_df.plot.hexbin(x="Mon", y="Thur", gridsize=10)
plt.show()

# ========================== KDE & Density ==========================
print("\nCreating KDE and density plots...")

my_df.plot(kind="kde", alpha=0.3, grid=True)
plt.show()

my_df.plot.kde()
plt.show()

my_df.plot(kind="density")
plt.show()

my_df.plot.density()
plt.show()

my_df.plot.density(title="Terrible Densities", legend=True)
plt.show()

# ========================== Teaching Notes =========================
r"""
Teaching Notes:

1. Pandas .plot():
   - A wrapper around Matplotlib.
   - Makes quick charts easy without writing full Matplotlib code.

2. Bar Charts:
   - stacked=True layers values.
   - alpha controls transparency.
   - grid=True adds background gridlines.

3. Line Charts:
   - lw controls line width.
   - figsize adjusts chart size.
   - legend=False hides the legend.

4. Scatterplots:
   - c="Column" colors points by a variable.
   - cmap chooses a colormap.
   - s sets point size (can be scaled by a column).

5. Boxplots:
   - Show distribution, quartiles, and outliers.
   - cmap applies color maps.

6. Hexbin:
   - Great for large scatter datasets.
   - gridsize controls resolution.

7. KDE / Density:
   - Smooth distribution curves.
   - density() is an alias for kde().
"""

# ========================== Examples ===============================
r"""
Examples:

df.abs().plot(kind="bar", stacked=True)
df.plot(kind="line", figsize=(12, 6))
df.plot(kind="scatter", x="Height", y="Weight", c="Age", cmap="viridis")
df.plot(kind="box", cmap="coolwarm")
df.plot(kind="hexbin", x="A", y="B", gridsize=20)
df.plot(kind="kde", alpha=0.4)
"""

# ====================== Common Mistakes ============================
r"""
Common Mistakes:

- Forgetting plt.show() in VS Code.
- Using %matplotlib inline outside Jupyter.
- Plotting negative values in area/bar charts without abs().
- Expecting scatterplots to show patterns with too little data.
"""

# ========================== Takeaways ==============================
r"""
Key Takeaways:

- Matplotlib is the foundation of Python visualization.
- Pandas .plot() makes charts fast and flexible.
- Bar, line, scatter, box, hexbin, and KDE plots reveal different insights.
- alpha, cmap, gridsize, and figsize offer powerful customization.
"""
