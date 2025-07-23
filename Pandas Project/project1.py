# Superstore Sales Analysis Using Pandas

import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\Karan Sahu\Desktop\Projects-2025\Pandas_Project\Superstore.csv", encoding='latin1')

# Display first few rows
print("\n--- First 5 rows ---")
print(df.head())

# Basic Info
print("\n--- Info ---")
print(df.info())

# Missing Values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Convert 'Order Date' and 'Ship Date' to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Extract month and year
df['Order Month'] = df['Order Date'].dt.month
df['Order Year'] = df['Order Date'].dt.year

# Create profit margin column
df['Profit Margin'] = df['Profit'] / df['Sales']

# Top Product Categories by Profit
print("\n--- Top Categories by Profit ---")
print(df.groupby('Category')['Profit'].sum().sort_values(ascending=False))

# Underperforming States
print("\n--- States with Negative Profit ---")
print(df.groupby('State')['Profit'].sum().sort_values().head(10))

# Correlation between Discount and Profit
print("\n--- Correlation: Discount vs Profit ---")
print(df[['Discount', 'Profit']].corr())

# Sub-categories with Loss
print("\n--- Sub-Categories with Overall Loss ---")
print(df.groupby('Sub-Category')['Profit'].sum().sort_values().head(5))

# Top Customers by Revenue
print("\n--- Top Customers by Sales ---")
print(df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10))

# Most Sold Products
print("\n--- Most Sold Products ---")
print(df['Product Name'].value_counts().head(10))

# Monthly Sales Trend
df['Order_Month_Year'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Order_Month_Year')['Sales'].sum()
print("\n--- Monthly Sales ---")
print(monthly_sales.tail(12))

# Shipping Delays - Difference in Days
df['Shipping Delay'] = (df['Ship Date'] - df['Order Date']).dt.days
print("\n--- Average Shipping Delay by Ship Mode ---")
print(df.groupby('Ship Mode')['Shipping Delay'].mean())

# Export Cleaned Data
df.to_csv("Superstore_Cleaned.csv", index=False)

print("\nProject Completed. Cleaned file saved as 'Superstore_Cleaned.csv'")
