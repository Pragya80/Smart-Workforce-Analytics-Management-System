import os
from typing import Dict

import matplotlib.pyplot as plt
import pandas as pd


class ReportGenerator:
    """Matplotlib reports: bar, scatter, histogram, pie (hackathon requirements)."""

    def __init__(self, output_dir: str = "."):
        self.output_dir = output_dir

    def _out(self, filename: str) -> str:
        return os.path.join(self.output_dir, filename)

    def plot_bar_department_avg_salary(self, df: pd.DataFrame) -> str:
        dept_avg = df.groupby("department")["salary"].mean()
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(dept_avg.index.astype(str), dept_avg.values, color="#4C72B0")
        ax.set_title("Average Salary by Department")
        ax.set_xlabel("Department")
        ax.set_ylabel("Average salary")
        fig.tight_layout()
        path = self._out("bar_chart.png")
        fig.savefig(path, dpi=150)
        plt.close(fig)
        return path

    def plot_scatter_experience_salary(self, df: pd.DataFrame) -> str:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.scatter(df["experience"], df["salary"], alpha=0.85, c="#DD8452")
        ax.set_title("Experience vs Salary")
        ax.set_xlabel("Experience (years)")
        ax.set_ylabel("Salary")
        fig.tight_layout()
        path = self._out("scatter_plot.png")
        fig.savefig(path, dpi=150)
        plt.close(fig)
        return path

    def plot_salary_histogram(self, df: pd.DataFrame, bins: int = 10) -> str:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.hist(df["salary"], bins=bins, color="#55A868", edgecolor="white")
        ax.set_title("Salary Distribution")
        ax.set_xlabel("Salary")
        ax.set_ylabel("Frequency")
        fig.tight_layout()
        path = self._out("histogram.png")
        fig.savefig(path, dpi=150)
        plt.close(fig)
        return path

    def plot_department_pie(self, df: pd.DataFrame) -> str:
        counts = df["department"].value_counts()
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.pie(
            counts.values,
            labels=counts.index.astype(str),
            autopct="%1.1f%%",
            startangle=90,
        )
        ax.set_title("Workforce Share by Department")
        fig.tight_layout()
        path = self._out("pie_chart.png")
        fig.savefig(path, dpi=150)
        plt.close(fig)
        return path

    def generate_all(self, df: pd.DataFrame) -> Dict[str, str]:
        if df is None or df.empty:
            raise ValueError("Cannot generate charts from empty data.")
        os.makedirs(self.output_dir, exist_ok=True)
        return {
            "bar": self.plot_bar_department_avg_salary(df),
            "scatter": self.plot_scatter_experience_salary(df),
            "histogram": self.plot_salary_histogram(df),
            "pie": self.plot_department_pie(df),
        }
