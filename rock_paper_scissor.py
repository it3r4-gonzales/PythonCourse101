import random
list=['scissors','rock','paper']

computer_choice = random.choice(list)

user_choice = input('Do you want rock, paper,or scissor? \n')

if computer_choice == user_choice:
    print('Tie')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN')
else:
    print('You lose T.T Computer Wins it selected '+ computer_choice + ':)')