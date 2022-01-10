class Dealer:
    def __init__(self):
        self.hand = []

    def isbust(self):  # Check if player has over 21
        if self.handValue() > 21:
            return True
        else:
            return False

    def handValue(self):  # Tehokkuuden lisääminen! Esim. tee niin että parametriksi laitetaan kortit, ja uusi kortti
        # lisätään ilmentymän totaliin, sen sijaan että iteroidaan koko lista joka kerta.
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

    def shouldHit(self):
        if self.handValue() >= 17:
            return False
        else:
            return True
