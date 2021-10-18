import random

def greeting(name):
    print("Hello !" , name)

#main program
input_name = input('Enter your name:\n')

greeting(input_name)

name1 = input('Enter your name:\n')
greeting(name1)
name2 = input('Enter your name:\n')
greeting(name2)

#Creating our addition function
def addition(a, b):
    return a+b

#main program
num1 = float(input('Enter your name:\n'))
num2 = float(input('Enter your name:\n'))

#calling our function
result = addition(num1,num2)
print(result)

#rolling dice game

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6) 
    return dice_total

def main():
    player1 = float(input('Enter your name:\n'))
    player2 = float(input('Enter your name:\n'))

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, 'rolled' ,roll1)
    print(player2, 'rolled' ,roll1)

    if roll1 > roll2:
        print(player1, "wins!")
    elif roll2 > roll1:
        print(player2, "wins!")
    else:
        print("TIE")
main()