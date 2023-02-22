marks=-15
#and/or -> only wordings should be used here in logical operators, if we use & then it will be considered as bitwise operator
if marks>=90 and marks<=100:
    print("A")
elif marks>=80 and marks<=89:
    print("B")
elif marks>=60 and marks<=79:
    print("C")
elif marks<60 and marks>0:
    print("D")
else:
    print("invalid number")


