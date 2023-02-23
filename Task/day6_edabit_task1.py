#find football points

def football_points(win,draw,loose):
    totalpoints=(win*3)+(draw*1)+(loose*0)
    return totalpoints

print("total scored football points are",football_points(3,4,2))

#find total legs of animals

def animals(chickens,cows,pigs):
    totallegs=(chickens*2)+(cows*4)+(pigs*4)
    return totallegs

print("total number of legs are",animals(1,2,3))

#find discounted price

def discount_price(price,discount):
    finalprice=(price-(price*discount/100))
    return finalprice

print("final price is",discount_price(100,75))

#convert radians into degrees

def radians_to_degrees(radians):
    degrees=radians*(180/(22/7))
    return round(degrees,1)

print("Angle in degrees :",radians_to_degrees(20))

#find vowels count

def count_vowels(word):
    count=0
    for letter in word:
        if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
            count=count+1
    return count

print("total vowels in a word is:", count_vowels("aeiou"))

# Find the Odd Integer

"""def find_odd(numbers):
    odd=[]
    for x in range(0,len(numbers)-1):
        while numbers[x]==numbers[x+1]:
            break
        else:
            odd=odd.append(numbers(x))

    return odd

test=[1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]
find_odd(test)"""
