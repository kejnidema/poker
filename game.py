from deck import Deck
from typing import List, Type

from player import Player


class Game:
    def __init__(self, deck: Deck, players: List[Type[Player]]) -> None:
        self.deck = deck
        self.players = players
        self.small_blind = 10
        self.big_blind = 20

    def deal(self):
        self.deck.deal_hands(self.players)
