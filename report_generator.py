import os
from typing import Dict
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class ReportGenerator:
    """Generates professional visualizations for workforce analytics."""

    def __init__(self, output_dir: str = "reports"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def _out(self, filename: str) -> str:
        return os.path.join(self.output_dir, filename)

    def plot_bar_department_avg_salary(self, df: pd.DataFrame) -> str:
        """Bar chart: Average salary by department"""
        dept_avg = df.groupby("department")["salary"].mean().sort_values(ascending=False)
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(dept_avg.index, dept_avg.values, color="#4C72B0", edgecolor="navy", linewidth=1.5)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'${height:,.0f}',
                   ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        ax.set_title("Average Salary by Department", fontsize=14, fontweight='bold')
        ax.set_xlabel("Department", fontsize=12)
        ax.set_ylabel("Average Salary ($)", fontsize=12)
        ax.grid(axis='y', alpha=0.3)
        fig.tight_layout()
        path = self._out("01_bar_chart_salary_by_dept.png")
        fig.savefig(path, dpi=150, bbox_inches='tight')
        plt.close(fig)
        return path

    def plot_scatter_experience_salary(self, df: pd.DataFrame) -> str:
        """Scatter plot: Experience vs Salary with trend line"""
        fig, ax = plt.subplots(figsize=(10, 6))
        scatter = ax.scatter(df["experience"], df["salary"], alpha=0.6, s=100, c=df["age"], 
                            cmap="viridis", edgecolor='black', linewidth=0.5)
        
        # Add trend line
        z = np.polyfit(df["experience"], df["salary"], 1)
        p = np.poly1d(z)
        ax.plot(df["experience"].sort_values(), p(df["experience"].sort_values()), 
               "r--", linewidth=2, label="Trend Line")
        
        ax.set_title("Experience vs Salary (colored by Age)", fontsize=14, fontweight='bold')
        ax.set_xlabel("Experience (years)", fontsize=12)
        ax.set_ylabel("Salary ($)", fontsize=12)
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label("Age", fontsize=11)
        ax.legend()
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        path = self._out("02_scatter_experience_salary.png")
        fig.savefig(path, dpi=150, bbox_inches='tight')
        plt.close(fig)
        return path

    def plot_salary_histogram(self, df: pd.DataFrame, bins: int = 12) -> str:
        """Histogram: Salary distribution"""
        fig, ax = plt.subplots(figsize=(10, 6))
        n, bins_edges, patches = ax.hist(df["salary"], bins=bins, color="#55A868", 
                                         edgecolor="darkgreen", linewidth=1.5, alpha=0.8)
        
        # Add mean and median lines
        mean_salary = df["salary"].mean()
        median_salary = df["salary"].median()
        ax.axvline(mean_salary, color='red', linestyle='--', linewidth=2, label=f'Mean: ${mean_salary:,.0f}')
        ax.axvline(median_salary, color='orange', linestyle='--', linewidth=2, label=f'Median: ${median_salary:,.0f}')
        
        ax.set_title("Salary Distribution", fontsize=14, fontweight='bold')
        ax.set_xlabel("Salary ($)", fontsize=12)
        ax.set_ylabel("Number of Employees", fontsize=12)
        ax.legend()
        ax.grid(axis='y', alpha=0.3)
        fig.tight_layout()
        path = self._out("03_histogram_salary_dist.png")
        fig.savefig(path, dpi=150, bbox_inches='tight')
        plt.close(fig)
        return path

    def plot_department_pie(self, df: pd.DataFrame) -> str:
        """Pie chart: Workforce distribution by department"""
        counts = df["department"].value_counts()
        colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF99CC']
        fig, ax = plt.subplots(figsize=(9, 7))
        wedges, texts, autotexts = ax.pie(
            counts.values,
            labels=counts.index,
            autopct="%1.1f%%",
            startangle=90,
            colors=colors,
            explode=[0.05 if i == 0 else 0 for i in range(len(counts))],
            textprops={'fontsize': 11, 'fontweight': 'bold'}
        )
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        ax.set_title("Workforce Share by Department", fontsize=14, fontweight='bold')
        fig.tight_layout()
        path = self._out("04_pie_chart_dept_dist.png")
        fig.savefig(path, dpi=150, bbox_inches='tight')
        plt.close(fig)
        return path

    def plot_age_distribution(self, df: pd.DataFrame) -> str:
        """Box plot: Age distribution by department"""
        fig, ax = plt.subplots(figsize=(10, 6))
        departments = df["department"].unique()
        age_data = [df[df["department"] == dept]["age"].values for dept in sorted(departments)]
        
        bp = ax.boxplot(age_data, labels=sorted(departments), patch_artist=True)
        
        # Customize colors
        for patch in bp['boxes']:
            patch.set_facecolor('#FF9999')
        
        ax.set_title("Age Distribution by Department", fontsize=14, fontweight='bold')
        ax.set_xlabel("Department", fontsize=12)
        ax.set_ylabel("Age (years)", fontsize=12)
        ax.grid(axis='y', alpha=0.3)
        fig.tight_layout()
        path = self._out("05_boxplot_age_by_dept.png")
        fig.savefig(path, dpi=150, bbox_inches='tight')
        plt.close(fig)
        return path

    def plot_experience_level_pie(self, df: pd.DataFrame) -> str:
        """Pie chart: Employees by experience level"""
        junior = len(df[df["experience"] < 3])
        mid = len(df[(df["experience"] >= 3) & (df["experience"] < 7)])
        senior = len(df[df["experience"] >= 7])
        
        sizes = [junior, mid, senior]
        labels = [f'Junior (< 3 yrs)\n{junior} emp', 
                  f'Mid-level (3-7 yrs)\n{mid} emp', 
                  f'Senior (7+ yrs)\n{senior} emp']
        colors = ['#FF9999', '#66B2FF', '#99FF99']
        
        fig, ax = plt.subplots(figsize=(9, 7))
        wedges, texts, autotexts = ax.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            startangle=45,
            colors=colors,
            textprops={'fontsize': 11, 'fontweight': 'bold'}
        )
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        ax.set_title("Employees by Experience Level", fontsize=14, fontweight='bold')
        fig.tight_layout()
        path = self._out("06_pie_chart_exp_level.png")
        fig.savefig(path, dpi=150, bbox_inches='tight')
        plt.close(fig)
        return path

    def plot_salary_by_experience_heatmap(self, df: pd.DataFrame) -> str:
        """Heatmap: Average salary by department and experience level"""
        df['exp_level'] = pd.cut(df['experience'], 
                                 bins=[0, 3, 7, 20], 
                                 labels=['Junior', 'Mid-level', 'Senior'])
        
        pivot_table = df.pivot_table(values='salary', 
                                     index='department', 
                                     columns='exp_level', 
                                     aggfunc='mean')
        
        fig, ax = plt.subplots(figsize=(10, 6))
        im = ax.imshow(pivot_table.values, cmap='RdYlGn', aspect='auto')
        
        ax.set_xticks(np.arange(len(pivot_table.columns)))
        ax.set_yticks(np.arange(len(pivot_table.index)))
        ax.set_xticklabels(pivot_table.columns)
        ax.set_yticklabels(pivot_table.index)
        
        # Add salary values as text
        for i in range(len(pivot_table.index)):
            for j in range(len(pivot_table.columns)):
                value = pivot_table.values[i, j]
                if not np.isnan(value):
                    text = ax.text(j, i, f'${value:,.0f}',
                                 ha="center", va="center", color="black", fontweight='bold')
        
        ax.set_title("Average Salary by Department and Experience Level", fontsize=14, fontweight='bold')
        ax.set_xlabel("Experience Level", fontsize=12)
        ax.set_ylabel("Department", fontsize=12)
        plt.colorbar(im, ax=ax, label='Salary ($)')
        fig.tight_layout()
        path = self._out("07_heatmap_salary_analysis.png")
        fig.savefig(path, dpi=150, bbox_inches='tight')
        plt.close(fig)
        return path

    def generate_all(self, df: pd.DataFrame) -> Dict[str, str]:
        """Generate all visualizations"""
        if df is None or df.empty:
            raise ValueError("Cannot generate charts from empty data.")
        
        reports = {
            "bar_chart": self.plot_bar_department_avg_salary(df),
            "scatter_plot": self.plot_scatter_experience_salary(df),
            "histogram": self.plot_salary_histogram(df),
            "pie_chart": self.plot_department_pie(df),
            "age_distribution": self.plot_age_distribution(df),
            "experience_levels": self.plot_experience_level_pie(df),
            "heatmap_analysis": self.plot_salary_by_experience_heatmap(df),
        }
        return reports
