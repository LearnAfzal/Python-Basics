for a in range(1,10):
 print(a)
print(5*"*") #to differentiate the output in console

# with interval of 5
for b in range(1,11,5):
 print(b)
print(5*"*")

#print all list items one by one
colors = ["red", "green", "yellow", "blue", "green"]
for c in range(0,len(colors)):
    print(colors[c])
print(5*"*")

#print numbers less than or equal to 50
numbers=[45,98,75,65,24,88,74,56,75]
for d in range(0,len(numbers)):
    if numbers[d]<=50:
        print(numbers[d])