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

def help():
    print("------------")
    print(f"{Fore.GREEN}bet {{number}} {Fore.RESET}| 35x return")
    print(f"{Fore.GREEN}bet {{color}} {Fore.RESET}| 2x return on red/black 35x return on green")
    print(f"{Fore.GREEN}bet {{number}} {{amount}} {Fore.RESET}| 35x return")
    print(f"{Fore.GREEN}bet {{color}} {{amount}} {Fore.RESET}| 2x return on red/black 35x return on green")
    print(f"{Fore.GREEN}set {{number}}{Fore.RESET} | sets bet amount")
    print(f"{Fore.RED} bet {{number/color}} all{Fore.RESET} | bet all money on color or number")
    print(f"{Fore.RED} bet {{number/color}} half{Fore.RESET} | bet half of money on color or number")

def pause():
    input("Press Enter to Continue . . .")

def invalid(variable):
    input(f'Invalid {variable}, Press Enter to Continue . . .')

class CLI:
    def __init__(self):
        self.score = Score()
        self.spinner = Spinner()
        self.bet_amount = 250
    
    def print_status(self):
        print(f"{Fore.GREEN}Money: ${self.score.get_money()}")
        print(f"Bet Amount: ${self.bet_amount}{Fore.RESET}")

    def run(self):
        # Maximum money variable
        max_money = self.score.get_money()

        # Runs while player still has money
        while self.score.get_money() > 0:
            # Print board and status
            self.spinner.print_board()
            self.print_status()

            # Logic for commands
            command = input('Command: ').split(' ')

            match command[0]:
                # Help command shows all available commands
                case "help":
                    help()
                    pause()
                
                case "bet":
                    valid = True

                    # Make sure command is correct length
                    if len(command) not in [2, 3]:
                        valid = False
                        invalid('format')

                    # Extract bet (color or number)
                    if valid:
                        try:
                            bet = int(command[1])
                            if bet not in list(range(0, 36)):
                                valid = False
                                invalid('number')
                        except:
                            bet = command[1].lower()
                            if bet not in ['red', 'black', 'green']:
                                valid = False
                                invalid('color')

                    # Extract bet amount
                    if valid:
                        if len(command) == 3:
                            money = self.score.get_money()
                            amount = command[2]
                            try:
                                bet_amount = money if amount == 'all' \
                                    else int(money/2) if amount == 'half' \
                                    else min(max(int(amount), 0), money)
                            except:
                                valid = False
                                invalid('amount')
                        else:
                            bet_amount = self.bet_amount

                    # Run bet
                    if valid:
                        # Set Color
                        color = Fore.RED if bet == 'red' else Fore.BLACK if bet == 'black' else Fore.GREEN
                        # Set message
                        message = f"Bet: {color}{bet}{Fore.RESET}\nAmount: {Fore.GREEN}${bet_amount}{Fore.RESET}"
                        # Run bet on score
                        info = self.score.spin(bet_amount, bet)
                        # Check for new max
                        if self.score.get_money() > max_money:
                            max_money = self.score.get_money()
                        # Set new default bet amount
                        if self.bet_amount > self.score.get_money():
                            self.bet_amount = int(self.score.get_money() / 20)
                        # Run bet on spinner
                        self.spinner.spin(info['winning_number'], message=message, pause_time=.05)
                        # Stop board to display
                        self.spinner.print_board(info['winning_number'])
                        # Tell user win or lose
                        self.print_status()
                        as_message = f'{Fore.GREEN}WON!{Fore.RESET}' if info['won'] else f'{Fore.RED}LOST{Fore.RESET}'
                        as_message += ' | Press Enter to Continue . . .'
                        input(as_message)
                
                # Set default bet amount
                case "set":
                    # Check for length
                    if len(command) != 2:
                        invalid('format')
                    else:
                        # Set bet amount
                        try:
                            self.bet_amount = max(min(self.score.get_money(), int(command[1])), 0)
                        # Display error
                        except:
                            invalid('number')
                
                # Exit game
                case "clear":
                    clear_screen()
                    exit()

                # Command not found
                case _:
                    invalid('command')

        # After player is out of money
        clear_screen()
        print(f'{Fore.RED}Out of Money{Fore.RESET}')
        print(f'Max Money: {max_money}')
        input('Press Enter to Continue . . .')
        clear_screen()