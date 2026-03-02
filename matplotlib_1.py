# pyright: reportGeneralTypeIssues=false
r"""
Lesson 21 — Charts and Graphs with Matplotlib
Codemy.com — Instructor: John Elder

This lesson covers:
- Creating histograms with Matplotlib
- Adjusting bins, legends, and gridlines
- Creating area plots (stacked and unstacked)
- Using transparency (alpha) and titles
- Plotting individual columns and subsets
- Adding tables to Matplotlib charts

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
print("Creating random DataFrame for Matplotlib charts...")
my_df = pd.DataFrame(randn(100, 4), columns=["Mon", "Tues", "Wed", "Thur"])
print(my_df.head())

# ========================== Histograms ============================
print("\nCreating histograms...")

# Basic histogram
my_df["Wed"].hist()
plt.show()

# Histogram with smaller bins
my_df["Wed"].hist(bins=20)
plt.show()

# Second method using plot(kind="hist")
my_df["Wed"].plot(kind="hist")
plt.show()

# Histogram without gridlines
my_df["Wed"].hist(bins=20, grid=False)
plt.show()

# Histogram with legend
my_df["Wed"].hist(bins=20, grid=False, legend=True)
plt.show()

# ========================== Area Plots ============================
print("\nCreating area plots...")

# New random DataFrame for area plots
my_df = pd.DataFrame(randn(20, 4), columns=["Mon", "Tues", "Wed", "Thur"])
print(my_df.head())

# Basic area plot
my_df.plot(kind="area", stacked=False)
plt.show()

# Absolute values
my_df.abs().plot(kind="area")
plt.show()

# Transparency
my_df.abs().plot(kind="area", alpha=0.3)
plt.show()

# Title
my_df.abs().plot(kind="area", alpha=0.3, title="My Very Cool Area Plot")
plt.show()

# Remove legend
my_df.abs().plot(kind="area", alpha=0.3, title="My Very Cool Area Plot", legend=False)
plt.show()

# Plot only one column
my_df["Mon"].abs().plot(kind="area", alpha=0.3, title="My Very Cool Area Plot")
plt.show()

# Plot two columns
my_df[["Mon", "Wed"]].abs().plot(
    kind="area", alpha=0.3, title="My Very Cool Area Plot", legend=False
)
plt.show()

# Basic area plot (Shift+Tab in Jupyter shows function info)
my_df.plot(kind="area")
plt.show()

# Add table under the chart
my_df.abs().plot(
    kind="area", alpha=0.3, title="My Very Cool Area Plot", legend=False, table=True
)
plt.show()

# ========================== Teaching Notes =========================
r"""
Teaching Notes:

1. Matplotlib:
   - The foundation of Python plotting.
   - Pandas uses Matplotlib under the hood for .plot().

2. Histograms:
   - Show distribution of numeric data.
   - bins controls granularity.
   - grid=False removes background gridlines.

3. Area Plots:
   - Show cumulative or individual values over an index.
   - stacked=False separates the lines.
   - alpha controls transparency.

4. Titles and Legends:
   - title="..." adds a chart title.
   - legend=False hides the legend.

5. Tables:
   - table=True adds a data table below the chart.
"""

# ========================== Examples ===============================
r"""
Examples:

df["Age"].hist(bins=30)
df.plot(kind="area", stacked=True)
df["Sales"].plot(kind="area", alpha=0.5)
df[["A", "B"]].plot(kind="area", legend=False)
df.plot(kind="area", table=True)
"""

# ====================== Common Mistakes ============================
r"""
Common Mistakes:

- Forgetting plt.show() in VS Code (plots may not appear).
- Using %matplotlib inline outside Jupyter (not needed in VS Code).
- Plotting negative values in area charts (use abs()).
- Expecting legends to appear when legend=False is set.
"""

# ========================== Takeaways ==============================
r"""
Key Takeaways:

- Matplotlib is the core plotting library behind Pandas and Seaborn.
- Histograms, area plots, and tables are easy to create with .plot().
- alpha, bins, legend, and title provide powerful customization.
"""
