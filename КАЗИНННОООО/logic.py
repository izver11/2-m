from random import randint
from decouple import config



number_list = randint(1, 10)
game_over = True
my_money = config('MY_MONEY', default = 1000, cast = int)


class Game:
    def input_money(self):
        while True:
            try:
                bet = int(input(f'Ur balance is {my_money}\nenter the sum of ur bet: '))
                if bet > my_money:
                    print('you do not have such a lot of money')
                elif bet <= 0:
                    print(' The negative number is not confirmable ')
                else:
                    return bet

            except ValueError:
                print('Unknown symbols, enter the correct numbers')

    def input_slot(self):
        global number_list
        while True:
            try:
                choosen_num = int(input('choose your number from 1 to 10: '))
                if 1 <= choosen_num <= 10:
                    return choosen_num
                else:
                    print('enter the number from 1 to 10')
            except ValueError:
                print('enter the correct number')


    def play_game(self):
        global my_money, game_over
        while my_money > 0 and game_over:
            bet_money = self.input_money()
            bet_slot = self.input_slot()

            if bet_slot == bet_money:
                win_money = bet_money * 2
                print(f"Congrat's {win_money}$")
                my_money -= bet_money
                my_money += win_money
            else:
                print(f"U loose")
                my_money -= bet_money



            if my_money != 0:
                while True:
                    contin = input(f'ur balance is {my_money} \nDo u wanna contin ur game? ').lower()
                    if contin == 'no':
                        print(f'ur balance is {my_money}\ngame over, good luck')
                        game_over = False
                        break

                    elif contin == 'yes':
                        break
                    else:
                        print('enter only YES/NO')

            else:
                print(f'ur balance is {my_money}\n YOU LOOSE!!!HI HI HI HA')
