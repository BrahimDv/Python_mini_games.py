import random

lst = ['rock', 'paper', 'scissors']
user_win = 0
computer_win = 0

while True:
    computer_pick = ''
    user_pick = input('enter rock/paper/scissors or q to quit..:_').lower()

    if user_pick == 'q':
        break
    elif user_pick not in lst:
        continue

    random_number = random.randint(0, 2)
    computer_pick = lst[random_number]

    if user_pick == 'rock' and computer_pick == 'scissors':
        print('computer chooses scissors..')
        print('Youuu woooon!!!')
        user_win += 1
    elif user_pick == 'scissors' and computer_pick == 'paper':
        print('computer chooses paper..')
        print('youuu wooon!!!')
        user_win += 1
    elif user_pick == 'paper' and computer_pick == 'rock':
        print('computer chooses rock..')
        print('youuu woon!!')
        user_win += 1
    elif computer_pick == 'rock' and user_pick == 'scissors':
        print('computer chooses rock..')
        print('you lost :(')
        computer_win += 1
    elif computer_pick == 'scissors' and user_pick == 'paper':
        print('computer chooses scissors..')
        print('you lost :(')
        computer_win += 1
    elif computer_pick == 'paper' and user_pick == 'rock':
        print('computer chooses paper..')
        print('you lost :(')
        computer_win += 1
    else:
        print('Draw result,Go again!!!')
        continue

print('You got ', user_win, 'wins and ', computer_win, 'loss')
