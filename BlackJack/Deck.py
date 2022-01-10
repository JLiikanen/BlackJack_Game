import random


class Deck:  # Uusi pakka joka pelissä!
    def __init__(self):
        self.cards = []
        self.fillDeck()
        self.shuffle()

    def fillDeck(self):
        graphics = ["\u2666", "\u2665", "\u2663", "\u2660"]
        cards = [x for x in range(2, 11)]
        cards = cards + ["J", "Q", "K", "A"]
        for maa in graphics:
            for value in cards:
                self.cards.append(str(value) + maa)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):  # returns a list of dealt cards
        if n > len(self.cards):
            return self.cards
        else:
            dealtCards = []
            i = 0
            while i < n:
                dealtCards.append(self.cards.pop())
                i += 1
        return dealtCards

    def _dealBlackJack(self):
        return ["10T", "11T"]
