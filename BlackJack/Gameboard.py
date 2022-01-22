from time import sleep


class GameBoard:
    def __init__(self):
        pass

    @staticmethod
    def placeBet(bet, player):  # Lista joka sisältää mahdollisen virheilmoituksen
        errors = []
        if bet < 1:
            errors.append("The minimum bet is $1.")
            return errors
        elif bet > player.bank:  # Unsufficient funds
            errors.append("You do not have sufficient funds.")
            return errors
        else:
            return errors

    def startGame(self, player):  # Call this function at the beginning of each game.
        startingCommand = \
            input(
                "You are starting with " + str(player.bank) + "€." + " Would you like to play a hand? ").lower().strip()
        if startingCommand == "yes":
            while True:
                bet = int(input("Place your bet: "))
                result = self.placeBet(bet, player)
                if len(result) < 1:
                    return [True, bet]
                else:
                    print(result[0])
        else:
            return [False, 0]

    @staticmethod
    def dealCardsForPlayer(player, pakka, round):
        if round < 1:
            player.hand.extend(pakka.deal(2))
            print("You are dealt: " + ", ".join(player.hand))
            print("Your hand's value is", player.handValue())
        else:
            dealt = pakka.deal(1)
            player.hand.extend(dealt)
            sleep(1.5)
            print("You are dealt: " + ", ".join(dealt))
            print("You now have:", ", ".join(player.hand))
            print("Your hand's value is", player.handValue())

    @staticmethod
    def dealCardsForDealer(dealer, pakka, round):
        if round < 1:
            dealer.hand.extend(pakka.deal(2))
            sleep(1)
            print("The dealer is dealt: " + dealer.hand[0] + ", Unkown")
        else:
            print("The dealer has:", ", ".join(dealer.hand))
            dealt = pakka.deal(1)
            dealer.hand.extend(dealt)
            print("The dealer hits and is dealt: " + dealt[0])
            print("The dealer has:", ", ".join(dealer.hand))

    @staticmethod
    def winner(pelaaja, dealer, bet):
        if pelaaja.handValue() > dealer.handValue():
            if pelaaja.handValue() == 21:
                print("YOU HAVE A BLACKJACK! You win", pelaaja.bets(True, bet, isBlackJack=True) + "€.")
            else:
                print("You win", pelaaja.bets(True, bet) + "€!")
        elif pelaaja.handValue() == dealer.handValue():
            print("You tie. The bet is returned to you.")
        else:
            print("The dealer wins! You lose", pelaaja.bets(False, bet) + "€.")

    def resetCards(self, pelaaja, dealer, deck, round):
        pelaaja.clearHand()
        dealer.clearHand()
        self.dealCardsForPlayer(pelaaja, deck, round)
        self.dealCardsForDealer(dealer, deck, round)
