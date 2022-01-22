from Dealer import Dealer


class Player(Dealer):
    # The following methods are inherited from dealer class
    # isBust
    # handValue
    # clear hand

    def __init__(self):
        super().__init__()
        self.hand = []
        self.bank = 500

    def hasLost(self):
        if self.bank <= 0:
            return True
        else:
            return False

    def bets(self, didWon, bet, isBlackJack=False):
        if isBlackJack:
            self.bank += bet * 1.5
            return str(bet * 1.5)
        elif didWon:
            self.bank += bet
            return str(bet)
        else:
            self.bank -= bet
            return str(bet)
