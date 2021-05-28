print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# If Else Syntax in Python
if height >= 120:
  print("You can ride the rollercoaster")
else:
  print("Sorry,you can't ride on the rollercoaster")

# Nested if/eval
if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("Whats your age?"))
  if age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $7.")
else:
  print("Sorry,you can't ride on the rollercoaster")

# elif 
if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("Whats your age?"))
  if age < 12:
    print("Child Ticket $5.")
  elif age <= 18:
    print("Youth Ticket $7.")
  else:
    print("Adult ticket $12.")
else:
  print("Sorry,you can't ride on the rollercoaster")

# Mutiple if
bill = 0;
if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("Whats your age?"))
  if age < 12:
    bill = 5;
    print("Child Ticket $5.")
  elif age <= 18:
    bill = 7
    print("Youth Ticket $7.")
  else:
    bill = 12
    print("Adult ticket $12.")
  wants_photo = input("Do u want the photo Y or N ?")
  if wants_photo == 'Y':
    bill += 3;
    print("Extra $3 for photo")
    
  print(f"Yor total bill is ${bill}")
else:
  print("Sorry,you can't ride on the rollercoaster")

