#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to tip calculator.\n")
total_bill_str = input("What was you total bill? ")
tip_perentage_str = input("What percentage tip would you like to give? 10, 12, or 15? ")
no_of_people_str = input("How may people to split the bill? ")

total_bill = float(total_bill_str)
tip_percentage = int(tip_perentage_str)
no_of_people = int(no_of_people_str)


pay_amount_including_tip = total_bill + ((tip_percentage / 100) * (total_bill))
pay_amount = round(pay_amount_including_tip / no_of_people,2)
print(f"Each person should pay: ${pay_amount}")