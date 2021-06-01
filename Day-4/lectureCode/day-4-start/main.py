import random
import pi

# Random Int
print(random.randint(100,200))

# Making a file and importing it to use.
print(pi.pi)

# Random floating point number
print(random.random())

# Random number in range of 1<= x <= 5
print(int((random.random() * 5) + 1))

# List in python
fruits_with_PLUCode = ["Apple",4173,"Banana",4011,"Cherry",4245]

print(fruits_with_PLUCode[0])

# Note:- we can use negative index to travel through the list in reverse order

# For loop to travel through the list
for i in fruits_with_PLUCode:
  print(i)

# append
fruits_with_PLUCode.append("Watermelon");

# extends(list[])
fruits_with_PLUCode.extend(["kiwi","cherry","orange"]);

# nested list
fruits = ["Grapes","Cherries","Pears","Strawberries","Pears"]
vegetables = ["Potatoes","Onion","Spinach","Celery"]
dirty_dozen = [fruits,vegetables]

print(dirty_dozen)