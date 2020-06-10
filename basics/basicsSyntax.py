import os
import sys
import random

print("Hello world")

# String
name = "Hellow world"

print(name.upper())

todo_list = ['List one', 'List two']

print(todo_list[0])

grocery_list = ['tomato', 'banana', 'apple']

other_event = ['wash car', 'cash check', 'pick up kids']

todo_list = [grocery_list, other_event]
print(todo_list[1][1])

# tuple

pi_tuple = (2, 2, 3, 3, 4, 4)

new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

print(len(new_tuple))

# dictionary

super_villains = {'Fiddler': 'Isaac Bowin',
                  'Captain cold': 'Leonard Snart', 'Pied Piper': 'Thomas Peterson'}

print(super_villains['Fiddler'])

super_villains['Pied Piper'] = 'Rajaram'

print(super_villains.get('Pied Piper'))

# Condition

age = 21

if age >= 21:
    print('You are old enough to drive heavy trucks')
elif age >= 16:
    print('You are old enough to drive a car')
else:
    print('You are not old enough to drive')

if((age >= 1) and (age <= 18)):
    print('You get a birthday')
elif (age == 21) and(age >= 65):
    print('you get a birthday')
elif not(age == 30):
    print("you don't get a birthday")
else:
    print("you get a birthday party yeah")

# Loop

for x in range(0, 10):
    print(x, " ", end="")

# for array loop
for y in grocery_list:
    print(y)

# Multidimension array loop
for x in range(0, len(grocery_list)-1):
    for y in range(0, len(other_event)-1):
        print(todo_list[x][y], " ", end="")

# while loop


random_num = random.randrange(0, 100)

# while(random_num != 15):
#     print(random_num)
#     random_num = random.randrange(0, 100)

i = 0

while (i <= 20):
    if(i % 2 == 0):
        print(i)
    elif(i == 9):
        break
    else:
        i += 1
        continue
    i += 1

#  function


def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum


print("Add Number function call", addNumber(1, 5))


#  input from user
print("What is your name?")
# name = sys.stdin.readline()
# print("Hello : " + name)

#  string manipulation

long_string = "I'll catch you if you fall - the floor"

print(long_string[0:4])
print(long_string[-5:])
print(long_string[:-5])
print(long_string[:4] + " be there")

#  %c- char, %s - string %d-number %.5f - decimal
print("%c is my %s letter and my number %d number is %.5f" %
      ('X', 'favorite', 1, .14))

print(long_string.find("floor"))

print(long_string.isalpha())

print(long_string.isalnum())
print(long_string.replace("floor", "Ground"))
print(long_string.strip())
print(len(long_string))

quote_list = long_string.split(" ")
print(quote_list)

#  file io
test_file = open("test.txt", "wb")
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("Write me to the file", 'UTF-8'))
test_file.close()

test_file = open("test.txt", "r+")
text_in_file = test_file.read()
print(text_in_file)
os.remove("text.txt")

#  Object

