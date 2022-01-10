# Make a func that check who wins the round when the dealer can no longer hit!!

class Player:
    def __init__(self):
        self.hand = []
        self.bank = 500

    def hasLost(self):
        if self.bank <= 0:
            return True
        else:
            return False

    def isbust(self):  # Check if player has over 21
        if self.handValue() > 21:
            return True
        else:
            return False

    def clearHand(self):
        self.hand.clear()

    def handValue(self):
        handContaisAce = False
        howManyAces = 0
        total = 0
        for card in self.hand:
            valueOfCard = card[0:(len(card) - 1)]
            if valueOfCard.isdigit():
                total += int(valueOfCard)
            else:
                if valueOfCard == "K" or valueOfCard == "Q" or valueOfCard == "J":
                    total += 10
                else:
                    howManyAces += 1
                    total += 11
                    handContaisAce = True

        if total > 21 and handContaisAce:
            for ace in range(howManyAces):
                total -= 10
                if total <= 21:
                    break
            return total
        else:
            return total

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
