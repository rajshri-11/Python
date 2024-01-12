import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Writing DataFrame to a CSV file
df.to_csv('example.csv', index=False)

# Reading data from a CSV file into a DataFrame
df_read = pd.read_csv('example.csv')
print("\nRead DataFrame from CSV:")
print(df_read)

# Displaying basic information about the DataFrame
print("\nDataFrame Info:")
print(df.info())

# Displaying summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Accessing columns
print("\nColumn 'Name':")
print(df['Name'])

# Selecting specific rows and columns
print("\nSubset of DataFrame:")
print(df.loc[1:2, ['Name', 'City']])

# Filtering data based on a condition
filtered_df = df[df['Age'] > 30]
print("\nFiltered DataFrame:")
print(filtered_df)

# Sorting DataFrame by a column
sorted_df = df.sort_values(by='Age', ascending=False)
print("\nSorted DataFrame:")
print(sorted_df)

# Grouping data by a column and calculating mean
grouped_df = df.groupby('City').mean()
print("\nGrouped DataFrame:")
print(grouped_df)

# Introducing missing data
df.loc[2, 'Age'] = None

# Checking for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Dropping rows with missing values
df_cleaned = df.dropna()
print("\nDataFrame after Dropping Missing Values:")
print(df_cleaned)
