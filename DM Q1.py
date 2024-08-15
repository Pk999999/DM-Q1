import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('employee_dataset.csv')

# 1. Get the dimensions, structure, attribute name, and attribute values of the dataset
dimensions = df.shape
structure = df.info()
attribute_names = df.columns.tolist()
attribute_values = df.head()

# 2. Display
# (A) First 5 Records
first_5_records = df.head(5)

# (B) Last 5 Records
last_5_records = df.tail(5)

# (C) Name, Designation, Salary of First 10 records
first_10_records = df[['Name', 'Designation', 'Salary']].head(10)

# (D) Name of all records
all_names = df['Name']

# (E) All records
all_records = df

# 3. Display the following statistical measures of the dataset
# a) Mean, median and mode of the variables
mean = df.mean()
median = df.median()
mode = df.mode().iloc[0]

# b) Variance and Covariance
variance = df.var()
covariance = df.cov()

# c) Correlation of salary to experience
correlation = df['Salary'].corr(df['Experience'])

# 4. Draw the following
# (A) Pie chart on designation
designation_counts = df['Designation'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(designation_counts, labels=designation_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart of Designation')
plt.show()

# (B) Histogram of Salary
plt.figure(figsize=(10, 6))
plt.hist(df['Salary'], bins=10, edgecolor='black')
plt.title('Histogram of Salary')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# (C) Scatter plot of Salary to Experience
plt.figure(figsize=(10, 6))
plt.scatter(df['Experience'], df['Salary'])
plt.title('Scatter Plot of Salary vs Experience')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()

# Printing results
print("Dimensions:", dimensions)
print("\nStructure:")
print(structure)
print("\nAttribute Names:", attribute_names)
print("\nAttribute Values:")
print(attribute_values)
print("\nFirst 5 Records:")
print(first_5_records)
print("\nLast 5 Records:")
print(last_5_records)
print("\nName, Designation, Salary of First 10 records:")
print(first_10_records)
print("\nName of all records:")
print(all_names)
print("\nAll records:")
print(all_records)
print("\nMean of the variables:")
print(mean)
print("\nMedian of the variables:")
print(median)
print("\nMode of the variables:")
print(mode)
print("\nVariance of the variables:")
print(variance)
print("\nCovariance of the variables:")
print(covariance)
print("\nCorrelation of Salary to Experience:", correlation)
