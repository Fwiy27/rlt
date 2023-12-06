from colorama import Fore
import sys
from os import system
import time

def clear_screen():
    if sys.platform.startswith('win'):
        system('cls')
    else:
        system('clear')

class Spinner:
    def __init__(self):
        self.numbers = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35']

    def print_board(self, highlight=None, message=None):
        clear_screen()
        board = '-------------------------------------\n'
        board += '|'

        for i in range(0, len(self.numbers)):
            if i == highlight:
                color = Fore.YELLOW
            elif i == 0:
                color = Fore.GREEN
            elif i % 2 == 0:
                color = Fore.LIGHTBLACK_EX
            else:
                color = Fore.RED
            if i % 12 == 0 and i != 0:
                board += '\n|'
            board += (color + self.numbers[i] + Fore.RESET + '|')
        
        board += '\n-------------------------------------'
        if message:
            board += '\n' + message

        print(board)

    def revolve(self, stop=99, pause_time=.01, message=None):
        for i in range(0, 36):
            if i == stop + 1:
                break
            self.print_board(i, message=message)
            time.sleep(pause_time)

    def spin(self, stop, pause_time=.01, message=None):
        for i in range(0, 2):
            self.revolve(99, pause_time, message=message)
        self.revolve(stop, pause_time, message = message)
