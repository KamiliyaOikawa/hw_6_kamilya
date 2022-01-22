import random

door = ['goat', 'auto']


def choose_door(choises):
    choises == random.choice(choises)
    print('you did your choose')
    option = input('One of the door revealed, and it is not your prize'
                   'Do you what to change your avto')
    if option == 'n':
        if choises == 'auto':
            print('You win')
        elif choises == 'goat':
            print('You loose')
    elif option == 'y':
        print(f'Your original choises was {choises}')
        if choises == 'goat':
            choises == 'auto'
            print()


choose_door()
