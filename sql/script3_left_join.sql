SELECT e.first_name, s.salary
FROM employees e
LEFT JOIN salaries s
ON e.employee_id = s.employee_id
WHERE s.salary > 80000;
