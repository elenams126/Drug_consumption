# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ucimlrepo import fetch_ucirepo

# Fetch the dataset
drug_consumption_quantified = fetch_ucirepo(id=373)

# Data (as pandas dataframes)
X = drug_consumption_quantified.data.features
y = drug_consumption_quantified.data.targets

# Metadata
print(drug_consumption_quantified.metadata)

# Print the first and last 10 rows of the dataset
print("First 10 rows of the dataset:\n", X.head(10))
print("Last 10 rows of the dataset:\n", X.tail(10))

# Print the columns and their data types
print("Columns and their data types:\n", X.dtypes)

# Create a markdown file for data exploration report
with open("data_exploration_report.md", "w") as report:
    report.write("## Overview of Data Exploration\n\n")
    
    # Summary of the dataset
    report.write("### Dataset Overview:\n")
    report.write(f"- The dataset contains {X.shape[0]} entries and {X.shape[1]} columns.\n")
    report.write("- The columns represent demographic data, personality traits (NEO-FFI-R), impulsivity, and sensation seeking scores.\n")
    report.write("- Target columns represent the use of 18 legal and illegal drugs.\n")
    report.write("- The data appears to be clean with no missing values.\n\n")
    
    # Display column names and types
    report.write("### Columns and Their Data Types:\n")
    report.write("```plaintext\n")
    report.write(str(X.dtypes) + "\n")
    report.write("```\n\n")
    
    # Show first 10 rows of the data
    report.write("## First 10 Rows of the Dataset\n\n")
    report.write("```plaintext\n")
    report.write(str(X.head(10)) + "\n")
    report.write("```\n\n")
    
    # Show last 10 rows of the data
    report.write("## Last 10 Rows of the Dataset\n\n")
    report.write("```plaintext\n")
    report.write(str(X.tail(10)) + "\n")
    report.write("```\n\n")
    
    # Summary statistics for the numerical columns (Personality Traits and Demographics)
    report.write("## Summary Statistics for Numerical Columns\n\n")
    report.write("```plaintext\n")
    report.write(str(X.describe()) + "\n")
    report.write("```\n\n")

# Visualize some data distributions
# Plot age distribution
plt.figure(figsize=(10, 6))
sns.histplot(X['age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.savefig('age_distribution.png')
plt.close()

# Plot gender distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='gender', data=X)
plt.title('Gender Distribution')
plt.savefig('gender_distribution.png')
plt.close()

# Create histograms for the personality traits (NEO-FFI-R)
personality_columns = ['nscore', 'escore', 'oscore', 'ascore', 'cscore']
for col in personality_columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(X[col], bins=30, kde=True)
    plt.title(f'Distribution of {col.upper()}')
    plt.savefig(f'{col}_distribution.png')
    plt.close()

# Add plots to the markdown file
with open("data_exploration_report_test.md", "a") as report:
    report.write("## Age Distribution\n")
    report.write("![Age Distribution](age_distribution.png)\n\n")
    
    report.write("## Gender Distribution\n")
    report.write("![Gender Distribution](gender_distribution.png)\n\n")
    
    report.write("## Personality Trait Distributions\n")
    for col in personality_columns:
        report.write(f"![Distribution of {col.upper()}]({col}_distribution.png)\n\n")

# Summary statistics for drug consumption targets
y_summary = y.describe()
with open("data_exploration_report.md", "a") as report:
    report.write("## Summary of Drug Consumption Targets\n\n")
    report.write("```plaintext\n")
    report.write(str(y_summary) + "\n")
    report.write("```\n\n")
