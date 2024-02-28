#IMPORTANDO A BIBLIOTECA RANDOM + FUNÇÃO RANDINT()
import random
random_choice = random.randint(0,2)
""" print("O computador escolheu o nº " + str(random_choice)) """

#BOOLEANO
""" gols_jogador1 = 5
gols_jogador2 = 3
booleano = gols_jogador1 > gols_jogador2
print(booleano) """

#if else
#EX1:
"""
number_of_scoops = random.randint(0,3)
print(number_of_scoops)
if(number_of_scoops == 0):
    print("You didn't want any ice cream?")
    print("We have a lot of flavors.")
elif(number_of_scoops == 1):
    print("A single scoop for you, coming up.")
elif(number_of_scoops == 2):
    print("Oh, two scoops for you!")
elif(number_of_scoops >= 3):
    print("Wow, that's a lot of scoops!")
else:
    print("I'm sorry I can't give you negative scoops.")
"""
#EX2: ROCK, PAPER, SCISSORS
winner = ''
if(random_choice == 0):
    computer_choice = 'rock'
elif(random_choice == 1):
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

print("O computador escolheu", computer_choice,".")
user_choice = input("rock, paper or scissors? ")
#print("Você escolheu", user_choice, "e o computador escolheu", computer_choice)
if(computer_choice == user_choice):
    winner = 'Tie'
elif(computer_choice == 'paper' and user_choice == 'rock'):
    winner = 'Computer'
elif(computer_choice == 'rock' and user_choice == 'scissors'):
    winner = 'Computer'
elif(computer_choice == 'scissors' and user_choice == 'paper'):
    winner = 'Computer'
else:
    winner = 'User'

print(winner)
