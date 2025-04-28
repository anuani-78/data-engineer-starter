SELECT 
    employee_id, 
    department_id, 
    salary, 
    ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) as salary_rank
FROM employees;
