import random
# check validity of user input
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
    
    print(f'It is the {run} run')

    # ask each player to choose Rock, paper or scissors
    player1 = check_spelling(input('please type Rock, paper or Scissors: \n ')).casefold()

    hand_game = ['Rock', 'Paper' ,'Scissors']
    player2 = random.choice(hand_game).casefold()
    
    # the user and system are differrent:
    if player1 != player2:
        print(f'you played {player1} and your compititor played a {player2}')

        # 1- player plays rock
        if player1 == 'rock' and player2 == 'scissors':
            print(f'Congratulations, You are the winner ^_^, Rock crushes scissors\n')
            
        elif player1 == 'rock' and player2 == 'paper':
            print(f'ooooops, You are the loser ^_^, Paper covers rock\n')


        # 2- player plays paper
        elif player1 == 'paper' and player2 == 'rock':
            print(f'Congratulations, You are the winner ^_^, Paper covers rock\n')

        elif  player1 == 'paper' and player2 == 'scissors':
            print(f'Ooooops, You are the loser!, scissors cuts paper\n')


        # 3- player plays scissor
        elif player1 == 'scissors' and player2 == 'rock':
            print(f'Ooooops, You are the loser !, Rock crushes scissors\n')

        elif player1 == 'scissors' and player2 == 'paper':
            print(f'Congratulations, You are the winner ^_^, scissors cuts paper\n')
        
    # player and the system are the same
    else: 
        print(f'Ooooooh ! You played the same {player1} as system, try again!\n')
    
    
    # ask the user to complete to the next level or to exit and save level.
    play_again= input(' Do you want to complete the game ? Type No  or N if yow want to exit: ').casefold()
    if play_again == 'no' or play_again == 'n':
        print('waiting to see you again !')
        break
    else:
        pass

    # to leaave space between runs:
    print('     ')
    