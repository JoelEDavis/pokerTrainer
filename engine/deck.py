import random

class Deck:
    def __init__(self):
        self.cards = [(rank, suit) for rank in "23456789TJQKA" for suit in "SCDH"]
        random.shuffle(self.cards)

    def deal(self, num_cards):
        return [self.cards.pop() for _ in range num_cards]
