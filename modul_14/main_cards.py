import random
from modul_14.compsre import CompareCards
from modul_14.casino import PythonCasino


class BlackJack:
    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.player = [random.choice(self.cards), random.choice(self.cards), ]
        self.computer = [random.choice(self.cards), random.choice(self.cards), ]
        self.die_or_win = [0, 0, 1000, 0]

    def game(self):
        print('Choose option:')
        print('1. Draw cards')
        print('2. Draw cards only to player')
        print('3. Draw cards only to computer')
        print('4 Russian rullet')
        print(f'Your cards: {sum(self.player)}')
        print(f'Computer cards: {sum(self.computer)}')

        choice = int(input('Your choice:'))
        while 1:
            compare_1 = CompareCards(player_list=self.player,
                                     computer_list=self.computer)

            if choice == 1:
                self.player.append(random.choice(self.cards))
                self.computer.append(random.choice(self.cards))
                if compare_1.compare_results():
                    break
            elif choice == 2:
                self.player.append(random.choice(self.cards))
                if compare_1.compare_results():
                    break
            elif choice == 3:
                self.computer.append(random.choice(self.cards))
                if compare_1.compare_results():
                    break
            elif choice == 4:
                self.player.append(random.choice(self.die_or_win))
                self.computer.append(random.choice(self.die_or_win))
                if compare_1.compare_results():
                    break
        print('Restart Option')
        restart_or_no = input('\nDo you want to restart or play another game: ')
        if restart_or_no == 'y':
            black = BlackJack()
            black.game()
        elif  restart_or_no == 'casino':
            casino = PythonCasino()
            choice_red = int(input('Red com choice:'))
            choice_black = int(input('Black com choice:'))
            casino.compare_combination(choice_red=choice_red,
                                       choice_black=choice_black)
        else:
            pass


black_crds = BlackJack()
black_crds.game()
def choose_game(chois):
    print('Game Option')
    print('1. BlackJack (J)')
    print('2. Casino(C)')
    # while 1:

        #
        # if chois = 'j':
        #     black_crds = BlackJack()
        #     black_crds.game()
        # elif:
        #
