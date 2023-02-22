from demo4_employee.employee_module import Employee

print(Employee.company_name)
print(Employee.company_location)

Employee.company_name="eInfoChips"
Employee.company_location="Chennai"

print(Employee.company_name)
print(Employee.company_location)

#object which we create here it will automatically go and directly fetch the def__init__

emp1=Employee()
emp2=Employee()
emp3=Employee()

print(emp1.emp_id)
print(emp2.emp_id)
print(emp3.emp_id)

#call static method using class name
Employee.about_company()

#call non-static method using object name
emp1.display_employee_record()

emp2.emp_name="afzal"
emp2.emp_performance="A"
emp2.emp_salary=5000

emp2.calculate_bonus()
print(emp2.emp_salary)

emp1.emp_name="afzalkhan"
emp1.emp_performance="B"
emp1.emp_salary=10000

print(emp1.calculate_bonus())
