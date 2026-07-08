# ======================================
# TASK 3 - DATA VISUALIZATION
# CodeAlpha Internship
# ======================================

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
print(df.head())

# --------------------------------------
# Chart 1 - Bar Chart
# --------------------------------------
plt.figure(figsize=(8,5))
plt.bar(df["Product"], df["Quantity"])
plt.title("Product vs Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# --------------------------------------
# Chart 2 - Line Chart
# --------------------------------------
plt.figure(figsize=(8,5))
plt.plot(df["Product"], df["Price"], marker='o')
plt.title("Product vs Price")
plt.xlabel("Product")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# --------------------------------------
# Chart 3 - Pie Chart
# --------------------------------------
category = df.groupby("Category")["Quantity"].sum()

plt.figure(figsize=(6,6))
plt.pie(category,
        labels=category.index,
        autopct="%1.1f%%",
        startangle=90)
plt.title("Category-wise Quantity")
plt.show()

# --------------------------------------
# Chart 4 - Histogram
# --------------------------------------
plt.figure(figsize=(7,5))
plt.hist(df["Price"], bins=5)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# --------------------------------------
# Chart 5 - Scatter Plot
# --------------------------------------
plt.figure(figsize=(7,5))
plt.scatter(df["Price"], df["Quantity"])
plt.title("Price vs Quantity")
plt.xlabel("Price")
plt.ylabel("Quantity")
plt.grid(True)
plt.show()

print("\n" + "="*50)
print("CONCLUSION")
print("="*50)
print("""
1. Five different charts were created.
2. Bar chart shows quantity sold for each product.
3. Line chart compares product prices.
4. Pie chart shows category-wise quantity distribution.
5. Histogram shows price distribution.
6. Scatter plot shows the relationship between price and quantity.
""")
