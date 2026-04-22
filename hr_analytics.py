import sqlite3
import pandas as pd
import queries
import visualizations
# Load CSV into dataframe
df = pd.read_csv(r'WA_Fn-UseC_-HR-Employee-Attrition.csv')

# Connect to database and load data
conn = sqlite3.connect('hr_analytics.db')
df.to_sql('employees', conn, if_exists='replace', index=False)
print("Database created successfully!")

cursor = conn.cursor()

# Attrition by Department
print("\nAttrition by Department:")
for row in cursor.execute(queries.ATTRITION_BY_DEPARTMENT).fetchall():
    print(row)

# Tenure and Salary by Department
print("\nAverage Tenure and Salary by Department:")
for row in cursor.execute(queries.TENURE_AND_SALARY).fetchall():
    print(row)

# Overtime vs Attrition
print("\nOvertime vs Attrition:")
for row in cursor.execute(queries.OVERTIME_VS_ATTRITION).fetchall():
    print(row)

# Attrition by Age Group
print("\nAttrition by Age Group:")
for row in cursor.execute(queries.ATTRITION_BY_AGE).fetchall():
    print(row)

# Top 5 Job Roles by Attrition
print("\nTop 5 Job Roles by Attrition Rate:")
for row in cursor.execute(queries.TOP_ROLES_BY_ATTRITION).fetchall():
    print(row)

# Employee Risk Scores
print("\nTop 10 High Flight Risk Employees:")
for row in cursor.execute(queries.RISK_SCORE).fetchall():
    print(row)

dept_data = cursor.execute(queries.ATTRITION_BY_DEPARTMENT).fetchall()
overtime_data = cursor.execute(queries.OVERTIME_VS_ATTRITION).fetchall()
age_data = cursor.execute(queries.ATTRITION_BY_AGE).fetchall()
roles_data = cursor.execute(queries.TOP_ROLES_BY_ATTRITION).fetchall()

visualizations.plot_attrition_by_department(dept_data)
visualizations.plot_overtime_attrition(overtime_data)
visualizations.plot_attrition_by_age(age_data)
visualizations.plot_top_roles(roles_data)