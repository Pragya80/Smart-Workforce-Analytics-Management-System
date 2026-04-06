from database_manager import DatabaseManager
from analytics_engine import AnalyticsEngine
from report_generator import ReportGenerator


def main():

    print("Smart Workforce Analytics System Starting...")

    try:
        # Initialize database
        db = DatabaseManager()

        if hasattr(db, "connect"):
            db.connect()

        if hasattr(db, "create_table"):
            db.create_table()

        # Initialize analytics module
        analytics = AnalyticsEngine()

        # Initialize report module
        report = ReportGenerator()

        print("System Ready")

    except Exception as e:
        print("System Error:", e)


if __name__ == "__main__":
    main()