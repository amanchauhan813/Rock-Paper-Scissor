
import random
lis=['rock','paper','scissor']


#print(rand)
while True:
    computer=random.choice(lis)
    person=input('Enter choice |Rock| |Paper| |Scissor|\n')
    if person == computer:
        print('Draw')
    elif person != computer:
        if (computer == 'rock' and person =='paper'):
            print('You Won')
        elif computer == 'paper' and person =='scissor':
            print('You Won')
        elif computer == 'scissor' and person =='rock':
            print('You Won')
        elif person == 'rock' and computer =='paper':
            print('You Lost')
        elif person == 'paper' and computer =='scissor':
            print('You Lost')
        elif person == 'scissor' and computer =='rock':
            print('You Lost')
        else:
            print('Invalid Input')
    play_again = input('Do you want to play again? (yes/no): ')
    if play_again.lower() != 'yes':
        break
