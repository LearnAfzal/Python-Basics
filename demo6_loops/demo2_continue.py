numbers=[45,98,75,65,24,88,74,56,75]
for d in range(0,len(numbers)):
    if numbers[d]==24:
        continue # when 24 matches it continue back from for loop without printing/proceeding further
    print(numbers[d])