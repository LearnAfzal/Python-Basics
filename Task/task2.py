#Part1

custName="Mary Smith"
itemDesc="Shirt"
message=custName+" want to purchase a "+itemDesc
#how to add the double quote in the message
print(message)


#Part2

price=24.5
tax=10.0
quantity=2
message=custName+" want to purchase "+str(quantity)+" "+itemDesc
print(message)
total=price*quantity*tax
print("Total cost with tax is:",total)

#Part3

outOfStock=False
if quantity>1 and outOfStock==False:
    message = custName + " want to purchase " + str(quantity) + " " + itemDesc+"'s"
    print(message)
    print("Total cost with tax is:",total)
elif quantity==1 and outOfStock==False:
    message = custName + " want to purchase " + str(quantity) + " " + itemDesc
    print(message)
    print("Total cost with tax is:",total)
elif quantity==0 and outOfStock==False:
    print("please add the quantity of selected item")
elif outOfStock == True:
    print("Item is unavailable")
else:
    print("something went wrong")


#Part4

items=["pant","shirt","t-shirt","jean"]
print("please select a item which you need to purchase from total available items:",len(items))
#print(items[4])
itemno=int(input("print item num"))
index=itemno-1
print(index)
itemDesc=items[index]
print("selected item is "+str(itemno)+" : "+itemDesc)