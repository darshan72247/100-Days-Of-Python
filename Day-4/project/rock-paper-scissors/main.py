import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

games_images = [rock,paper,scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice >= 3 or player_choice <= -1:
  print("Soory you enterd an invalid input")
  exit(0)

print(games_images[player_choice])

computer_choice = random.randint(0,2);
print("Computer choose :")

print(games_images[computer_choice])

# Rock wins against scissor
# Scissor win against paper
# paper win against rock.

if player_choice == 0 and computer_choice == 2:
  print("You win :)")
elif player_choice == 2 and computer_choice == 1:
  print("You win :)")
elif player_choice == 1 and computer_choice == 0:
  print("You win :)")
elif player_choice == computer_choice:
  print("Draw! :|")
else:
  print("You lose! :(")