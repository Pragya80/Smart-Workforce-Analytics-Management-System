from database_manager import DatabaseManager
from analytics_engine import AnalyticsEngine


def main():
    """
    Main entry point for Smart Workforce Analytics System.
    Demonstrates functionality of Analytics Engine for Pandas-based analysis.
    """

    # Initialize database
    db = DatabaseManager()
    db.connect()
    db.create_table()

    print("=" * 70)
    print("🚀 SMART WORKFORCE ANALYTICS SYSTEM - PANDAS ANALYSIS MODULE")
    print("=" * 70)

    # Initialize Analytics Engine
    analytics = AnalyticsEngine('workforce.db')
    
    # Load employee data from database
    print("\n⏳ Loading employee data from database...")
    df = analytics.load_employee_data_from_db()
    
    if df is None or df.empty:
        print("❌ Failed to load data. Please ensure database has employee records.")
        return

    # Display basic data information
    analytics.display_data_info()

    # ==================== DEPARTMENT-WISE ANALYSIS ====================
    print("\n" + "=" * 70)
    print("SECTION 1: DEPARTMENT-WISE ANALYSIS")
    print("=" * 70)
    
    analytics.analyze_by_department()
    analytics.department_salary_statistics()
    analytics.salary_by_department_summary()

    # ==================== FILTERING OPERATIONS ====================
    print("\n" + "=" * 70)
    print("SECTION 2: FILTERING OPERATIONS")
    print("=" * 70)
    
    # Filter by salary range
    analytics.filter_by_salary_range(min_salary=40000, max_salary=80000)
    
    # Filter by department (Example: IT)
    analytics.filter_by_department('IT')
    
    # Filter by experience
    analytics.filter_by_experience(min_experience=3)
    
    # Filter by salary threshold
    analytics.filter_by_salary_above(salary_threshold=75000)

    # ==================== SORTING OPERATIONS ====================
    print("\n" + "=" * 70)
    print("SECTION 3: SORTING OPERATIONS")
    print("=" * 70)
    
    analytics.sort_by_salary(ascending=False)  # Highest salaries first
    analytics.sort_by_experience(ascending=False)  # Most experienced first
    analytics.sort_by_name()  # Alphabetical order
    analytics.sort_by_age(ascending=True)  # Youngest first

    # ==================== GROUPING & AGGREGATION ====================
    print("\n" + "=" * 70)
    print("SECTION 4: GROUPING & AGGREGATION")
    print("=" * 70)
    
    analytics.group_salary_by_department()
    analytics.group_by_department_and_experience()
    analytics.salary_distribution_by_age_group(bin_size=10)

    # ==================== ADVANCED ANALYSIS WITH NUMPY ====================
    print("\n" + "=" * 70)
    print("SECTION 5: ADVANCED ANALYSIS (NumPy Integration)")
    print("=" * 70)
    
    analytics.correlation_analysis()
    analytics.salary_percentile_analysis(percentiles=[25, 50, 75, 90, 95])
    analytics.performance_metrics()
    analytics.salary_normalization()

    print("\n" + "=" * 70)
    print("✅ ANALYSIS COMPLETE - All Pandas operations executed successfully")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()