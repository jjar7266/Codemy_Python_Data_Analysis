"""
Lesson 12 — Importing CSV Files into Pandas
Codemy.com — Instructor: John Elder

This lesson covers:
- Loading CSV files into a Pandas DataFrame
- Loading CSVs from your local machine
- Loading CSVs directly from a URL
- Understanding how Pandas parses CSV data
- Displaying DataFrames in VS Code vs. Colab

Notes:
- John uses Google Colab; this version is adapted for VS Code.
- VS Code does NOT auto-display DataFrames — print() is required.
- CSV files are the most common real-world data source for Pandas.
"""

# ========================== Imports ===============================
import pandas as pd
import numpy as np

# ====================== Import CSV (Local File) ====================
"""
In Colab, John uses: "/content/dog_data.csv"
In VS Code, use a path relative to your project folder.

Place dog_data.csv in the same folder as this script.
Then use: pd.read_csv("dog_data.csv")
"""

print("Loading local CSV file:")
my_df = pd.read_csv("dog_data.csv")
print(my_df)

# ====================== Import CSV (From URL) ======================
"""
Pandas can load CSVs directly from a URL.
This is extremely useful for:
- Public datasets
- GitHub raw CSVs
- Online APIs that return CSV data
"""

print("\nLoading CSV from URL:")
url = "https://raw.githubusercontent.com/flatplanet/Data_Analysis_With_Python_Course/main/dog_data.csv"
my_df2 = pd.read_csv(url)
print(my_df2)

# ========================== Teaching Notes =========================
"""
Teaching Notes:

1. pd.read_csv() is the most important Pandas function.
   It loads data into a DataFrame and automatically detects headers,
   columns, and data types.

2. File paths:
   - In Colab: /content/filename.csv
   - In VS Code: use relative paths like "dog_data.csv"
   - On Windows, forward slashes work perfectly:
       "C:/data/file.csv"

3. URLs:
   Pandas can read CSVs directly from HTTP/HTTPS.

4. DataFrame display:
   - Colab auto-displays DataFrames.
   - VS Code requires print(df).

5. After loading:
   - df.head() shows the first 5 rows.
   - df.info() shows column types.
   - df.describe() shows statistics.
"""

# ========================== Examples ===============================
"""
Examples:

df = pd.read_csv("sales.csv")
df = pd.read_csv("data/myfile.csv")
df = pd.read_csv("https://example.com/data.csv")

df.head()      → first 5 rows
df.tail()      → last 5 rows
df.columns     → list of column names
df.shape       → (rows, columns)
"""

# ====================== Common Mistakes ============================
"""
Common Mistakes:

- Using Colab paths in VS Code:
    pd.read_csv("/content/file.csv") → FileNotFoundError

- Forgetting print() in VS Code:
    df   # does nothing

- Wrong file location:
    CSV must be in the same folder OR you must specify the correct path.

- Using Windows backslashes without escaping:
    "C:\data\file.csv"  → WARNING / incorrect
    Correct forms:
        "C:/data/file.csv"
        "C:\\data\\file.csv"
        r"C:\data\file.csv"
"""

# ========================== Takeaways ==============================
"""
Key Takeaways:

- pd.read_csv() is the gateway to real-world data analysis.
- Local CSVs require correct file paths.
- Pandas can load CSVs directly from URLs.
- VS Code requires print() to display DataFrames.
- Once loaded, DataFrames can be filtered, cleaned, and analyzed.
"""
