

class Player:
    def __init__(self, hand, chips) -> None:
        self.hand = hand
        self.chips = chips
        self.bet = 0
        self.blind = 0

    def start(self, hand):
        self.hand = hand
        if self.blind == 1:
            self.bet = 10
        elif self.blind == 2:
            self.bet = 20
        else:
            self.bet = 0

    def call(self, bet):
        self.bet = bet

    def check(self, bet):
        if self.bet == bet:
            pass

    def fold():
        pass

    def raisee(self, current_bet, desired_bet):
        if desired_bet > current_bet:
            self.bet = desired_bet
