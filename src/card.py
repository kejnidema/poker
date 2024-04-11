from functools import total_ordering


@total_ordering
class Card:
    def __init__(self, value, suite):
        if value not in range(14):
            raise Exception("card value must be 1-13")
        if suite not in [1,2,3,4,"spade","heart","club","diamond"]:
            raise Exception("card suite must be 1,2,3,4 or spade, heart, club, diamond")
        self.value = value
        if suite == 1:
            suite = "spade"
        elif suite == 2:
            suite = "heart"
        elif suite == 3:
            suite = "club"
        elif suite == 4:
            suite = "diamond"
        self.suite = suite

    def suite_to_symbol(self):
        if self.suite == "spade":
            return "♠"
        elif self.suite == "heart":
            return "♥"
        elif self.suite == "club":
            return "♣"
        elif self.suite == "diamond":
            return "♦"
        else:
            return ""

    def value_to_card(self):
        if self.value == 11:
            return "J"
        elif self.value == 12:
            return "Q"
        elif self.value == 13:
            return "K"
        elif self.value == 1:
            return "A"
        else:
            return self.value

    def __str__(self):
        return f"{self.value_to_card()}{self.suite_to_symbol()} "

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __ne__(self, other) -> bool:
        return not self == other

    def __lt__(self, other) -> bool:
        return self.value < other.value
