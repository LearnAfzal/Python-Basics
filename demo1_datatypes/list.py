#list -> is mutable/editable
colors=["red","green","blue"]
print(type(colors))
print(colors[1])
print(type(colors))
colors.append("pink")
print(colors)
colors.insert(2,"orange")
print(colors)
colors.append("pink")
print(colors)
colors.insert(2,"orange")
print(colors)
#remove -> it will remove only the fisrt occurence
colors.remove("orange")
print(colors)
#to find length
print(len(colors))
#to remove based on the index
colors.remove(colors[5])
print(colors)
#pop -> remove/delete the last value & also it gives the output which item is deleted
removed_item=colors.pop()
print(colors)
print(removed_item)