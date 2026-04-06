# 🚀 Smart Workforce Analytics Management System

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

**A comprehensive workforce analytics platform for data-driven HR insights and decision making**

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Project Architecture](#project-architecture)
- [Directory Structure](#directory-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Core Components](#core-components)
- [Output Reports](#output-reports)
- [Database Schema](#database-schema)
- [Contributing](#contributing)

---

## 🎯 Overview

The **Smart Workforce Analytics Management System** is an integrated platform designed to analyze and manage employee data efficiently. It provides actionable insights into workforce metrics including salary analysis, experience correlation, department distribution, and comprehensive statistical reporting.

### Purpose
- 📊 Extract meaningful insights from employee data
- 📈 Generate interactive visualizations and reports
- 💼 Support data-driven HR decisions
- 🔍 Analyze workforce trends and patterns
- 📉 Monitor salary distributions and department metrics

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🗄️ **Database Management** | SQLite-based employee data management with full CRUD operations |
| 📊 **Advanced Analytics** | Department-wise analysis, correlation analysis, percentile calculations |
| 📈 **7 Professional Visualizations** | Bar charts, scatter plots, histograms, pie charts, heatmaps, and more |
| 💾 **Data Persistence** | Permanent SQLite database with error handling |
| 📋 **Comprehensive Reports** | Automated multi-format report generation with matplotlib |
| 🔢 **Statistical Analysis** | Mean, median, std dev, variance, percentiles, correlation analysis |
| 📉 **Distribution Analysis** | Salary distribution, experience levels, department metrics |
| 🎯 **Trend Analysis** | Linear regression trend lines and correlation insights |
| ⚡ **Real-time Processing** | Process and analyze employee data in real-time |

---

## 🏗️ Project Architecture

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    SMART WORKFORCE SYSTEM                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────┐                                          │
│  │   main.py        │                                          │
│  │  (Entry Point)   │                                          │
│  └────────┬─────────┘                                          │
│           │                                                     │
│    ┌──────┴──────────────────┬─────────────────────┐           │
│    │                         │                     │           │
│ ┌──▼──────────────┐  ┌─────▼────────────┐  ┌────▼────────┐   │
│ │ DatabaseManager  │  │ AnalyticsEngine  │  │ ReportGen   │   │
│ │                  │  │                  │  │ Generator   │   │
│ │ - connect()      │  │ - load_data()    │  │             │   │
│ │ - create_table() │  │ - statistics()   │  │ - bar_chart │   │
│ │ - add_employee() │  │ - analysis()     │  │ - scatter   │   │
│ │ - get_employees()│  │                  │  │ - histogram │   │
│ │ - update()       │  │                  │  │ - pie_chart │   │
│ │ - delete()       │  │                  │  │             │   │
│ └──────┬───────────┘  └────────┬──────────┘  └────┬────────┘   │
│        │                       │                   │           │
│        │         ┌─────────────┘                   │           │
│        │         │                                 │           │
│    ┌───▼─────────▼──────┐          ┌──────────────▼──────┐    │
│    │   workforce.db     │          │  reports/ (output)  │    │
│    │   (SQLite DB)      │          │  - bar_chart.png    │    │
│    │                    │          │  - scatter_plot.png │    │
│    │  employees table   │          │  - histogram.png    │    │
│    │                    │          │  - pie_chart.png    │    │
│    └────────────────────┘          └─────────────────────┘    │
│                                                                 │
│  ┌──────────────────┐                                          │
│  │   employee.py    │                                          │
│  │  (Data Model)    │                                          │
│  └──────────────────┘                                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Technology Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.8+ |
| **Database** | SQLite3 |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib |
| **Data Model** | Python Classes |

---

## 📂 Directory Structure

```
Smart-Workforce-Analytics-Management-System/
│
├── 📄 main.py                              # Application entry point with workflow
├── 📄 database_manager.py                  # SQLite database operations (CRUD)
├── 📄 analytics_engine.py                  # Advanced analytics & statistics
├── 📄 report_generator.py                  # 7 professional visualizations
├── 📄 employee.py                          # Employee data model
├── 📄 requirements.txt                     # Python dependencies (pandas, numpy, matplotlib)
├── 📄 README.md                            # Project documentation
├── 📄 ENHANCEMENTS.md                      # Detailed enhancements documentation
├── 🗄️  workforce.db                        # SQLite database file
└── 📊 reports/                             # Generated visualizations directory
    ├── 📈 01_bar_chart_salary_by_dept.png       # Avg salary by department
    ├── 📊 02_scatter_experience_salary.png      # Experience vs salary correlation
    ├── 📉 03_histogram_salary_dist.png          # Salary distribution analysis
    ├── 🥧 04_pie_chart_dept_dist.png            # Department workforce share
    ├── 📦 05_boxplot_age_by_dept.png            # Age distribution by department
    ├── 🎯 06_pie_chart_exp_level.png            # Experience level distribution
    └── 🔥 07_heatmap_salary_analysis.png        # Multi-dimensional salary analysis
```

---

## 📋 Prerequisites

- **Python 3.8** or higher
- **pip** (Python package manager)
- **Git** (for cloning the repository)

---

## 🔧 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/Pragya80/Smart-Workforce-Analytics-Management-System.git
cd Smart-Workforce-Analytics-Management-System
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python main.py
```

---

## 💻 Usage Guide

### Basic Usage

```python
# The main.py script initializes the system:

from database_manager import DatabaseManager
from analytics_engine import AnalyticsEngine
from report_generator import ReportGenerator
from employee import Employee

# 1. Initialize Database
db = DatabaseManager()
db.connect()

# 2. Add Employees
emp = Employee(emp_id=1, name="John Doe", department="IT", 
               salary=75000, age=30, experience=5)
db.add_employee(emp)

# 3. Perform Analytics
analytics = AnalyticsEngine()
analytics.department_salary_analysis()
analytics.calculate_statistics()

# 4. Generate Reports
report = ReportGenerator()
employees = db.get_all_employees()
report.generate_all(df)
```

### Common Operations

#### Add an Employee
```python
emp = Employee(1, "Alice Smith", "HR", 65000, 28, 3)
db.add_employee(emp)
```

#### Retrieve All Employees
```python
employees = db.get_all_employees()
```

#### Update Employee Information
```python
db.update_employee(1, {
    "name": "Alice Johnson",
    "department": "Finance",
    "salary": 70000,
    "age": 29,
    "experience": 4
})
```

#### Delete Employee
```python
db.delete_employee(1)
```

---

## 🔧 Core Components

### 1. **Employee.py** - Data Model
Represents employee entity with attributes:
- `emp_id`: Unique employee identifier
- `name`: Employee full name
- `department`: Department assignment
- `salary`: Annual salary
- `age`: Employee age
- `experience`: Years of experience

**Methods:**
- `to_dict()`: Converts employee object to dictionary
- `display()`: Prints employee information

### 2. **DatabaseManager.py** - Data Persistence
Handles all database operations using SQLite with error handling.

**Key Methods:**
- `connect()`: Establishes database connection
- `create_table()`: Creates employees table
- `add_employee(employee)`: Inserts new employee (with duplicate handling)
- `get_all_employees()`: Retrieves all employee records
- `update_employee(emp_id, data)`: Updates employee information
- `delete_employee(emp_id)`: Removes employee record

### 3. **AnalyticsEngine.py** - Advanced Data Analysis
Performs comprehensive statistical and analytical operations using Pandas and NumPy.

**Core Analysis Methods:**
- `load_data(db_connection)`: Loads employee data from database into DataFrame
- `calculate_statistics()`: Computes mean, median, std dev, min, max, range, variance
- `department_salary_analysis()`: Department-wise salary metrics and aggregation
- `correlation_analysis()`: Pearson correlation between salary, age, and experience
- `salary_distribution_analysis()`: Quartile analysis, percentiles, IQR, coefficient of variation
- `experience_level_analysis()`: Employee categorization and salary by experience level

**Key Libraries:**
- **pandas**: Data manipulation, grouping, aggregation, pivot tables
- **numpy**: Statistical computations (mean, median, percentile, correlation, polynomial fitting)

### 4. **ReportGenerator.py** - Professional Visualizations
Generates 7 professional business-grade visualizations with matplotlib.

**Visualization Methods:**

1. **`plot_bar_department_avg_salary()`** 
   - Sorted bar chart of average salary by department
   - Value labels for precision
   - Department salary benchmarking

2. **`plot_scatter_experience_salary()`**
   - Scatter plot with age color mapping
   - Linear regression trend line (0.83 correlation)
   - Multi-dimensional experience-salary relationship

3. **`plot_salary_histogram()`**
   - Salary distribution with 12 bins
   - Mean and median reference lines
   - Frequency analysis and distribution shape

4. **`plot_department_pie()`**
   - Workforce distribution by department
   - Percentage breakdown with exploded segments
   - Department composition analysis

5. **`plot_age_distribution()`**
   - Box plot showing age quartiles by department
   - Outlier identification
   - Age demographics and spread

6. **`plot_experience_level_pie()`**
   - Employee categorization (Junior < 3, Mid-level 3-7, Senior 7+)
   - Experience level distribution
   - Career progression insights

7. **`plot_salary_by_experience_heatmap()`**
   - Multi-dimensional heatmap analysis
   - Salary by department × experience level
   - Color-coded salary ranges (red=low, green=high)

**Output:** All visualizations saved as high-resolution PNG files (150+ dpi)

---

## 📊 Output Reports & Analytics

The system generates **7 professional visualizations** and comprehensive numerical analyses:

### Visualizations Generated

#### 1. 📈 Bar Chart - Department Salary Comparison
- Sorted average salary by department
- Visual salary benchmarking
- Department compensation analysis

#### 2. 📊 Scatter Plot - Experience vs Salary with Trend Line
- Correlation visualization (0.83 strong positive)
- Age-based color mapping
- Linear regression trend line
- Employee career progression insights

#### 3. 📉 Histogram - Salary Distribution
- 12-bin salary distribution
- Mean ($76,400) and median ($75,000) reference lines
- Distribution shape analysis
- Salary range identification

#### 4. 🥧 Pie Chart - Department Workforce Distribution
- Percentage breakdown by department
- Employee count per department
- Organizational structure visualization

#### 5. 📦 Box Plot - Age Distribution by Department
- Quartile analysis by department
- Outlier identification
- Age spread and demographics
- Department age composition

#### 6. 🎯 Pie Chart - Experience Level Distribution
- **Junior (< 3 years)**: 13.3% of workforce
- **Mid-level (3-7 years)**: 53.3% of workforce
- **Senior (7+ years)**: 33.3% of workforce
- Career progression metrics

#### 7. 🔥 Heatmap - Multi-Dimensional Salary Analysis
- Salary by Department × Experience Level
- Color-coded ranges (red = low, green = high)
- Cross-tabulation analysis
- Advanced insights for compensation strategy

### Numerical Analytics Output

**Statistical Summary:**
```
Mean Salary:           $76,400.00
Median Salary:         $75,000.00
Standard Deviation:    $9,714.59
Minimum Salary:        $62,000.00
Maximum Salary:        $95,000.00
Salary Range:          $33,000.00
Total Payroll:         $1,146,000.00

Quartile Analysis:
25th Percentile (Q1):  $69,000.00
50th Percentile (Q2):  $75,000.00
75th Percentile (Q3):  $83,500.00
Interquartile Range:   $14,500.00
Coefficient of Variation: 12.72%
```

**Correlation Analysis:**
```
Experience vs Salary: 0.8286 (Strong Positive)
Age vs Salary:        0.8421 (Strong Positive)
Age vs Experience:    0.9885 (Very Strong Positive)
```

**Department-wise Analysis:**
```
IT:         $84,000 avg (5 employees, 5.8 yrs avg exp)
Finance:    $81,250 avg (4 employees, 6.8 yrs avg exp)
Marketing:  $69,500 avg (2 employees, 4.0 yrs avg exp)
Operations: $67,500 avg (2 employees, 5.5 yrs avg exp)
HR:         $63,500 avg (2 employees, 2.5 yrs avg exp)
```

**Experience Level Analysis:**
```
Junior:     $68,500 avg (13.3% of employees)
Mid-level:  $72,625 avg (53.3% of employees)
Senior:     $85,600 avg (33.3% of employees)
Salary Premium: Senior earns 25% more than mid-level
```

---

## 🗄️ Database Schema

### Employees Table

```sql
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL,
    age INTEGER NOT NULL,
    experience INTEGER NOT NULL
);
```

**Table Structure:**

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| emp_id | INTEGER | PRIMARY KEY | Unique employee identifier |
| name | TEXT | NOT NULL | Employee full name |
| department | TEXT | NOT NULL | Department assignment |
| salary | REAL | NOT NULL | Annual salary (in dollars) |
| age | INTEGER | NOT NULL | Employee age |
| experience | INTEGER | NOT NULL | Years of professional experience |

---

## 🎨 Dependencies

```
pandas        # Data manipulation and analysis
numpy         # Numerical computing
matplotlib    # Data visualization
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 📈 System Workflow

### 5-Step Execution Process

1. **[1/5] Initialization** 
   - Database manager setup
   - SQLite connection established
   - Employee table created

2. **[2/5] Data Loading** 
   - Sample employee data populated (15 records)
   - Data validation and integrity checks
   - Records committed to database

3. **[3/5] Analytics Processing** 
   - Data loaded into pandas DataFrame
   - Statistical computations performed
   - Department-wise analysis calculated
   - Correlation analysis executed
   - Percentile and distribution analysis completed
   - Experience level categorization

4. **[4/5] Report Generation** 
   - 7 professional visualizations created
   - High-resolution PNG output (150+ dpi)
   - Charts saved to `reports/` directory
   - Value annotations and legends added

5. **[5/5] System Summary** 
   - Total employee count displayed
   - Department statistics summarized
   - Average salary calculated
   - Salary range displayed
   - System ready confirmation

---

## 🚀 Advanced Features

### Numerical Analysis
- ✅ Descriptive Statistics (Mean, Median, Mode, Std Dev, Variance, Range)
- ✅ Distribution Analysis (Quartiles, Percentiles, IQR, Skewness metrics)
- ✅ Correlation Analysis (Pearson correlation matrix)
- ✅ Trend Analysis (Linear regression with numpy polyfit)
- ✅ Department Aggregation (Multi-metric grouping)
- ✅ Experience Level Categorization (3-tier classification)

### Data Processing
- ✅ Pandas DataFrame operations
- ✅ Data grouping and aggregation
- ✅ Pivot table analysis
- ✅ Multi-dimensional cross-tabulation
- ✅ Automatic data type handling

### Visualization
- ✅ 7 different chart types
- ✅ Color-coded multi-dimensional analysis
- ✅ Value annotations and labels
- ✅ Legend and reference lines
- ✅ Professional styling and formatting
- ✅ High-resolution output (150+ dpi)

### Database Features
- ✅ SQLite persistent storage
- ✅ ACID compliance
- ✅ Exception handling and error management
- ✅ Connection pooling
- ✅ Duplicate entry handling

---

## 📋 Sample Data & Analytics

### Included Sample Dataset
The system comes with **15 sample employees** across **5 departments**:
- **IT**: 5 employees (Avg: $84,000, Exp: 5.8 yrs)
- **Finance**: 4 employees (Avg: $81,250, Exp: 6.8 yrs)  
- **Marketing**: 2 employees (Avg: $69,500, Exp: 4.0 yrs)
- **Operations**: 2 employees (Avg: $67,500, Exp: 5.5 yrs)
- **HR**: 2 employees (Avg: $63,500, Exp: 2.5 yrs)

### Key Insights from Analytics
- **Positive Correlation**: Experience strongly correlates with salary (r=0.83)
- **Salary Premium**: IT department pays 33% more than HR
- **Experience Effect**: Senior employees earn 25% more than mid-level
- **Distribution**: Mostly mid-level workforce (53.3%) with strong senior representation (33.3%)
- **Compensation**: Total payroll of $1,146,000 with low variance (CV=12.72%)

---

## 🎓 Learning Outcomes

This project demonstrates comprehensive implementation of:

### 1. Database-Driven Python Applications
- SQLite database design and implementation
- CRUD operations with error handling
- Connection management and transaction handling
- Data persistence and retrieval

### 2. Data Analysis with Pandas & NumPy
- DataFrame operations and manipulations
- Grouping, aggregation, and filtering
- Statistical computations and analysis
- Correlation matrix calculations
- Percentile and quartile analysis
- Data pivoting and cross-tabulation

### 3. Data Visualization with Matplotlib
- Multiple chart types (bar, scatter, histogram, pie, box plot, heatmap)
- Color mapping and multi-dimensional visualization
- Trend line analysis with numpy
- Professional styling and annotations
- High-resolution output generation

### 4. Object-Oriented Programming (OOP)
- Class design with single responsibility principle
- Encapsulation and modularity
- Method organization and inheritance
- Clean code architecture

### 5. Real-World HR Analytics Workflow
- Employee data management
- Compensation analysis
- Department performance metrics
- Career progression insights
- Organizational structure analysis
- Data-driven decision making

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit changes (`git commit -m 'Add improvement'`)
5. Push to branch (`git push origin feature/improvement`)
6. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👤 Author

**Pragya80**

---

## 📞 Support & Contact

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review the code comments

---

## 🎉 Thank You!

Thank you for using the Smart Workforce Analytics Management System. We hope this tool helps you make better data-driven HR decisions!

<div align="center">

**Made with ❤️ for Smart Workforce Management**

</div>

## Technologies Used

- Python
- SQLite
- NumPy
- Pandas
- Matplotlib
- Object-Oriented Programming