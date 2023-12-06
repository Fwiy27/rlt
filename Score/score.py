import random

def get_winning_number() -> int:
    return random.randint(0, 35)

class Score:
    def __init__(self, money=5000):
        self.money = money

    # odd numbers are red, even numbers are black, 0 is green
    def spin(self, bet_amount, bet) -> dict:
        winning_number = get_winning_number()
        multiplier = 1
        won = False

        if isinstance(bet, str):
            match bet.lower():
                case "red":
                    if winning_number % 2 != 0:
                        won = True
                case "black":
                    if winning_number % 2 == 0:
                        won = True
                case "green":
                    if winning_number == 0:
                        won = True
        
        elif isinstance(bet, int):
            multiplier = 34
            if bet == winning_number:
                won = True

        if won:
            self.money += bet_amount * multiplier
        else:
            self.money -= bet_amount

        return {"won": won, "winning_number": winning_number}
    
    def get_money(self) -> int:
        return self.money