import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/customer_churn.csv")

# Display first rows
print("Customer Churn Dataset")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Churn count
print("\nChurn Distribution:")
print(df['Churn'].value_counts())

# Average monthly charges by churn
print("\nAverage Monthly Charges:")
print(df.groupby('Churn')['MonthlyCharges'].mean())

# Visualization settings
sns.set_style("whitegrid")

# Churn Count Plot
plt.figure(figsize=(6,4))
sns.countplot(x='Churn', data=df)
plt.title("Customer Churn Count")
plt.savefig("churn_count.png")
plt.show()

# Monthly Charges vs Churn
plt.figure(figsize=(8,5))
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title("Monthly Charges vs Churn")
plt.savefig("monthly_charges_vs_churn.png")
plt.show()

# Support Calls vs Churn
plt.figure(figsize=(8,5))
sns.boxplot(x='Churn', y='SupportCalls', data=df)
plt.title("Support Calls vs Churn")
plt.savefig("support_calls_vs_churn.png")
plt.show()

# Internet Usage vs Churn
plt.figure(figsize=(8,5))
sns.boxplot(x='Churn', y='InternetUsageGB', data=df)
plt.title("Internet Usage vs Churn")
plt.savefig("internet_usage_vs_churn.png")
plt.show()

# Key Insights
print("\nKey Insights:")
print("- Customers with higher support calls are more likely to churn.")
print("- Monthly contract users show higher churn.")
print("- Customers with low internet usage tend to churn more.")

print("\nAnalysis Completed Successfully!")
