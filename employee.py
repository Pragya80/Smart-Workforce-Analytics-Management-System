class Employee:

    def __init__(self, emp_id, name, department, salary, age, experience):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        self.age = age
        self.experience = experience

    def display(self):
        print(self.name, self.department, self.salary)