import sqlite3
from typing import Optional

import numpy as np
import pandas as pd


class AnalyticsEngine:
    """Loads workforce data and runs NumPy-based statistical computations."""

    def __init__(self, db_path: str = "workforce.db"):
        self.db_path = db_path
        self._df: Optional[pd.DataFrame] = None

    def load_from_sqlite(self, table: str = "employees") -> pd.DataFrame:
        conn = sqlite3.connect(self.db_path)
        try:
            self._df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
        finally:
            conn.close()
        return self._df

    def from_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        self._df = df.copy()
        return self._df

    def get_dataframe(self) -> Optional[pd.DataFrame]:
        return self._df

    def _require_df(self) -> pd.DataFrame:
        if self._df is None or self._df.empty:
            raise ValueError(
                "No employee rows loaded. Use load_from_sqlite() or from_dataframe() first."
            )
        return self._df

    def department_salary_summary(self) -> pd.DataFrame:
        """Pandas grouping/aggregation for department-wise salary insight."""
        df = self._require_df()
        return (
            df.groupby("department")["salary"]
            .agg(mean_salary="mean", headcount="count", total_salary="sum")
            .sort_values("mean_salary", ascending=False)
        )

    def numpy_statistics(self) -> dict:
        """
        NumPy: mean, median, std, salary–experience correlation, z-score normalization.
        """
        df = self._require_df()
        salaries = np.asarray(df["salary"], dtype=float)
        experience = np.asarray(df["experience"], dtype=float)

        mean_s = float(np.mean(salaries))
        median_s = float(np.median(salaries))
        std_s = float(np.std(salaries))

        if len(salaries) < 2 or np.std(salaries) == 0 or np.std(experience) == 0:
            correlation = float("nan")
        else:
            correlation = float(np.corrcoef(salaries, experience)[0, 1])

        if std_s == 0:
            normalized = [0.0] * len(salaries)
        else:
            normalized = ((salaries - mean_s) / std_s).tolist()

        return {
            "mean_salary": mean_s,
            "median_salary": median_s,
            "std_salary": std_s,
            "salary_experience_correlation": correlation,
            "normalized_salary": normalized,
        }


def _sample_dataframe() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "emp_id": [1, 2, 3, 4, 5, 6],
            "name": ["A", "B", "C", "D", "E", "F"],
            "department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
            "salary": [42000, 51000, 58000, 62000, 47000, 55000],
            "age": [24, 31, 28, 35, 29, 33],
            "experience": [2, 5, 4, 8, 3, 6],
        }
    )


if __name__ == "__main__":
    from report_generator import ReportGenerator

    engine = AnalyticsEngine()
    try:
        engine.load_from_sqlite()
    except Exception:
        engine.from_dataframe(_sample_dataframe())
        print("Note: using sample DataFrame (SQLite empty/missing).")

    stats = engine.numpy_statistics()
    print("NumPy statistics:", {k: v for k, v in stats.items() if k != "normalized_salary"})
    print("Normalized salaries (z-scores):", stats["normalized_salary"])

    out_dir = "reports"
    ReportGenerator(output_dir=out_dir).generate_all(engine.get_dataframe())
    print(f"Charts saved under ./{out_dir}/")
