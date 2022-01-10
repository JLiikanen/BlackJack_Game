import BlackJack
from time import sleep


# Tee funktioille joku järkevä järjestys

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


def startGame(player):  # Call this function at the begginning of each game.
    startingCommand = \
        input("You are starting with " + str(player.bank) + "€." + " Would you like to play a hand? ").lower().strip()
    if startingCommand == "yes":
        while True:
            bet = int(input("Place your bet: "))
            result = placeBet(bet, player)
            if len(result) < 1:
                return [True, bet]
            else:
                print(result[0])
    else:
        return [False, 0]


def dealCardsForPlayer(player, pakka, round):
    if round < 1:
        player.hand.extend(pakka.deal(2))
        print("You are dealt: " + ", ".join(player.hand))
    else:
        dealt = pakka.deal(1)
        player.hand.extend(dealt)
        sleep(1.5)
        print("You are dealt: " + ", ".join(dealt))
        print("You now have: ", ", ".join(player.hand))


def dealCardsForDealer(dealer, pakka, round):
    if round < 1:
        dealer.hand.extend(pakka.deal(2))
        sleep(1)
        print("The dealer is dealt: " + dealer.hand[0] + ", Unkown")
    else:
        dealt = pakka.deal(1)
        dealer.hand.extend(dealt)
        print("The dealer hits and is dealt: " + dealt[0])
        print("The dealer has:", ", ".join(dealer.hand))


def winner(pelaaja, dealer, bet):
    if pelaaja.handValue() > dealer.handValue():
        if pelaaja.handValue() == 21:
            print("YOU HAD A BLACKJACK! You win", pelaaja.bets(True, bet, isBlackJack=True) + "€.")
        else:
            print("You win", pelaaja.bets(True, bet) + "€!")
    elif pelaaja.handValue() == dealer.handValue():
        print("You tie. The bet is returned to you.")
    else:
        print("The dealer wins! You lose", pelaaja.bets(False, bet) + "€.")


def main():
    pelaaja = BlackJack.Player()
    dealer = BlackJack.Dealer()
    continueTurn = True
    round = 0
    while not pelaaja.hasLost():
        startRound = startGame(pelaaja)
        if startRound[0]:  # Start the round
            bet = startRound[1]
            d = BlackJack.Deck()
            pelaaja.clearHand()
            dealCardsForPlayer(pelaaja, d, round)
            dealCardsForDealer(dealer, d, round)
            round += 1
            while True:  # Players turn
                sleep(0.5)
                command = input("Would you like to hit or stay? ").lower().strip()
                if command == "hit":
                    dealCardsForPlayer(pelaaja, d, round)
                    if pelaaja.isbust():
                        print("Your hand value is over 21 and you lose", str(bet) + "€. :(")
                        pelaaja.bank -= bet
                        continueTurn = False
                        break
                elif command == "stay":
                    break
                else:
                    print("That's not a valid option")

            while continueTurn:  # Dealer's turn
                if dealer.isbust():
                    sleep(2)
                    print("The dealer busts, you win", str(bet) + "€")
                    pelaaja.bank += bet
                    break
                elif dealer.shouldHit():
                    sleep(2)
                    dealCardsForDealer(dealer, d, round)
                else:
                    print(dealer.hand)
                    print("The dealer stays.")
                    sleep(2)
                    winner(pelaaja, dealer, bet)
                    break
        else:
            break
    if pelaaja.hasLost():
        sleep(2)
        print()
        print()
        print("You've ran out of money. Please restart this program to try again. Goodbye.")
    elif round == 0:
        pass
    else:
        print("You left the game with", str(pelaaja.bank) + "€")


main()
