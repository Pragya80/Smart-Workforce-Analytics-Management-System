from database_manager import DatabaseManager


def main():

    db = DatabaseManager()
    db.connect()
    db.create_table()

    print("Smart Workforce Analytics System Started")


if __name__ == "__main__":
    main()