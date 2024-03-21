class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

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
