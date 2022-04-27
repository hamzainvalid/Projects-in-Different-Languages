from random import randint

points = 0
tries = 0
choice = ['rock', 'paper', 'scissor']
total_points = 0

def totalPoints():
    global total_points
    total_points += points

def playerChoice():
    global invalid_input
    global player_choice
    invalid_input = 0
    player_choice = 0
    if player == 'r' or player == 'rock':
        player_choice = choice[0]
    elif player == 'p' or player == 'paper':
        player_choice = choice[1]
    elif player == 's' or player == 'scissor':
        player_choice = choice[2]
    else:
        invalid_input = 1
        print('Please enter a valid input!')

def gameplay():
    global tries, points
    global player
    points = 0
    while tries < 7:
        player = input('Please input your choice: ')
        playerChoice()
        computer_choice = choice[randint(0,2)]
        if computer_choice == player_choice:
            print("It's a draw!")
        elif computer_choice == 'rock' and player_choice == 'paper':
            points+=1
            print('Congrats you won, the computer chose ', computer_choice)
        elif computer_choice == 'paper' and player_choice == 'scissor':
            points+=1
            print('Congrats you won, the computer chose ', computer_choice)
        elif computer_choice == 'scissor' and player_choice == 'rock':
            points+=1
            print('Congrats you won, the computer chose ', computer_choice)
        elif invalid_input == 1:
            continue
        else:
            print('Oops! You lost, the computer chose ', computer_choice)
        tries+=1
    totalPoints()
    print('Your total points are ', total_points)
    x = input('Do you wish to continue for another 7 rounds? "y/n"')
    if x == 'y' or x == 'yes':
        tries = 0
        gameplay()

gameplay()