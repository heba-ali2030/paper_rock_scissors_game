
import random
# check valisity of user input
def check_spelling(player1):
    list= ['paper','scissors', 'rock']
    while player1 not in list:
        print('Ooh, Sorry, there is a mistake in your typing, try again!')
        player1= input('please type Rock, paper or Scissors: \n ').casefold()

    return player1

# Number of times for playing the game:
print (f'Hello, You can play as you want ^_^')

run = 0
while True: 
    run += 1
    
    # tell the user about turns

    print(f'It is the {run} run')

    # ask each player to choose Rock, paper or scissors
    player1 = check_spelling(input('please type Rock, paper or Scissors: \n ')).casefold()

    hand_game = ['Rock', 'Paper' ,'Scissors']
    player2 = random.choice(hand_game).casefold()
    
    # the user and system are differrent:
    if player1 != player2:
        print(f'you played {player1} and your compititor played a {player2}')

        # 1- player plays rock
        if player1 == 'rock':
            if player2 == 'scissors':
                print(f'Congratulations, You are the winner ^_^, Rock crushes scissors')
            
            # elif player2 == 'paper':
            else:
                print(f'ooooops, You are the loser ^_^, Paper covers rock')

        # 2- player plays paper
        elif player1 == 'paper':
            if player2 == 'rock':
               print(f'Congratulations, You are the winner ^_^, Paper covers rock')

            # elif player2 == 'scissors':
            else:
               print(f'Ooooops, You are the loser!, scissors cuts paper')

        # 3- player plays scissor

        elif player1 == 'scissors':
            if player2 == 'rock':
                print(f'Ooooops, You are the loser !, Rock crushes scissors')

            # elif  player2 == 'paper':
            else:
                print(f'Congratulations, You are the winner ^_^, scissors cuts paper')
        
    # player and the system are the same
    else: 
        print(f'Ooooooh ! You played the same {player1} as system, try again!')

    # to leaave space between runs:
    print('     ')
    





