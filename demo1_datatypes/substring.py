welcome='hello world'
print(welcome[0])
print(welcome[0:5])
print(welcome[6:])
#reverse
print(welcome[-1])
#only one char will be printed if not make use of : (it means just accessing the index position)
print(welcome[-5])
print(welcome[-5:])
#to find the index of specific word or char
print(welcome.index("world"))
print(welcome.index("o"))#only first instance index will be givenas output
#to replace
print(welcome.replace("world","afzal"))

#extract the username without domain from mail id

mail="afzal.hello@gmail.com"
a=mail.index('@')
print(mail[:a])
b=mail.replace("@gmail.com","")
print(b)
c=mail.split("@")
print(c)
print(c[0])
