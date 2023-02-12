# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
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

#Write your code below this line 👇

import random
computer  = random.choice(["rock", "paper", "scissors"])
human = input("Enter your choice (rock, paper, scissors): ").lower()


print(f"computer chose {computer} & you chose {human}")
if computer == human:
    print("It is a DRAW!")
elif (computer == "rock" and human == "scissors") or (computer == "scissors" and human == "paper") or (computer == "paper" and human == "rock"):
    print("You lose!")
else:
    print("You win!")

