# Import necessary libraries
import pandas as pd

# Load the raw dataset
data = pd.read_csv('drug_consumption.data', sep=',', header=None)

# Define column names (adding 'UnknownColumn' for the extra column)
columns = [
    'ID', 'Age', 'Gender', 'Education', 'Country', 'Ethnicity',
    'Nscore', 'Escore', 'Oscore', 'Ascore', 'Cscore', 'Impulsiveness', 'SS',
    'Alcohol', 'Amphetamines', 'Amyl_nitrite', 'Benzodiazepines', 'Cannabis',
    'Chocolate', 'Cocaine', 'Caffeine', 'Crack', 'Ecstasy', 'Heroin',
    'Ketamine', 'Legal_highs', 'LSD', 'Methadone', 'MMushrooms', 'Nicotine', 'VSA',
    'UnknownColumn'  # Adding the missing column name
]

# Assign the new column names
data.columns = columns

# Step 1: Handle Missing Values and Invalid Data
# Assuming there should be no missing values based on the paper
data.fillna(method='ffill', inplace=True)

# Step 2: Encode categorical variables (e.g., Gender, Education, Drug Use)
# Gender: 1 = Male, 0 = Female
data['Gender'] = data['Gender'].replace({1: 'Male', 0: 'Female'})

# Education levels (0–4 corresponding to certain levels)
education_levels = {0: 'Left school before 16', 1: 'Left school at 16', 2: 'Left school at 17', 
                    3: 'Left school at 18', 4: 'Some College/University', 5: 'Professional degree'}
data['Education'] = data['Education'].map(education_levels)

# Convert drug use columns (e.g., Alcohol, Cannabis, etc.) to binary (user vs non-user)
for col in data.columns[13:]:
    data[col] = data[col].apply(lambda x: 1 if x != 'CL0' else 0)  # 1 for user, 0 for non-user

# Step 3: Save the cleaned dataset
data.to_csv('cleaned_drug_consumption_v2.csv', index=False)
print("Data cleaning completed and saved as 'cleaned_drug_consumption_v2.csv'")

# Overview of data clean:

#No Missing Values:

# There are no missing values in any of the columns, as confirmed by the count of non-null values for each column.

#Numerical Columns:

# Columns 0 to 12 are numerical, and they appear to have been standardized (mean-centered and scaled) based on the transformed values (e.g., some values are now between -1 and 2).

# Categorical Columns:

# Columns 13 to 31 are properly typed as object, and contain categorical values like CL0, CL1, etc., which match the structure identified during the data exploration.