from database_manager import DatabaseManager
from employee import Employee


def main():

    db = DatabaseManager()
    print("System started successfully")
    db.connect()
    db.create_table()
    db.add_employee(Employee(1, "Alice", "HR", 60000, 30, 5))
    db.add_employee(Employee(2, "Bob", "Engineering", 80000, 28, 3))
    employees = db.get_all_employees()
    for emp in employees:
        print(emp)
    gi

    print("Smart Workforce Analytics System Started")


if __name__ == "__main__":
    main()