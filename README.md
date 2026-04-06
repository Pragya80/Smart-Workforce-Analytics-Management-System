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
| 🗄️ **Database Management** | SQLite-based employee data management with CRUD operations |
| 📊 **Analytics Engine** | Department-wise salary analysis and statistical computations |
| 📈 **Interactive Visualizations** | Bar charts, scatter plots, histograms, and pie charts |
| 💾 **Data Persistence** | Permanent storage with SQLite database |
| 📋 **Report Generation** | Automated report creation with matplotlib |
| 🔢 **Statistical Analysis** | Mean, median, and standard deviation calculations |
| ⚡ **Real-time Processing** | Process employee data in real-time |

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
├── 📄 main.py                      # Application entry point
├── 📄 database_manager.py          # Database operations handler
├── 📄 analytics_engine.py          # Analytics & statistics module
├── 📄 report_generator.py          # Report & visualization module
├── 📄 employee.py                  # Employee data model
├── 📄 requirements.txt             # Python dependencies
├── 🗄️  workforce.db                # SQLite database file
├── 📊 reports/                     # Generated reports directory
│   ├── 📈 bar_chart.png            # Department salary analysis
│   ├── 📊 scatter_plot.png         # Experience vs salary correlation
│   ├── 📉 histogram.png            # Salary distribution
│   └── 🥧 pie_chart.png            # Department workforce share
└── 📖 README.md                    # Project documentation

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
Handles all database operations using SQLite.

**Key Methods:**
- `connect()`: Establishes database connection
- `create_table()`: Creates employees table
- `add_employee(employee)`: Inserts new employee
- `get_all_employees()`: Retrieves all employee records
- `update_employee(emp_id, data)`: Updates employee information
- `delete_employee(emp_id)`: Removes employee record

### 3. **AnalyticsEngine.py** - Data Analysis
Performs statistical analysis on workforce data.

**Key Methods:**
- `load_data(db_connection)`: Loads employee data from database
- `department_salary_analysis()`: Calculates average salary by department
- `calculate_statistics()`: Computes mean, median, and standard deviation

**Key Libraries:**
- pandas: Data manipulation and analysis
- numpy: Numerical computations

### 4. **ReportGenerator.py** - Visualization
Generates professional reports and charts.

**Chart Types:**
- **Bar Chart**: Average salary by department
- **Scatter Plot**: Experience vs Salary correlation
- **Histogram**: Salary distribution analysis
- **Pie Chart**: Workforce distribution by department

**Methods:**
- `plot_bar_department_avg_salary()`: Department salary comparison
- `plot_scatter_experience_salary()`: Experience-salary relationship
- `plot_salary_histogram()`: Salary range distribution
- `plot_department_pie()`: Department workforce percentages
- `generate_all()`: Creates all reports at once

---

## 📊 Output Reports

The system generates four types of reports in the `reports/` directory:

### 1. Bar Chart - Department Average Salary
Shows average salary across different departments for comparison.

### 2. Scatter Plot - Experience vs Salary
Visualizes the relationship between employee experience and salary.

### 3. Histogram - Salary Distribution
Displays the distribution of salaries across the workforce.

### 4. Pie Chart - Department Distribution
Shows the percentage of workforce in each department.

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

1. **Initialization** → System components are loaded
2. **Data Input** → Employee data is added to the database
3. **Data Processing** → Analytics engine processes the data
4. **Analysis** → Statistical computations and trends
5. **Reporting** → Visual reports are generated
6. **Output** → Charts saved to `reports/` directory

---

## 🚀 Advanced Features

- ✅ Real-time data processing
- ✅ SQLite persistence
- ✅ Automated report generation
- ✅ Multi-metric analysis
- ✅ Department-wise statistics
- ✅ Professional visualization

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