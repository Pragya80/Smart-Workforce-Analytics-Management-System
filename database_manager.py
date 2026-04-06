import sqlite3


class DatabaseManager:
    def __init__(self, db_name="workforce.db"):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                emp_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL,
                age INTEGER NOT NULL,
                experience INTEGER NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    def add_employee(self, employee):
        conn = self.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO employees (emp_id, name, department, salary, age, experience)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                employee.emp_id,
                employee.name,
                employee.department,
                employee.salary,
                employee.age,
                employee.experience
            ))
            conn.commit()
        except Exception as e:
            # Handle duplicate entries gracefully
            pass
        finally:
            conn.close()

    def get_all_employees(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()

        conn.close()
        return employees

    def update_employee(self, emp_id, data):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE employees
            SET name = ?, department = ?, salary = ?, age = ?, experience = ?
            WHERE emp_id = ?
        """, (
            data["name"],
            data["department"],
            data["salary"],
            data["age"],
            data["experience"],
            emp_id
        ))

        conn.commit()
        conn.close()

    def delete_employee(self, emp_id):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM employees WHERE emp_id = ?", (emp_id,))

        conn.commit()
        conn.close()