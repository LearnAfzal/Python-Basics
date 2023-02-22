class Employee:
    company_name=None
    company_location=None

#initialization also called as constructor or init method
#self represents current object -> whatever object we created
    def __init__(self):
        self.emp_id=None
        self.emp_name=None
        self.emp_salary = None
        self.emp_performance = None

#to define a static method -> follow the below way
    @staticmethod
    def about_company():
        print("owned by software people")

#non-static method
    def display_employee_record(self):
        print(35*"-") #it will print hyphen 35 times
        print("Employee ID:", self.emp_id) #non-static variable
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Performance:", self.emp_performance)
        print("Company Name:", Employee.company_name) #static variable
        print(35 * "-")

    def calculate_bonus(self):
        #we can call other method inside a method
        self.display_employee_record() # displays employee details before updating bonus
        if self.emp_performance=="A":
            print(self.emp_name)
            print("10%")
            self.emp_salary=self.emp_salary+self.emp_salary*(10/100)
            print("updated salary with bonus is", self.emp_salary)
        elif self.emp_performance=="B":
            """print(self.emp_name)
            print("5%")"""
            self.emp_salary = self.emp_salary + self.emp_salary * (5 / 100)
            return self.emp_salary # code will get end here itself because we used return
        elif self.emp_performance=="C":
            """print(self.emp_name)
            print("2%")"""
            self.emp_salary = self.emp_salary + self.emp_salary * (5 / 100)
            return self.emp_salary # code will end here itself & will not proceed further because we used return
        else:
            print("No Bonus for :", self.emp_name)
        self.display_employee_record()  # displays employee details after updating bonus

