class Employee:

    def __init__(self, emp_id, name, department, salary, age, experience):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        self.age = age
        self.experience = experience

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "salary": self.salary,
            "age": self.age,
            "experience": self.experience
        }

    def display(self):
        print(
            self.emp_id,
            self.name,
            self.department,
            self.salary
        )