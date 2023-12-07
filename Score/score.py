import random

# Gets a winning number 0-35
def get_winning_number() -> int:
    return random.randint(0, 35)

class Score:
    def __init__(self, money=5000):
        self.money = money

    # Odd numbers are red, even numbers are black, 0 is green
    def spin(self, bet_amount, bet) -> dict:
        winning_number = get_winning_number()
        multiplier = 1
        won = False

        # If bet is a string check color
        if isinstance(bet, str):
            match bet.lower():
                case "red":
                    if winning_number % 2 != 0 and winning_number != 35:
                        won = True
                case "black":
                    if winning_number % 2 == 0 and winning_number != 0:
                        won = True
                case "green":
                    if winning_number in [0, 35]:
                        multiplier = 17
                        won = True
        
        # If bet is a number check number
        elif isinstance(bet, int):
            if bet in [0, 35]:
                multiplier = 17
                won = True if winning_number in [0, 35] else False
            elif bet == winning_number:
                multiplier = 35
                won = True

        # If user wins increase money
        if won:
            self.money += bet_amount * multiplier
        # If user loses reduce money
        else:
            self.money -= bet_amount

        # Return array of game information
        return {"won": won, "winning_number": winning_number}
    
    # Function to check money
    def get_money(self) -> int:
        return self.money