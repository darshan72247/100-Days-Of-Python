# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

combined_string = name1 + name2

true_count = 0
true_count = combined_string.count("t") + combined_string.count("r") + combined_string.count("u") + combined_string.count("e")


love_count = 0;
love_count = combined_string.count("l") + combined_string.count("o") + combined_string.count("v") + combined_string.count("e")

love_score = (true_count * 10) + love_count

if love_score <10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")