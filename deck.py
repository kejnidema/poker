from card import Card
import numpy as np
from typing import List, Type
from player import Player


class Deck:
    def __init__(self) -> None:
        self.make_deck()
        self.shuffle()

    def make_deck(self):
        suites = ["spade", "heart", "club", "diamond"]
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        deck = []
        for s in suites:
            for v in values:
                deck.append(Card(s, v))
        self.deck = deck

    def shuffle(self):
        np.random.shuffle(self.deck)

    def deal_hands(self, players: List[type[Player]]):
        for player in players:
            card1, card2, *rest = self.deck
            self.deck = rest
            player.hand = [card1, card2]

    def deal_river(self):
        card1, card2, card3, _, *rest = self.deck
        self.deck = rest
        return [card1, card2, card3]

    def deal_turn(self):
        card1, _, *rest = self.deck
        self.deck = rest
        return card1

    def deal_flop(self):
        card1, _, *rest = self.deck
        self.deck = rest
        return card1

    def reset(self):
        self.deck = self.shuffle(self.make_deck())

    def __str__(self):
        self.card_string(self.deck)

    def card_string(self, cards: list[Card]):
        card_string = ""
        for card in cards:
            card_string += str(card)
        return card_string

    def print_cards(self, cards: list[Card]):
        print(self.card_string(cards))
