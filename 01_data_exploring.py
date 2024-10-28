# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
# Load the dataset
data = pd.read_csv('drug_consumption.data', sep=',', header=None)

# Create a markdown file
with open("data_exploration_report.md", "w") as report:
    
  # Overview of Data Exploration
    report.write("## Overview of Data Exploration\n\n")
    report.write("### Dataset Overview:\n")
    report.write("- The dataset contains **1885 entries** and **32 columns**.\n")
    report.write("- The first 13 columns are **numerical** (with types int64 and float64), while columns 13 to 31 are **categorical** (type object), which seem to hold values like `CL0`, `CL1`, etc.\n")
    report.write("- No missing values were detected in the dataset, as all columns have a full count of non-null values.\n")
    report.write("- There are no duplicate rows in the dataset.\n\n")

    # Summary statistics and insights for numerical data
    report.write("### Numerical Data Insights:\n")
    report.write("- The numerical columns show a wide range of values, with some having extreme values (e.g., column 9 with a minimum value of -3.46 and a maximum of 3.46).\n")
    report.write("- The summary statistics (mean, standard deviation, min, max, etc.) provide insight into the distribution of these numerical features.\n")
    report.write("- The correlation matrix shows some moderate correlations between variables, particularly between:\n")
    report.write("  - Columns 1 and 4 (correlation = 0.354)\n")
    report.write("  - Columns 11 and 12 (correlation = 0.623)\n")
    report.write("  - Columns 8 and 12 (correlation = 0.421)\n")
    report.write("- This suggests there might be interdependencies between some of the numerical features.\n\n")

    # Summary statistics and insights for categorical data
    report.write("### Categorical Data Insights:\n")
    report.write("- Categorical columns (13 to 31) have **7 unique values** (ranging from `CL0` to `CL6`), with frequencies indicating some dominant categories like `CL0` and `CL6`.\n")
    report.write("- For example:\n")
    report.write("  - Column 13 has `CL5` as the most frequent value, with 759 occurrences.\n")
    report.write("  - Column 31 has `CL0` as the most frequent value, with 1455 occurrences.\n")
    report.write("- This could indicate a skewness in categorical variables, with some categories being much more common than others.\n\n")

    
    # Show first few rows of the data
    report.write("## First Few Rows of the Dataset\n\n")
    report.write("```plaintext\n")
    report.write(str(data.head()) + "\n")
    report.write("```\n\n")
    
    # Summary statistics for numerical columns
    report.write("## Summary Statistics for Numerical Columns\n\n")
    report.write("```plaintext\n")
    report.write(str(data.describe(include=[float, int])) + "\n")
    report.write("```\n\n")
    
    # Summary statistics for categorical columns
    report.write("## Summary Statistics for Categorical Columns\n\n")
    report.write("```plaintext\n")
    report.write(str(data.describe(include=[object])) + "\n")
    report.write("```\n\n")
    
    # Check for missing values
    report.write("## Missing Values in Each Column\n\n")
    report.write("```plaintext\n")
    report.write(str(data.isnull().sum()) + "\n")
    report.write("```\n\n")
    
    # Check for duplicate entries
    duplicate_count = data.duplicated().sum()
    report.write(f"## Number of Duplicate Rows: {duplicate_count}\n\n")
    
    # Correlation Matrix for Numerical Columns
    correlation_matrix = data.iloc[:, :13].corr()  # Correlation for numerical columns only
    report.write("## Correlation Matrix for Numerical Columns\n\n")
    report.write("```plaintext\n")
    report.write(str(correlation_matrix) + "\n")
    report.write("```\n\n")

# Updated: Visualize the distribution of numerical columns and save the figures
for col in data.columns[:13]:  # Loop through the first 13 numerical columns
    plt.figure()
    plt.hist(data[col], bins=50)
    plt.title(f'Distribution of Column {col}')
    plt.xlabel(f'Column {col}')
    plt.ylabel('Frequency')
    plt.savefig(f'distribution_column_{col}.png')  # Save the figure
    plt.close()  # Close the figure to free memory

# Updated: Correlation matrix heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Numerical Variables')
plt.savefig('correlation_matrix.png')  # Save the heatmap
plt.close()

# Updated: Bar plot for categorical columns
for col in data.columns[13:]:  # Loop through the categorical columns
    plt.figure()
    data[col].value_counts().plot(kind='bar')
    plt.title(f'Distribution of Categorical Column {col}')
    plt.xlabel(f'Column {col}')
    plt.ylabel('Count')
    plt.savefig(f'categorical_column_{col}.png')  # Save the plot
    plt.close()  # Close the figure to free memory

# Add figure references to the markdown file
with open("data_exploration_report.md", "a") as report:
    # Adding the plots for numerical columns
    report.write("## Distribution Plots for Numerical Columns\n")
    for col in data.columns[:13]:
        report.write(f"![Distribution of Column {col}](distribution_column_{col}.png)\n\n")
    
    # Adding the heatmap for correlation matrix
    report.write("## Correlation Heatmap\n")
    report.write("![Correlation Matrix](correlation_matrix.png)\n\n")
    
    # Adding the plots for categorical columns
    report.write("## Bar Plots for Categorical Columns\n")
    for col in data.columns[13:]:
        report.write(f"![Categorical Column {col}](categorical_column_{col}.png)\n\n")

print("Data exploration completed and the markdown report is saved as 'data_exploration_report.md'.")
