# pyright: reportGeneralTypeIssues=false
r"""
Lesson 19 — Intro to SciKit-Learn (Decision Trees & Classification)
Codemy.com — Instructor: John Elder

This lesson covers:
- Using SciKit-Learn for basic machine learning
- Preparing data for classification
- Encoding categorical variables
- Splitting data into training/testing sets
- Training a Decision Tree model
- Making predictions and evaluating accuracy

Notes:
- Adapted for VS Code (print() required for output)
- Uses local dog_data.csv from your GitHub repo
"""

# ========================== Imports ===============================
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# ========================== Load Data =============================
print("🐕 Dog Data Overview")
print("=" * 50)

df = pd.read_csv("dog_data.csv")

print(f"\nTotal number of dogs: {len(df)}")
print(f"\nColumns in our data: {list(df.columns)}")

print("\nFirst few rows:")
print(df.head())

print("\n📊 Data Summary:")
print(f"Number of different breeds: {df['Breed'].nunique()}")
print(f"Number of different colors: {df['Color'].nunique()}")
print(f"Number of different zip codes: {df['OwnerZip'].nunique()}")

# ========================== ML Question ===========================
r"""
QUESTION:
Can we predict a dog's breed based only on the owner's zip code?

This is a CLASSIFICATION problem — predicting categories.
"""

print("\n" + "=" * 50)
print("🤖 BUILDING OUR FIRST MODEL")
print("=" * 50)

# ====================== Step 1: Prepare Data ======================
print("\n📋 Step 1: Preparing the data...")

# Focus on the top 10 most common breeds
top_breeds = df["Breed"].value_counts().head(10).index
df_filtered = df[df["Breed"].isin(top_breeds)].copy()

print(f"We're focusing on these {len(top_breeds)} popular breeds:")
for i, breed in enumerate(top_breeds, 1):
    count = len(df_filtered[df_filtered["Breed"] == breed])
    print(f"  {i}. {breed}: {count} dogs")

# ====================== Step 2: Encode Data =======================
print("\n🔢 Step 2: Converting text to numbers...")
print("(Machine learning models need numbers, not words!)")

breed_encoder = LabelEncoder()
df_filtered["BreedEncoded"] = breed_encoder.fit_transform(df_filtered["Breed"])  # type: ignore

X = df_filtered[["OwnerZip"]].values   # Feature
y = df_filtered["BreedEncoded"].values # Target

print(f"✓ Converted {len(breed_encoder.classes_)} breeds to numbers")

# ====================== Step 3: Train/Test Split ==================
print("\n✂️ Step 3: Splitting data...")
print("We'll use 80% for training and 20% for testing")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"✓ Training set: {len(X_train)} dogs")
print(f"✓ Testing set: {len(X_test)} dogs")

# ====================== Step 4: Train Model =======================
print("\n🌳 Step 4: Training our Decision Tree model...")
print("(This is where the magic happens!)")

model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

print("✓ Model trained successfully!")

# ====================== Step 5: Predictions ========================
print("\n🔮 Step 5: Making predictions...")

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\n📊 MODEL PERFORMANCE")
print(f"Accuracy: {accuracy:.2%}")
print("\nWhat does this mean?")
print(f"Our model correctly predicted the breed {accuracy:.2%} of the time")
print("based only on the owner's zip code!")

# ====================== Step 6: Example Predictions ===============
print("\n" + "=" * 50)
print("🎯 EXAMPLE PREDICTIONS")
print("=" * 50)

sample_indices = np.random.choice(len(X_test), 10, replace=False)

for idx in sample_indices:
    actual_breed = breed_encoder.inverse_transform([y_test[idx]])[0]
    predicted_breed = breed_encoder.inverse_transform([y_pred[idx]])[0]
    zip_code = X_test[idx][0]

    match = "✓" if actual_breed == predicted_breed else "✗"
    print(f"\n{match} Zip Code: {zip_code}")
    print(f"   Actual breed: {actual_breed}")
    print(f"   Predicted breed: {predicted_breed}")

# ========================== Teaching Notes =========================
r"""
Teaching Notes:

1. Machine Learning Workflow:
   - Clean data
   - Encode categories
   - Split into training/testing sets
   - Train a model
   - Evaluate accuracy

2. Decision Trees:
   - Easy to understand
   - Good for small datasets
   - Can overfit without depth limits

3. Label Encoding:
   - Converts text labels into integers
   - Required for most ML algorithms

4. Accuracy:
   - Percentage of correct predictions
   - Depends heavily on data quality
"""

# ========================== Examples ===============================
r"""
Examples:

# Encode categories
encoder = LabelEncoder()
df["Encoded"] = encoder.fit_transform(df["Category"])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict
model.predict([[33065]])
"""

# ====================== Common Mistakes ============================
r"""
Common Mistakes:

- Forgetting to encode text before training
- Using too many rare categories (model can't learn patterns)
- Not splitting data (training on everything gives misleading accuracy)
- Assuming high accuracy means a good model (depends on context)
"""

# ========================== Takeaways ==============================
r"""
Key Takeaways:

- SciKit-Learn makes machine learning accessible and structured.
- Decision Trees are great beginner models.
- Encoding and splitting data are essential steps.
- Accuracy helps evaluate model performance.
"""
