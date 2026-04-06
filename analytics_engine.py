import pandas as pd
import numpy as np
import sqlite3
from typing import Tuple


class AnalyticsEngine:
    """
    Analytics Engine for Pandas-based data analysis on employee workforce data.
    Handles department-wise analysis, filtering, sorting, grouping, and aggregation.
    """

    def __init__(self, db_path='workforce.db'):
        """
        Initialize the Analytics Engine with database path.
        
        Args:
            db_path (str): Path to the SQLite database file
        """
        self.db_path = db_path
        self.df = None

    def load_employee_data_from_db(self) -> pd.DataFrame:
        """
        Load employee data from SQLite database into a pandas DataFrame.
        
        Returns:
            pd.DataFrame: DataFrame containing all employee records
        """
        try:
            connection = sqlite3.connect(self.db_path)
            query = "SELECT * FROM employees"
            self.df = pd.read_sql_query(query, connection)
            connection.close()
            
            if self.df.empty:
                print("⚠️  No employee data found in database")
                return self.df
            
            print(f"✓ Loaded {len(self.df)} employee records")
            return self.df
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    # ==================== DEPARTMENT-WISE ANALYSIS ====================

    def analyze_by_department(self) -> pd.DataFrame:
        """
        Analyze employees grouped by department with salary statistics.
        
        Returns:
            pd.DataFrame: Department-wise analysis with count, avg salary, min/max salary
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded. Call load_employee_data_from_db() first")
            return None

        analysis = self.df.groupby('department').agg({
            'emp_id': 'count',
            'salary': ['mean', 'median', 'min', 'max', 'std']
        }).round(2)

        analysis.columns = ['Employee_Count', 'Avg_Salary', 'Median_Salary', 
                          'Min_Salary', 'Max_Salary', 'Std_Dev_Salary']
        
        print("\n📊 DEPARTMENT-WISE SALARY ANALYSIS:")
        print(analysis)
        return analysis

    def department_salary_statistics(self) -> pd.DataFrame:
        """
        Calculate detailed salary statistics per department using NumPy.
        
        Returns:
            pd.DataFrame: Department statistics including variance and range
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return None

        stats = {}
        for dept in self.df['department'].unique():
            dept_salaries = self.df[self.df['department'] == dept]['salary'].values
            
            stats[dept] = {
                'Count': len(dept_salaries),
                'Mean': np.mean(dept_salaries),
                'Median': np.median(dept_salaries),
                'Std_Dev': np.std(dept_salaries),
                'Variance': np.var(dept_salaries),
                'Min': np.min(dept_salaries),
                'Max': np.max(dept_salaries),
                'Range': np.max(dept_salaries) - np.min(dept_salaries)
            }

        stats_df = pd.DataFrame(stats).T.round(2)
        print("\n📈 DETAILED DEPARTMENT SALARY STATISTICS:")
        print(stats_df)
        return stats_df

    # ==================== FILTERING OPERATIONS ====================

    def filter_by_salary_range(self, min_salary: float, max_salary: float) -> pd.DataFrame:
        """
        Filter employees within a specified salary range.
        
        Args:
            min_salary (float): Minimum salary threshold
            max_salary (float): Maximum salary threshold
            
        Returns:
            pd.DataFrame: Filtered employee records
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return None

        filtered_df = self.df[(self.df['salary'] >= min_salary) & 
                             (self.df['salary'] <= max_salary)]
        
        print(f"\n🔍 EMPLOYEES WITH SALARY RANGE ${min_salary:,.0f} - ${max_salary:,.0f}:")
        print(f"Found {len(filtered_df)} employees")
        print(filtered_df[['emp_id', 'name', 'department', 'salary']])
        return filtered_df

    def filter_by_department(self, department_name: str) -> pd.DataFrame:
        """
        Filter employees by specific department.
        
        Args:
            department_name (str): Department name to filter
            
        Returns:
            pd.DataFrame: Employees in specified department
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return None

        filtered_df = self.df[self.df['department'].str.upper() == 
                             department_name.upper()]
        
        print(f"\n🔍 EMPLOYEES IN {department_name.upper()} DEPARTMENT:")
        print(f"Found {len(filtered_df)} employees")
        print(filtered_df[['emp_id', 'name', 'salary', 'age', 'experience']])
        return filtered_df

    def filter_by_experience(self, min_experience: int) -> pd.DataFrame:
        """
        Filter employees by minimum experience level.
        
        Args:
            min_experience (int): Minimum years of experience
            
        Returns:
            pd.DataFrame: Employees with specified experience
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return None

        filtered_df = self.df[self.df['experience'] >= min_experience]
        
        print(f"\n🔍 EMPLOYEES WITH {min_experience}+ YEARS EXPERIENCE:")
        print(f"Found {len(filtered_df)} employees")
        print(filtered_df[['emp_id', 'name', 'experience', 'salary']])
        return filtered_df

    def filter_by_salary_above(self, salary_threshold: float) -> pd.DataFrame:
        """
        Filter employees with salary above threshold.
        
        Args:
            salary_threshold (float): Salary threshold
            
        Returns:
            pd.DataFrame: High-earning employees
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return None

        filtered_df = self.df[self.df['salary'] > salary_threshold]
        
        print(f"\n🔍 EMPLOYEES WITH SALARY > ${salary_threshold:,.0f}:")
        print(f"Found {len(filtered_df)} employees")
        print(filtered_df[['emp_id', 'name', 'department', 'salary']])
        return filtered_df

    # ==================== SORTING OPERATIONS ====================

    def sort_by_salary(self, ascending: bool = False) -> pd.DataFrame:
        """
        Sort employees by salary.
        
        Args:
            ascending (bool): Sort in ascending order if True, descending if False
            
        Returns:
            pd.DataFrame: Sorted employee records
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return None

        sorted_df = self.df.sort_values('salary', ascending=ascending)
        order = "ASCENDING" if ascending else "DESCENDING"
        
        print(f"\n📋 EMPLOYEES SORTED BY SALARY ({order}):")
        print(sorted_df[['emp_id', 'name', 'department', 'salary']])
        return sorted_df

    def sort_by_experience(self, ascending: bool = False) -> pd.DataFrame:
        """
        Sort employees by years of experience.
        
        Args:
            ascending (bool): Sort in ascending order if True
            
        Returns:
            pd.DataFrame: Sorted employee records
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return None

        sorted_df = self.df.sort_values('experience', ascending=ascending)
        order = "ASCENDING" if ascending else "DESCENDING"
        
        print(f"\n📋 EMPLOYEES SORTED BY EXPERIENCE ({order}):")
        print(sorted_df[['emp_id', 'name', 'experience', 'salary']])
        return sorted_df

    def sort_by_name(self) -> pd.DataFrame:
        """
        Sort employees alphabetically by name.
        
        Returns:
            pd.DataFrame: Alphabetically sorted employee records
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return None

        sorted_df = self.df.sort_values('name')
        
        print("\n📋 EMPLOYEES SORTED BY NAME (A-Z):")
        print(sorted_df[['emp_id', 'name', 'department', 'salary']])
        return sorted_df

    def sort_by_age(self, ascending: bool = False) -> pd.DataFrame:
        """
        Sort employees by age.
        
        Args:
            ascending (bool): Sort in ascending order if True
            
        Returns:
            pd.DataFrame: Sorted employee records
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return None

        sorted_df = self.df.sort_values('age', ascending=ascending)
        order = "ASCENDING" if ascending else "DESCENDING"
        
        print(f"\n📋 EMPLOYEES SORTED BY AGE ({order}):")
        print(sorted_df[['emp_id', 'name', 'age', 'salary']])
        return sorted_df

    # ==================== GROUPING & AGGREGATION ====================

    def group_salary_by_department(self) -> pd.DataFrame:
        """
        Group and aggregate salary data by department.
        
        Returns:
            pd.DataFrame: Salary aggregation by department
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return None

        grouped = self.df.groupby('department')['salary'].agg([
            ('Total_Salary', 'sum'),
            ('Avg_Salary', 'mean'),
            ('Median_Salary', 'median'),
            ('Min_Salary', 'min'),
            ('Max_Salary', 'max'),
            ('Employee_Count', 'count')
        ]).round(2)

        print("\n📊 SALARY AGGREGATION BY DEPARTMENT:")
        print(grouped)
        return grouped

    def salary_distribution_by_age_group(self, bin_size: int = 10) -> pd.DataFrame:
        """
        Analyze salary distribution across age groups.
        
        Args:
            bin_size (int): Size of age bins (default 10 years)
            
        Returns:
            pd.DataFrame: Age-wise salary analysis
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return None

        # Create age groups
        self.df['age_group'] = pd.cut(self.df['age'], 
                                       bins=range(0, 100, bin_size), 
                                       right=False)
        
        age_analysis = self.df.groupby('age_group', observed=True).agg({
            'salary': ['mean', 'median', 'count'],
            'emp_id': 'count'
        }).round(2)

        age_analysis.columns = ['Avg_Salary', 'Median_Salary', 
                               'Salary_Count', 'Employee_Count']
        
        print(f"\n📊 SALARY DISTRIBUTION BY AGE GROUP ({bin_size}-year intervals):")
        print(age_analysis)
        
        # Remove temporary age_group column
        self.df.drop('age_group', axis=1, inplace=True)
        return age_analysis

    def group_by_department_and_experience(self) -> pd.DataFrame:
        """
        Multi-level grouping: Department and Experience Level.
        
        Returns:
            pd.DataFrame: Grouped and aggregated data
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return None

        grouped = self.df.groupby(['department', 'experience']).agg({
            'salary': ['mean', 'count'],
            'emp_id': 'count'
        }).round(2)

        grouped.columns = ['Avg_Salary', 'Salary_Count', 'Employee_Count']
        
        print("\n📊 GROUPING BY DEPARTMENT AND EXPERIENCE:")
        print(grouped)
        return grouped

    # ==================== ADVANCED ANALYSIS WITH NUMPY ====================

    def correlation_analysis(self) -> pd.DataFrame:
        """
        Calculate correlation between salary and other numeric features using NumPy.
        
        Returns:
            pd.DataFrame: Correlation matrix
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return None

        numeric_cols = self.df[['salary', 'age', 'experience']].copy()
        correlation = numeric_cols.corr()
        
        print("\n📈 CORRELATION ANALYSIS (Salary vs Other Factors):")
        print(correlation.round(4))
        return correlation

    def salary_normalization(self) -> pd.DataFrame:
        """
        Normalize salary data using NumPy (0-1 range).
        
        Returns:
            pd.DataFrame: Original data with normalized salary column
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return None

        result_df = self.df.copy()
        salary_values = result_df['salary'].values
        
        # Min-Max Normalization using NumPy
        min_sal = np.min(salary_values)
        max_sal = np.max(salary_values)
        normalized_salary = (salary_values - min_sal) / (max_sal - min_sal)
        
        result_df['normalized_salary'] = normalized_salary
        
        print("\n📊 SALARY NORMALIZATION (0-1 range):")
        print(result_df[['emp_id', 'name', 'salary', 'normalized_salary']].head(10))
        return result_df

    def salary_percentile_analysis(self, percentiles: list = [25, 50, 75, 90]) -> dict:
        """
        Calculate salary percentiles using NumPy.
        
        Args:
            percentiles (list): Percentile values to calculate
            
        Returns:
            dict: Percentile analysis
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return None

        salary_values = self.df['salary'].values
        percentile_values = np.percentile(salary_values, percentiles)
        
        percentile_dict = {f'{p}th_percentile': val 
                          for p, val in zip(percentiles, percentile_values)}
        
        print("\n📊 SALARY PERCENTILE ANALYSIS:")
        for percentile, value in percentile_dict.items():
            print(f"  {percentile}: ${value:,.2f}")
        
        return percentile_dict

    def performance_metrics(self) -> dict:
        """
        Calculate comprehensive performance metrics using NumPy and Pandas.
        
        Returns:
            dict: Key performance metrics
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return None

        salary_values = self.df['salary'].values
        experience_values = self.df['experience'].values
        
        metrics = {
            'total_employees': len(self.df),
            'total_salary_cost': np.sum(salary_values),
            'avg_salary': np.mean(salary_values),
            'median_salary': np.median(salary_values),
            'salary_std_dev': np.std(salary_values),
            'salary_variance': np.var(salary_values),
            'min_salary': np.min(salary_values),
            'max_salary': np.max(salary_values),
            'salary_range': np.max(salary_values) - np.min(salary_values),
            'avg_experience': np.mean(experience_values),
            'total_departments': self.df['department'].nunique(),
            'high_earners': len(self.df[self.df['salary'] > np.mean(salary_values)])
        }
        
        print("\n📊 KEY PERFORMANCE METRICS:")
        for metric, value in metrics.items():
            if isinstance(value, float):
                print(f"  {metric}: {value:,.2f}")
            else:
                print(f"  {metric}: {value}")
        
        return metrics

    def salary_by_department_summary(self) -> pd.DataFrame:
        """
        Create a comprehensive summary of salary by department.
        
        Returns:
            pd.DataFrame: Summary statistics
        """
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return None

        summary = self.df.groupby('department').agg({
            'salary': [np.sum, np.mean, np.median, np.std, np.min, np.max],
            'emp_id': 'count',
            'experience': np.mean,
            'age': np.mean
        }).round(2)

        summary.columns = ['Total_Salary', 'Avg_Salary', 'Median_Salary', 
                          'Std_Dev', 'Min_Salary', 'Max_Salary', 
                          'Employee_Count', 'Avg_Experience', 'Avg_Age']
        
        print("\n📊 COMPREHENSIVE DEPARTMENT SALARY SUMMARY:")
        print(summary)
        return summary

    # ==================== DATA OVERVIEW ====================

    def display_data_info(self):
        """Display basic information about the loaded dataset."""
        if self.df is None or self.df.empty:
            print("⚠️  No data loaded")
            return

        print("\n📋 DATASET INFORMATION:")
        print(f"  Total Records: {len(self.df)}")
        print(f"  Total Columns: {len(self.df.columns)}")
        print(f"  Columns: {', '.join(self.df.columns.tolist())}")
        print("\n  Data Types:")
        print(self.df.dtypes)
        print("\n  First 5 Records:")
        print(self.df.head())

    def get_dataframe(self) -> pd.DataFrame:
        """
        Get the current loaded DataFrame.
        
        Returns:
            pd.DataFrame: Current DataFrame
        """
        return self.df
