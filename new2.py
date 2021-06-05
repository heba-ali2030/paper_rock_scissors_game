# import random
# from typing import Match
# # check validity of user input
# def check_spelling(player1):
#     list= ['paper','scissors', 'rock']
#     while player1 not in list:
#         print('Ooh, Sorry, there is a mistake in your typing, try again!')
#         player1= input('please type Rock, paper or Scissors: \n ').casefold()

#     return player1

# # Number of times for playing the game:
# print (f'Hello, You can play as you want ^_^')

# run = 0
# while True: 
#     run += 1
    
#     print(f'It is the {run} run')

#     # ask each player to choose Rock, paper or scissors
#     player1 = check_spelling(input('please type Rock, paper or Scissors: \n ')).casefold()

#     hand_game = ['Rock', 'Paper' ,'Scissors']
#     player2 = random.choice(hand_game).casefold()
    
#     # the user and system are differrent:
#     # if player1 != player2:
#     #     print(f'you played {player1} and your compititor played a {player2}')

#         # 1- player plays rock
    

#     def result(player2):
#         match (player1, player2):
#             case ('rock' ,'scissors'):
#                 return(f'Congratulations, You are the winner ^_^, Rock crushes scissors\n')
            
#             case ('rock' , 'paper'):
#                 return (f'ooooops, You are the loser ^_^, Paper covers rock\n')

#         # 2- player plays paper
#             case ('paper', 'rock'):
#                 return (f'Congratulations, You are the winner ^_^, Paper covers rock\n')

#             case'scissors':
#                 return (f'Ooooops, You are the loser!, scissors cuts paper\n')

#         # 3- player plays scissor
       
#             case ('scissors','rock'):
#                 return (f'Ooooops, You are the loser !, Rock crushes scissors\n')

#             case ('scissors','paper'):
#                 return (f'Congratulations, You are the winner ^_^, scissors cuts paper\n')
#     result(player2)
        
#     # player and the system are the same
#     # else: 
#     #     print(f'Ooooooh ! You played the same {player1} as system, try again!\n')
    
    
#     # ask the user to complete to the next level or to exit and save level.
#     play_again= input(' Do you want to complete the game ? Type No  or N if yow want to exit: ').casefold()
#     if play_again == 'no' or play_again == 'n':
#         print('waiting to see you again !')
#         break
#     else:
#         pass

#     # to leaave space between runs:
#     print('     ')
    
code = 200
match code:
    case 404:
        print('ddd')
    case 200:
        print ('ssss')
