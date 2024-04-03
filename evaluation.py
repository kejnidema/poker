from card import Card


class Evaluation:
    def __init__(self) -> None:
        return

    def high_card(self, cards: list[Card]):
        sortedCards = sorted(cards)
        if sortedCards[0].value == 1:
            return 13
        else:
            return sortedCards[-1].value

    def pair(self, cards: list[Card]):
        sortedCards = sorted(cards)
        values = [card.value for card in sortedCards]
        unique_values = set(values)

        score = 0
        for val in unique_values:
            isPair = values.count(val) == 2
            newScore = 1400 if val == 1 else 100 * val

            if isPair and newScore > score:
                score = newScore

        filteredCard = score / 100 if score / 100 != 14 else 1

        remainingCards = filter(lambda x: x.value != filteredCard, sortedCards)
        return score, list(remainingCards)

    def two_pair(self, cards: list[Card]):
        score1, remainingCards = self.pair(cards)
        score2, remainingCards = self.pair(remainingCards)
        return (100 * score1 + score2, remainingCards) if score1 > 0 and score2 > 0 else (0, cards)

    def three_of_a_kind(self, cards: list[Card]):
        sortedCards = sorted(cards)
        values = [card.value for card in sortedCards]
        unique_values = set(values)
        
        score = 0
        for val in unique_values:
            isTriple = values.count(val) == 3
            newScore = 1400 if val == 1 else 1000000 * val

            if isTriple and newScore > score:
                score = newScore
                
        filteredCard = score / 1000000 if score / 1000000 != 14 else 1

        remainingCards = filter(lambda x: x.value != filteredCard, sortedCards)
        return score, list(remainingCards)
    
    def straight(self, cards: list[Card]):
        pass
        
    
    def flush(self, cards: list[Card]):
        suites = [card.suite for card in cards]
        for suite in ['spade', 'heart', 'club', 'diamond']:
            isFlush = suites.count(suite) >= 5
            flushSuite = suite
        if isFlush:
            flushCards = sorted(list(filter(lambda x: x.suite == flushSuite, cards)))
            highCard = flushCards[-1].value if flushCards[-1].value > 1 else 14
            score = 10000000000 * highCard
        return (score, flushCards) if isFlush else (0, sorted(cards))
    
    def full_house(self, cards: list[Card]):
        pass
    
    def four_of_a_kind(self, cards: list[Card]):
        pass
    
    def straight_flush(self):
        pass
    
    def royal_flush(self):
        pass

    def eval(self, hand):
        pass

    def compare(self, hand1, hand2):
        pass
