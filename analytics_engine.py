import pandas as pd
import numpy as np


class AnalyticsEngine:
    """Performs comprehensive workforce analytics using Pandas and NumPy"""

    def __init__(self):
        self.data = None

    def load_data(self, db_connection):
        """Load employee data from database into pandas DataFrame"""
        try:
            query = "SELECT * FROM employees"
            self.data = pd.read_sql_query(query, db_connection)
            print(f"✓ Data loaded successfully ({len(self.data)} records)")
        except Exception as e:
            print(f"Error loading data: {e}")

    def calculate_statistics(self):
        """Calculate comprehensive salary statistics"""
        if self.data is not None and not self.data.empty:
            salaries = self.data["salary"]
            
            print(f"  Mean Salary:           ${np.mean(salaries):,.2f}")
            print(f"  Median Salary:         ${np.median(salaries):,.2f}")
            print(f"  Standard Deviation:    ${np.std(salaries):,.2f}")
            print(f"  Minimum Salary:        ${np.min(salaries):,.2f}")
            print(f"  Maximum Salary:        ${np.max(salaries):,.2f}")
            print(f"  Salary Range:          ${np.max(salaries) - np.min(salaries):,.2f}")
            print(f"  Total Payroll:         ${np.sum(salaries):,.2f}")
            print(f"  Variance:              ${np.var(salaries):,.2f}")

    def department_salary_analysis(self):
        """Analyze salary metrics by department"""
        if self.data is not None and not self.data.empty:
            dept_analysis = self.data.groupby("department").agg({
                "salary": ["mean", "min", "max", "std", "count"],
                "age": "mean",
                "experience": "mean"
            }).round(2)
            
            print("\n  Department-wise Salary Analysis:")
            for dept in self.data["department"].unique():
                dept_data = self.data[self.data["department"] == dept]
                avg_salary = dept_data["salary"].mean()
                min_salary = dept_data["salary"].min()
                max_salary = dept_data["salary"].max()
                count = len(dept_data)
                avg_exp = dept_data["experience"].mean()
                
                print(f"\n  {dept}:")
                print(f"    • Employees:      {count}")
                print(f"    • Avg Salary:     ${avg_salary:,.2f}")
                print(f"    • Salary Range:   ${min_salary:,.2f} - ${max_salary:,.2f}")
                print(f"    • Avg Experience: {avg_exp:.1f} years")

    def correlation_analysis(self):
        """Analyze correlations between numeric variables"""
        if self.data is not None and not self.data.empty:
            print("\n  Correlation Analysis:")
            correlation_matrix = self.data[["salary", "age", "experience"]].corr()
            
            print(f"  • Experience vs Salary: {correlation_matrix.loc['experience', 'salary']:.4f}")
            print(f"  • Age vs Salary:        {correlation_matrix.loc['age', 'salary']:.4f}")
            print(f"  • Age vs Experience:    {correlation_matrix.loc['age', 'experience']:.4f}")
            
            if correlation_matrix.loc['experience', 'salary'] > 0:
                print("  ✓ Positive correlation between experience and salary")

    def salary_distribution_analysis(self):
        """Analyze salary distribution and quartiles"""
        if self.data is not None and not self.data.empty:
            salaries = self.data["salary"]
            
            print("\n  Salary Distribution Analysis:")
            percentiles = np.percentile(salaries, [25, 50, 75])
            print(f"  • 25th Percentile (Q1): ${percentiles[0]:,.2f}")
            print(f"  • 50th Percentile (Q2): ${percentiles[1]:,.2f}")
            print(f"  • 75th Percentile (Q3): ${percentiles[2]:,.2f}")
            print(f"  • Interquartile Range:  ${percentiles[2] - percentiles[0]:,.2f}")
            
            # Calculate coefficient of variation
            cv = (np.std(salaries) / np.mean(salaries)) * 100
            print(f"  • Coefficient of Variation: {cv:.2f}%")

    def experience_level_analysis(self):
        """Categorize and analyze employees by experience level"""
        if self.data is not None and not self.data.empty:
            print("\n  Experience Level Analysis:")
            
            junior = len(self.data[self.data["experience"] < 3])
            mid = len(self.data[(self.data["experience"] >= 3) & (self.data["experience"] < 7)])
            senior = len(self.data[self.data["experience"] >= 7])
            
            total = len(self.data)
            print(f"  • Junior (< 3 years):  {junior} employees ({junior/total*100:.1f}%)")
            print(f"  • Mid-level (3-7 yrs): {mid} employees ({mid/total*100:.1f}%)")
            print(f"  • Senior (7+ years):   {senior} employees ({senior/total*100:.1f}%)")
            
            avg_salary_junior = self.data[self.data["experience"] < 3]["salary"].mean()
            avg_salary_mid = self.data[(self.data["experience"] >= 3) & (self.data["experience"] < 7)]["salary"].mean()
            avg_salary_senior = self.data[self.data["experience"] >= 7]["salary"].mean()
            
            print(f"\n  Average Salary by Experience Level:")
            print(f"  • Junior:    ${avg_salary_junior:,.2f}")
            print(f"  • Mid-level: ${avg_salary_mid:,.2f}")
            print(f"  • Senior:    ${avg_salary_senior:,.2f}")