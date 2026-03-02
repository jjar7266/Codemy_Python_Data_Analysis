# pyright: reportGeneralTypeIssues=false
r"""
Lesson 20 — Seaborn Charts
Codemy.com — Instructor: John Elder

This lesson covers:
- Creating histograms, bar charts, line charts, scatterplots, boxplots, and KDE plots
- Customizing colors, transparency, palettes, and styles
- Understanding how Seaborn works with Pandas DataFrames
- Using random numeric data to demonstrate chart types

Notes:
- Adapted for VS Code (plots appear in the interactive window)
- Uses Seaborn for statistical visualizations
"""

# ========================== Imports ===============================
import matplotlib.pyplot as plt
plt.switch_backend("TkAgg")   # Force real pop-up windows

import pandas as pd
import numpy as np
from numpy.random import randn
import seaborn as sns

# ========================== Create Data ===========================
print("Creating random DataFrame for Seaborn charts...")
my_df = pd.DataFrame(randn(100, 4), columns=["Mon", "Tues", "Wed", "Thur"])
print(my_df.head())

# ========================== Histograms ============================
print("\nCreating histograms...")

plt.figure()
sns.histplot(data=my_df, x="Mon")

plt.figure()
sns.histplot(data=my_df, x="Mon", bins=15, color="green")

plt.figure()
sns.histplot(data=my_df, x="Mon", kde=True, bins=15, color="coral")

plt.figure()
sns.histplot(
    data=my_df, x="Mon", kde=True, bins=15,
    color="coral", alpha=0.3, stat="density"
)

# ========================== Bar Charts ============================
print("\nCreating bar charts...")

means = my_df.abs().mean()
days = my_df.columns

plt.figure()
sns.barplot(x=days, y=means)

plt.figure()
sns.barplot(x=days, y=means, palette="coolwarm", hue=days)

plt.figure()
sns.barplot(y=days, x=means, palette="Set2", hue=days)

plt.figure()
sns.barplot(
    x=days, y=means, palette="coolwarm",
    hue=days, width=0.2, alpha=0.3
)

# ========================== Line Charts ===========================
print("\nCreating line charts...")

plt.figure()
sns.lineplot(data=abs(my_df), x=my_df.index, y="Mon")

plt.figure()
sns.lineplot(abs(my_df), alpha=0.9)

plt.figure()
sns.lineplot(
    data=abs(my_df), x=my_df.index, y="Mon",
    marker="o", linewidth=2, color="purple"
)

plt.figure()
sns.lineplot(
    data=abs(my_df), x=my_df.index, y="Mon",
    marker="o", linewidth=2, color="purple", alpha=0.3
)

# ========================== Scatterplots ==========================
print("\nCreating scatterplots...")

plt.figure()
sns.scatterplot(data=my_df, x="Mon", y="Tues")

plt.figure()
sns.scatterplot(data=my_df, x="Mon", y="Tues", color="red", s=200)

plt.figure()
sns.scatterplot(
    data=my_df, x="Mon", y="Tues",
    hue=my_df["Mon"], palette="viridis", s=200
)

plt.figure()
sns.scatterplot(
    data=my_df, x="Mon", y="Tues",
    hue="Mon", palette="viridis",
    alpha=0.3, sizes=(20, 800),
    size=abs(my_df["Tues"])
)

# ========================== Boxplots ==============================
print("\nCreating boxplots...")

plt.figure()
sns.boxplot(data=my_df)

plt.figure()
sns.boxplot(data=my_df, palette="Set2")

plt.figure()
sns.boxplot(data=my_df, orient="h", palette="Set2")

plt.figure()
sns.boxplot(data=my_df, palette="Set2", showfliers=False)

# ========================== KDE Plots =============================
print("\nCreating KDE plots...")

plt.figure()
sns.kdeplot(data=my_df, x="Mon", fill=True)

plt.figure()
sns.kdeplot(data=my_df, x="Mon", fill=True, label="Mon")
sns.kdeplot(data=my_df, x="Thur", fill=True, label="Thur")

plt.figure()
sns.kdeplot(
    data=my_df, x="Mon", fill=True,
    label="Mon", bw_adjust=2, alpha=0.3
)

plt.figure()
sns.kdeplot(
    data=my_df, x="Mon", fill=True,
    label="Mon", bw_adjust=0.5,
    alpha=0.3, linewidth=3, color="purple"
)

# ========================== Show All Windows ======================
plt.show()

print("Lesson complete — all charts generated.")

# ========================== Teaching Notes =========================
r"""
Teaching Notes:

1. Seaborn:
   - Built on top of Matplotlib.
   - Designed for statistical visualizations.
   - Works seamlessly with Pandas DataFrames.

2. Histograms:
   - Show distribution of numeric data.
   - KDE adds a smooth curve.

3. Bar Charts:
   - Great for comparing categories.
   - Can customize palettes, orientation, and transparency.

4. Line Charts:
   - Show trends over time or index.
   - Markers and transparency improve readability.

5. Scatterplots:
   - Show relationships between two numeric variables.
   - Hue and size add extra dimensions.

6. Boxplots:
   - Show spread, median, and outliers.
   - Horizontal orientation improves readability.

7. KDE Plots:
   - Smooth distribution curves.
   - Bandwidth controls smoothness.
"""

# ========================== Examples ===============================
r"""
Examples:

sns.histplot(data=df, x="Age", bins=20, kde=True)
sns.barplot(x=df["Category"], y=df["Value"])
sns.lineplot(data=df, x=df.index, y="Sales")
sns.scatterplot(data=df, x="Height", y="Weight", hue="Gender")
sns.boxplot(data=df, palette="coolwarm")
sns.kdeplot(data=df, x="Income", fill=True)
"""

# ====================== Common Mistakes ============================
r"""
Common Mistakes:

- Forgetting that Seaborn expects tidy DataFrames.
- Using hue incorrectly (must be categorical or numeric).
- Overlapping too many KDE plots without transparency.
- Forgetting to import seaborn as sns.
"""

# ========================== Takeaways ==============================
r"""
Key Takeaways:

- Seaborn provides powerful, beautiful statistical charts.
- Customization options (palette, alpha, hue) make visuals clearer.
- KDE, boxplots, and scatterplots reveal patterns not obvious in raw data.
"""
