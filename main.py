import pandas as pd
from database_manager import DatabaseManager
from analytics_engine import AnalyticsEngine
from report_generator import ReportGenerator
from employee import Employee


def populate_sample_data(db):
    """Populate database with sample employee data"""
    sample_employees = [
        Employee(1, "Harsh Verma", "IT", 75000, 23, 2),
        Employee(2, "Priya Singh", "IT", 80000, 28, 5),
        Employee(3, "Rajesh Kumar", "IT", 95000, 35, 10),
        Employee(4, "Anjali Sharma", "HR", 65000, 26, 3),
        Employee(5, "Vikram Patel", "HR", 62000, 24, 2),
        Employee(6, "Deepak Sharma", "Finance", 85000, 32, 8),
        Employee(7, "Neha Gupta", "Finance", 78000, 29, 6),
        Employee(8, "Arjun Mishra", "Finance", 72000, 27, 4),
        Employee(9, "Sneha Joshi", "Marketing", 68000, 25, 3),
        Employee(10, "Karan Singh", "Marketing", 71000, 28, 5),
        Employee(11, "Zara Khan", "Operations", 70000, 30, 7),
        Employee(12, "Rohan Desai", "Operations", 65000, 26, 4),
        Employee(13, "Preeti Verma", "IT", 88000, 31, 7),
        Employee(14, "Amit Kumar", "IT", 82000, 29, 5),
        Employee(15, "Sanya Reddy", "Finance", 90000, 34, 9),
    ]
    
    for emp in sample_employees:
        try:
            db.add_employee(emp)
        except Exception as e:
            pass  # Skip if employee already exists


def main():
    print("\n" + "="*70)
    print("  🚀 SMART WORKFORCE ANALYTICS MANAGEMENT SYSTEM 🚀")
    print("="*70 + "\n")

    try:
        # Initialize database
        print("[1/5] Initializing Database Manager...")
        db = DatabaseManager()
        db.create_table()
        print("      ✓ Database initialized successfully\n")

        # Populate sample data
        print("[2/5] Loading Sample Employee Data...")
        populate_sample_data(db)
        employees_list = db.get_all_employees()
        print(f"      ✓ Loaded {len(employees_list)} employee records\n")

        # Load data into pandas dataframe
        print("[3/5] Performing Analytics & Numerical Computations...")
        conn = db.connect()
        analytics = AnalyticsEngine()
        analytics.load_data(conn)
        
        # Display comprehensive analytics
        print("\n" + "-"*70)
        print("STATISTICAL ANALYSIS")
        print("-"*70)
        analytics.calculate_statistics()
        
        print("\n" + "-"*70)
        print("DEPARTMENT-WISE ANALYSIS")
        print("-"*70)
        analytics.department_salary_analysis()
        
        print("\n" + "-"*70)
        print("CORRELATION & DATA INSIGHTS")
        print("-"*70)
        analytics.correlation_analysis()
        
        print("\n" + "-"*70)
        print("ADVANCED ANALYTICS")
        print("-"*70)
        analytics.salary_distribution_analysis()
        analytics.experience_level_analysis()
        
        # Generate visualizations
        print("\n[4/5] Generating Professional Visualizations...")
        report = ReportGenerator(output_dir="reports")
        
        if analytics.data is not None and not analytics.data.empty:
            reports_generated = report.generate_all(analytics.data)
            print(f"      ✓ Generated {len(reports_generated)} visualizations")
            print("\n      Generated Reports:")
            for report_type, filepath in reports_generated.items():
                print(f"      • {report_type.upper()}: {filepath}")
        
        conn.close()
        
        print("\n[5/5] System Summary")
        print("-"*70)
        print(f"✓ Total Employees: {len(employees_list)}")
        print(f"✓ Departments: {len(analytics.data['department'].unique())}")
        print(f"✓ Average Salary: ${analytics.data['salary'].mean():.2f}")
        print(f"✓ Salary Range: ${analytics.data['salary'].min():.2f} - ${analytics.data['salary'].max():.2f}")
        
        print("\n" + "="*70)
        print("✅ System Ready - All Analyses Complete!")
        print("="*70 + "\n")

    except Exception as e:
        print(f"\n❌ System Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()