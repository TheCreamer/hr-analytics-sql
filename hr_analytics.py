import sqlite3
import pandas as pd

#This loads the CSV file into a dataframe called df
df = pd.read_csv(r'WA_Fn-UseC_-HR-Employee-Attrition.csv')

conn = sqlite3.connect('hr_analytics.db')
df.to_sql('employees', conn, if_exists='replace', index=False)
print("Database created successfully!")

cursor = conn.cursor()
#This shows the count of the total count of Employees in each Department
query = """
SELECT Department, COUNT(*) as TotalEmployees
FROM employees
GROUP BY Department
"""

results = cursor.execute(query).fetchall()
#This Query shows the Attrition by Department 
query3 = """
SELECT 
    Department,
    COUNT(*) as TotalEmployees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Attrition_Count,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as Attrition_Rate
FROM employees
GROUP BY Department
ORDER BY Attrition_Rate DESC
"""
# Executes query number 3
results3 = cursor.execute(query3).fetchall()

# Prints results for query number 3
for row in results3:
    print(row)

#This query shows the Average Tenure at the Company with the Income in mind
query4= """
SELECT 
    Department,
    ROUND(AVG(YearsAtCompany), 2) as Avg_Tenure,
    ROUND(AVG(MonthlyIncome), 2) as Avg_Salary
FROM employees
GROUP BY Department 
ORDER BY Avg_Tenure DESC
"""


results4 = cursor.execute(query4).fetchall()

# Prints results for query number 4
print("\nAverage Tenure and Salary by Department:")
for row in results4:
    print(row)

#This shows the Overtime vs Attrition in the Company
query5 = """
SELECT
    OverTime,
    COUNT(*) as TotalEmployees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Attrition_Count,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)* 100.0 / COUNT(*), 2)
FROM employees
GROUP BY OverTime
ORDER BY 4 DESC 
""" #Attrition Rate column Number is 4

results5 = cursor.execute(query5).fetchall()

print("\nOvertime vss Attrition")
for row in results5:
    print(row)

query6 = """ 
SELECT 
    CASE
        WHEN Age < 25 THEN 'Under 25'
        WHEN Age BETWEEN 25 and 34 THEN '25-34'
        WHEN Age BETWEEN 35 and 44 THEN '35-44'
        WHEN AGE BETWEEN 45 and 54 THEN '45-55'
        ELSE '55+'
    END as Age_Group,
    COUNT(*) as TotalEmployees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Attrition_Count,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2)
FROM employees
GROUP BY Age_Group
ORDER BY 4 DESC
"""
results6 = cursor.execute(query6).fetchall()

print("\nAttrition by Age Group")
for row in results6:
    print(row)

query7 = """ \
SELECT 
    JobRole,
    COUNT(*) as TotalEmployees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Attrition_Count,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2)
FROM employees
GROUP BY JobRole
ORDER BY 4 DESC
LIMIT 5
"""
results7 = cursor.execute(query7).fetchall()
print("\nTop 5 Job Roles by Attrition Rate:")
for row in results7:
    print(row)