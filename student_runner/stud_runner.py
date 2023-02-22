from student_package.student import Student
print(Student.schoolName)
stud1=Student(1001,"Jack","jack@gmail.com",45.2)
#if we dont know the order of arguments we can pass it as mentioned below
stud2=Student(studentRollno=1002,studentName="peter",studentMailid="peter@gmail.com",studentPercentage=85.2)
stud3=Student(studentRollno=1003,studentPercentage=56.2,studentName="mark",studentMailid="mark@gmail.com")
Student.schoolName="Global School"
Student.schoolAddress="Chennai"

"""
#stud1 details
stud1.studentName="jack"
stud1.studentRollno=1001
stud1.studentMailid="jack@gmail.com"
stud1.studentPercentage=45.2
#stud2 details
stud2.studentName="peter"
stud2.studentRollno=1002
stud2.studentMailid="peter@gmail.com"
stud2.studentPercentage=85.2
#stud3 details
stud3.studentName="mark"
stud3.studentRollno=1003
stud3.studentMailid="mark@gmail.com"
stud3.studentPercentage=56.2
"""
print(stud1.studentMailid)
print(stud2.studentMailid)
print(stud3.studentMailid)

#to assign 1 object's varaiable values to other object variables
"""stud2=stud1

print(stud1.studentMailid)
print(stud2.studentMailid)
print(stud3.studentMailid)"""


print(stud2.studentRollno)
print(stud2.studentName)
print(stud2.studentPercentage)

print(stud3.studentRollno)
print(stud3.studentName)
print(stud3.studentPercentage)

# call the static method
Student.about_school()

# call non-static method
print(stud2.get_student_name())
per=stud2.get_student_percentage()
print(per)

print(stud2.get_name_with_percentage())

# call the static method with static variables
print(Student.get_school_details())