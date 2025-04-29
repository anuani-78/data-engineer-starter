import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="data_engineer_practice",
    user="postgres",
    password="your_password_here"
)

cur = conn.cursor()

cur.execute("""
    INSERT INTO employees (employee_id, first_name, last_name, department_id) VALUES
    (5, 'Charlie', 'Delta', 102),
    (6, 'Samantha', 'Gamma', 103),
    (7, 'Harry', 'Beta', 101),
    (8, 'Laura', 'Theta', 101),
    (9, 'Ken', 'Alpha', 102);
""")

conn.commit()
cur.close()
conn.close()

print("Records inserted successfully.")
