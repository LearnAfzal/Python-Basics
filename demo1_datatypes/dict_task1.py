student={"name":"afzal",
             "id":"153192",
             "mail":"test@gmail.com",
         "marks":[80,70,90,60,35],
         "sports":{"indoor":"carrom","outdoor":"cricket"}}
print(student)
print(type(student["marks"]))
#to get the value of marks
print(student["marks"][1])
print(type(student["marks"][1]))
print(student["sports"]["indoor"])
