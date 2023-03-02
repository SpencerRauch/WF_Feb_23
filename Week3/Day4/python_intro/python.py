print("Hello")

# comment 

"""
multiline
comment
"""

# multiline
# comment

number = 9

string = "text"

print(string + str(number))

#type conversion functions in python
#int() str() float() type()

# f-string (format string)

print(f"The number is {number}, The text was {string}")
# r""

bool = True
bool2 = False

if not number > 5 or number <= 199:
    print("Large number")
    number = number + 1
    number += 1
    # number++
elif number == 4:
    print("Its 4")
else:
    print("not big")


list = [1,2,3,4,5]
list[2]
print(f"The length is {len(list)} ")

# adding into a list
list.append(6)

dict = {
    'key': 'value',
    'second_key': 9
}
# snake case : all lower case, separated by _ 

def add(a,b):
    return a+b

result = add(3,2)
print(result)

# for ____ in ___:

#first blank: is our iterative variable
#second blank: the collection we are iterating over


# range(start, stop, step)
#start is optional, defaults to 0 and is inclusive
#stop is required and exclusive
#step the amount to iterate by optional, default 1
# for i in range(1,100,2):
#     print(i)

list2 = ["pineapple", "kiwi", "oranges"]

# for fruit in list2:
#     print(fruit)
#     # list2[fruit] = 'apple'

# print(list2)

# for index in range(len(list2)):
#     print(list2[index])
#     list2[index] = "apple"

# print(list2)

dict = {
    'key': 'value',
    'second_key': 9
}

for key in dict:
    print(f"The key is {key} and the value is {dict[key]}")

