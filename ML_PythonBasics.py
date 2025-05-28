import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'student_data.csv')

#Task1
print(df.head(5))  # Display the first few rows of the DataFrame
print(df.describe())  # Display summary statistics of the DataFrame
print(df.isnull().sum())  # Check for missing values in each column

if df.isnull().sum().sum() > 0:
    print("\nPopulating missing values with column means...")
    df_filled = df.fillna(df.mean())
    print("Missing values after population:")
    print(df_filled.isnull().sum())
    df = df_filled
else:
    print("No incomplete values found in the data.")

#Task2
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Student Data Analysis - Visualizations', fontsize=16, fontweight='bold')

# 1. Scatter plot: Study_Hours vs Exam_Score
axes[0, 0].scatter(df['Study_Hours'], df['Exam_Score'], alpha=0.6, color='blue', s=50)
axes[0, 0].set_xlabel('Study Hours')
axes[0, 0].set_ylabel('Exam Score')
axes[0, 0].set_title('Relationship between Study Hours and Exam Score')
axes[0, 0].grid(True, alpha=0.3)

# 2. Histogram of Exam_Score distribution
axes[0, 1].hist(df['Exam_Score'], bins=20, alpha=0.7, color='green', edgecolor='black')
axes[0, 1].set_xlabel('Exam Score')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('Distribution of Exam Scores')
axes[0, 1].grid(True, alpha=0.3)

# 3. Box plot of Sleep_Hours
axes[1, 0].boxplot(df['Sleep_Hours'])
axes[1, 0].set_ylabel('Sleep Hours')
axes[1, 0].set_title('Distribution of Sleep Hours')
axes[1, 0].grid(True, alpha=0.3)

