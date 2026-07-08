# ================================
# TASK 2 - EXPLORATORY DATA ANALYSIS (EDA)
# CodeAlpha Internship
# ================================

import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

# Upload Dataset
uploaded = files.upload()

# Read Dataset
df = pd.read_csv("sales.csv")

print("="*50)
print("DATASET")
print("="*50)
print(df)

print("\n" + "="*50)
print("FIRST 5 ROWS")
print("="*50)
print(df.head())

print("\n" + "="*50)
print("LAST 5 ROWS")
print("="*50)
print(df.tail())

print("\n" + "="*50)
print("DATASET SHAPE")
print("="*50)
print(df.shape)

print("\n" + "="*50)
print("COLUMN NAMES")
print("="*50)
print(df.columns.tolist())

print("\n" + "="*50)
print("DATA TYPES")
print("="*50)
print(df.dtypes)

print("\n" + "="*50)
print("DATASET INFORMATION")
print("="*50)
df.info()

print("\n" + "="*50)
print("SUMMARY STATISTICS")
print("="*50)
print(df.describe())

print("\n" + "="*50)
print("MISSING VALUES")
print("="*50)
print(df.isnull().sum())

print("\n" + "="*50)
print("DUPLICATE ROWS")
print("="*50)
print(df.duplicated().sum())

print("\n" + "="*50)
print("UNIQUE PRODUCTS")
print("="*50)
print(df["Product"].unique())

print("\n" + "="*50)
print("UNIQUE CATEGORIES")
print("="*50)
print(df["Category"].unique())

print("\n" + "="*50)
print("CORRELATION")
print("="*50)
print(df.corr(numeric_only=True))

# ----------------------------
# Visualization 1 - Bar Chart
# ----------------------------
plt.figure(figsize=(7,5))
plt.bar(df["Product"], df["Quantity"])
plt.title("Product vs Quantity")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.grid(True)
plt.show()

# ----------------------------
# Visualization 2 - Histogram
# ----------------------------
plt.figure(figsize=(7,5))
plt.hist(df["Price"], bins=5)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# ----------------------------
# Visualization 3 - Pie Chart
# ----------------------------
category = df.groupby("Category")["Quantity"].sum()

plt.figure(figsize=(6,6))
plt.pie(category, labels=category.index, autopct="%1.1f%%", startangle=90)
plt.title("Category-wise Quantity")
plt.show()

print("\n" + "="*50)
print("CONCLUSION")
print("="*50)
print("""
1. Dataset loaded successfully.
2. Dataset information and statistics generated.
3. Missing values and duplicate rows checked.
4. Product and category details explored.
5. Correlation between numerical columns calculated.
6. Bar chart, Histogram, and Pie chart created.
7. Dataset is ready for further analysis.
""")
