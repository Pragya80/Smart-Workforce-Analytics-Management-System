from database_manager import DatabaseManager
from analytics_engine import AnalyticsEngine
from report_generator import ReportGenerator


def main():

    print("Smart Workforce Analytics System Starting...")

    db = DatabaseManager()
    db.connect()
    db.create_table()

    analytics = AnalyticsEngine()
    report = ReportGenerator()

    print("System Ready")


if __name__ == "__main__":
    main()