from Spinner.spinner import Spinner
from Score.score import Score
from os import system
import sys
from colorama import Fore


def clear_screen():
    if sys.platform.startswith('win'):
        system('cls')
    else:
        system('clear')

class CLI:
    def __init__(self):
        self.s = Score()
        self.sp = Spinner()
        self.bet_amount = 250

    def run(self):
        max_money = self.s.get_money()
        while self.s.get_money() > 0:
            self.sp.print_board()
            print(f"{Fore.GREEN}Money: ${self.s.get_money()}")
            print(f"Bet Amount: ${self.bet_amount}{Fore.RESET}")
            command = input('Command: ')
            command_list = command.split(' ')
            match command_list[0]:
                case "help":
                    print("------------")
                    print(f"{Fore.GREEN}bet {{number}} {Fore.RESET}| 35x return")
                    print(f"{Fore.GREEN}bet {{color}} {Fore.RESET}| 2x return on red/black 35x return on green")
                    print(f"{Fore.GREEN}bet {{number}} {{amount}} {Fore.RESET}| 35x return")
                    print(f"{Fore.GREEN}bet {{color}} {{amount}} {Fore.RESET}| 2x return on red/black 35x return on green")
                    print(f"{Fore.GREEN}set {{number}}{Fore.RESET} | sets bet amount")
                    print(f"{Fore.RED} bet {{number/color}} all{Fore.RESET} | bet all money on color or number")
                    print(f"{Fore.RED} bet {{number/color}} half{Fore.RESET} | bet half of money on color or number")
                    input("Press Enter to Continue . . .")
                case "bet":
                    valid = True
                    # Make sure command is correct length
                    if len(command_list) not in [2, 3]:
                        valid = False
                        print('Invalid format, press enter to continue . . .', end="")
                        input()
                    # Extract bet (color or number)
                    if valid:
                        try:
                            bet = int(command_list[1])
                            if bet not in list(range(0, 36)):
                                valid = False
                                print('Invalid number, press enter to continue . . .', end ='')
                                input()
                        except:
                            if command_list[1].lower() in ['red', 'black', 'green']:
                                bet = command_list[1].lower()
                                valid = True
                            else:
                                valid = False
                                print('Invalid color, press enter to continue . . .', end='')
                                input()
                    # Extract bet amount
                    if valid:
                        if len(command_list) == 3:
                            if command_list[2].lower() == 'all':
                                bet_amount = self.s.get_money()
                            elif command_list[2].lower() == 'half':
                                bet_amount = int(self.s.get_money() / 2)
                            else:
                                try:
                                    bet_amount = max(min(self.s.get_money(), int(command_list[2])), 0)
                                except:
                                    bet_amount = self.bet_amount
  
                        else:
                            bet_amount = self.bet_amount
                    
                    if valid:
                        color = Fore.RED if bet == 'red' else Fore.BLACK if bet == 'black' else Fore.GREEN
                        message = f"Bet: {color}{bet}{Fore.RESET}\nAmount: {Fore.GREEN}${bet_amount}{Fore.RESET}"
                        info = self.s.spin(bet_amount, bet)
                        # Check for new max
                        if self.s.get_money() > max_money:
                            max_money = self.s.get_money()
                        if self.bet_amount > self.s.get_money():
                            self.bet_amount = int(self.s.get_money() / 20)
                        winning_number = info['winning_number']
                        self.sp.spin(winning_number, message=message, pause_time=.05)
                        self.sp.print_board(winning_number)
                        as_message = f"{Fore.GREEN}WON!{Fore.RESET}" if info['won'] else f'{Fore.RED}LOST{Fore.RESET}'
                        as_message += " | Press Enter to Continue . . ."
                        input(as_message)

                case "set":
                    if len(command_list) != 2:
                        print('Invalid format, press enter to continue . . .', end = '')
                        input()
                    else:
                        try:
                            self.bet_amount = max(min(self.s.get_money(), int(command_list[1])), 0)
                        except:
                            print('Not a number, press enter to continue . . .', end='')
                            input()
                case "clear":
                    clear_screen()
                    exit()
                case _:
                    print("Command not found, press enter to continue . . .", end = '')
                    input()
        clear_screen()
        print(f'{Fore.RED}Out of Money{Fore.RESET}')
        print(f'Max Money: {max_money}')
        input('Press Enter to Continue . . .')
        clear_screen()
            