# This file contains all SQL queries for the HR Analytics project

ATTRITION_BY_DEPARTMENT = """
SELECT 
    Department,
    COUNT(*) as TotalEmployees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Attrition_Count,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as Attrition_Rate
FROM employees
GROUP BY Department
ORDER BY 4 DESC
"""

TENURE_AND_SALARY = """
SELECT 
    Department,
    ROUND(AVG(YearsAtCompany), 2) as Avg_Tenure,
    ROUND(AVG(MonthlyIncome), 2) as Avg_Salary
FROM employees
GROUP BY Department
ORDER BY Avg_Tenure DESC
"""

OVERTIME_VS_ATTRITION = """
SELECT 
    OverTime,
    COUNT(*) as TotalEmployees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Attrition_Count,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as Attrition_Rate
FROM employees
GROUP BY OverTime
ORDER BY 4 DESC
"""

ATTRITION_BY_AGE = """
SELECT 
    CASE
        WHEN Age < 25 THEN 'Under 25'
        WHEN Age BETWEEN 25 AND 34 THEN '25-34'
        WHEN Age BETWEEN 35 AND 44 THEN '35-44'
        WHEN Age BETWEEN 45 AND 54 THEN '45-54'
        ELSE '55+'
    END as Age_Group,
    COUNT(*) as TotalEmployees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Attrition_Count,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as Attrition_Rate
FROM employees
GROUP BY Age_Group
ORDER BY 4 DESC
"""

TOP_ROLES_BY_ATTRITION = """
SELECT 
    JobRole,
    COUNT(*) as TotalEmployees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Attrition_Count,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as Attrition_Rate
FROM employees
GROUP BY JobRole
ORDER BY 4 DESC
LIMIT 5
"""

RISK_SCORE = """
SELECT 
    EmployeeNumber,
    JobRole,
    Department,
    Age,
    MonthlyIncome,
    OverTime,
    YearsAtCompany,
    (
        CASE WHEN OverTime = 'Yes' THEN 3 ELSE 0 END +
        CASE WHEN Age < 25 THEN 3 ELSE 0 END +
        CASE WHEN YearsAtCompany < 2 THEN 2 ELSE 0 END +
        CASE WHEN MonthlyIncome < 3000 THEN 2 ELSE 0 END
    ) as Risk_Score
FROM employees
WHERE Attrition = 'No'
ORDER BY Risk_Score DESC
LIMIT 10
"""