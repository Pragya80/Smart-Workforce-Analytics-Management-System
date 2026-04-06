import pandas as pd
import numpy as np


class AnalyticsEngine:

    def __init__(self):
        self.data = None

    def load_data(self, db_connection):
        try:
            query = "SELECT * FROM employees"
            self.data = pd.read_sql_query(query, db_connection)
            print("Data loaded successfully")
        except Exception as e:
            print("Error loading data:", e)

    def department_salary_analysis(self):
        if self.data is not None:
            result = self.data.groupby("department")["salary"].mean()
            print("Department-wise average salary:")
            print(result)

    def calculate_statistics(self):
        if self.data is not None:
            salaries = self.data["salary"]

            print("Mean Salary:", np.mean(salaries))
            print("Median Salary:", np.median(salaries))
            print("Standard Deviation:", np.std(salaries))