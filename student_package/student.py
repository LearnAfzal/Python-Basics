class Student:
    schoolName=None
    schoolAddress=None
    def __init__(self,studentRollno=None,studentName=None,studentMailid=None,studentPercentage=None): # here all the arguments are optional because
        # we already assigned the default value as "None", if nothing is mentioned then it will be mandatory (always keep the optinal value as last one inside arguments)
        self.studentRollno=studentRollno
        self.studentName=studentName
        self.studentMailid=studentMailid
        self.studentPercentage=studentPercentage

    def get_student_name(self):
        return self.studentName

    def get_student_percentage(self):
        return self.studentPercentage

    def get_name_with_percentage(self):
        #return "hi", self.studentName,"your percentage is :", self.studentPercentage
        #if we use comma then same coma would be displayed in output too
        #with single quote wherever we used double quote
        return "hi "+self.studentName+" your percentage is : "+str(self.studentPercentage) #concatenate is possible only in string

    @staticmethod
    def about_school():
        print("owned by the people")

    @staticmethod
    def get_school_details():
        return Student.schoolName+" is located in "+Student.schoolAddress
