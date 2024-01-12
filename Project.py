import pandas as pd
 # Load the data from the CSV file
df = pd.read_csv("jobs_in_data.csv")
 # Display the first few rows of the dataframe to inspect the data
print(df.head())
 # Summary statistics for numerical columns
print(df.describe())
 # Count the number of missing values in each column
print(df.isnull().sum())
# Group by job_category and calculate the average salary
average_salary_by_category = df.groupby('job_category')['salary_in_usd'].mean()
print(average_salary_by_category)
# Group by experience_level and calculate the median salary
median_salary_by_experience = df.groupby('experience_level')['salary_in_usd'].median()
print(median_salary_by_experience)
 # Count the number of occurrences of each job title
job_title_counts = df['job_title'].value_counts()
print(job_title_counts)
# Plotting examples
import matplotlib.pyplot as plt
 # Histogram of salary distribution
df['salary_in_usd'].plot(kind='hist', bins=20, title='Salary Distribution')
plt.show()
 # Bar chart of average salary by job category
average_salary_by_category.plot(kind='bar', title='Average Salary by Job Category')
plt.show()
