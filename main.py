from database_manager import DatabaseManager
from employee import Employee


def main():

    db = DatabaseManager()
    print("System started successfully")
    db.connect()
    db.create_table()

    print("Smart Workforce Analytics System Started")


if __name__ == "__main__":
    main()