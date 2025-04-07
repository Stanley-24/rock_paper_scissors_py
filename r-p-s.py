from random import choice as game_choices
from time import sleep as delay

emojis = {'r': '🪨', 's': '✄', 'p': '📃'}
choices = ('r', 'p', 's')

print() #space
welcome_note = print("Hello player 1, welcome")

while True:
  #try:
    print() #space
    user_input = input("Rock, Scissors or Paper (r/s/p): ").lower()
    print() #space

    if user_input not in choices:
      print(f"Invalid input '{user_input}'")
      continue
    
    computer_choice = game_choices(choices)  
      
    print(f"You chose {emojis[user_input]}")
    print() #space
    print("Computer is choosing...")
    print() #space

    delay(1)
    print(f"Computer chose {emojis[computer_choice]}")
    print() #space
    if user_input == computer_choice:
      print("Tie") 
    elif (
      (user_input == 'r' and computer_choice == 's') 
      or (user_input == 's' and computer_choice == 'p') 
      or (user_input == 'p' and computer_choice == 'r')):
      print("You win, Congratulations you have just unlocked $1,300 apple card ")
      print() #space
    else:
      print() #space
      print("You lose")
      print() #space

    
    should_continue = input("Do you want to play again? (y/n)").lower()
    print() #space

    if should_continue == 'n':
      print("Thank you for playing")
      delay(1)
      print("Closing game....")
      delay(2)
      print("Game closed")
      break
  #except Exception as e:
  #  print("invalid input", e)