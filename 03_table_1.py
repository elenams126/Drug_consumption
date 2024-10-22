# Import necessary libraries
import pandas as pd

# Load the cleaned dataset
data = pd.read_csv('cleaned_drug_consumption_v2.csv')

# Step 1: Generate summary statistics for demographic columns
demographic_stats = {
    'n': [len(data)],
    'Gender (Male)': [data['Gender'].value_counts().get('Male', 0)],
    'Gender (Female)': [data['Gender'].value_counts().get('Female', 0)],
    'Age (mean (sd))': [f"{data['Age'].mean():.2f} ({data['Age'].std():.2f})"],
    'Education (High)': [len(data[data['Education'] == 'Professional degree'])],
    'Education (Medium)': [len(data[data['Education'] == 'Some College/University'])],
    'Education (Low)': [len(data[data['Education'].isin(['Left school at 16', 'Left school at 17', 'Left school at 18'])])]
}

# Convert the dictionary into a DataFrame
demographic_table = pd.DataFrame(demographic_stats)

# Step 2: Write the Table 1 to an HTML file
html_content = f"""
<html>
<head>
    <title>Table 1: Demographic Breakdown and Descriptive Statistics</title>
    <style>
        table {{
            width: 80%;
            margin: 20px auto;
            border-collapse: collapse;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
        }}
        th {{
            background-color: #f2f2f2;
            text-align: center;
        }}
        td {{
            text-align: center;
        }}
        h1 {{
            text-align: center;
        }}
    </style>
</head>
<body>
    <h1>Table 1: Demographic Breakdown and Descriptive Statistics</h1>
    {demographic_table.to_html(classes='table', justify='center')}
</body>
</html>
"""

# Save the HTML content to a file
with open('table_1_demographics.html', 'w') as file:
    file.write(html_content)

print("Table 1 has been generated and saved as 'table_1_demographics.html'")
