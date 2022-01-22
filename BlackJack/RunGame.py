import BlackJack
from time import sleep


def main():
    pelaaja = BlackJack.Player()
    dealer = BlackJack.Dealer()
    gameboard = BlackJack.GameBoard()

    continueTurnToDealer = True
    while not pelaaja.hasLost():
        round = 0
        startRound = gameboard.startGame(pelaaja)  # Check if player wants to play
        if startRound[0]:  # Starting the round
            bet = startRound[1]
            d = BlackJack.Deck()
            gameboard.resetCards(pelaaja, dealer, d, round)
            round += 1

            while True:  # Players turn
                sleep(0.5)
                command = input("Would you like to hit or stay? ").lower().strip()
                if command == "hit":
                    gameboard.dealCardsForPlayer(pelaaja, d, round)
                    if pelaaja.isbust():
                        print("Your hand value is over 21 and you lose", str(bet) + "€. :(")
                        pelaaja.bank -= bet
                        continueTurnToDealer = False
                        break
                elif command == "stay":
                    break
                else:
                    print("That's not a valid option")

            while continueTurnToDealer:  # Dealer's turn
                if dealer.isbust():
                    sleep(2)
                    if pelaaja.handValue() == 21:
                        print("The dealer busts and you have a BlackJack!, you win",
                              str(pelaaja.bets(True, bet, isBlackJack=True)) + "€")
                        break
                    else:
                        print("The dealer busts, and you win", str(bet) + "€!")
                        pelaaja.bank += bet
                        break
                elif dealer.shouldHit():
                    sleep(2)
                    gameboard.dealCardsForDealer(dealer, d, round)
                else:
                    print(dealer.hand)
                    print("The dealer stays.")
                    sleep(2)
                    gameboard.winner(pelaaja, dealer, bet)
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


if __name__ == "__main__":
    main()
