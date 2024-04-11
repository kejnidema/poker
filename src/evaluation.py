from card import Card


class Evaluation:
    def __init__(self) -> None:
        self.PAIR_MULT = 100
        self.TWO_PAIR_MULT = 100**2
        self.THREE_OF_A_KIND_MULT = 100**3
        self.STRAIGHT_MULT = 100**4
        self.FLUSH_MULT = 100**5
        self.FULL_HOUSE_MULT = 100**6
        self.FOUR_OF_A_KIND_MULT = 100**7
        self.STRAIGHT_FLUSH_MULT = 100**8
        return

    def highCard(self, cards: list[Card]) -> tuple[list[Card], int]:
        sortedCards = sorted(cards)
        score = 14 if sortedCards[0].value == 1 else sortedCards[-1].value
        remainingCards = list(
            filter(lambda x: x.value != (1 if score == 14 else score), sortedCards)
        )
        return remainingCards, score

    def pair(self, cards: list[Card]) -> tuple[list[Card], int]:
        sortedCards = sorted(cards)
        values = [card.value for card in sortedCards]
        valueSet = set(values)

        score = 0
        filteredCard = 0

        for val in valueSet:
            isPair = values.count(val) == 2
            newScore = 14 if val == 1 else val

            if isPair and newScore > score:
                filteredCard = val
                score = newScore

        remainingCards = list(filter(lambda x: x.value != filteredCard, sortedCards))

        return remainingCards, score

    def twoPair(self, cards: list[Card])-> tuple[list[Card], int, int]:
        remainingCards, score1 = self.pair(cards)
        remainingCards, score2 = self.pair(remainingCards)
        return remainingCards, score1, score2

    def threeOfAKind(self, cards: list[Card]) -> tuple[list[Card], int]:
        sortedCards = sorted(cards)
        values = [card.value for card in sortedCards]
        valueSet = set(values)

        score = 0
        filteredCard = 0

        for val in valueSet:
            isTriple = values.count(val) == 3
            newScore = 14 if val == 1 else val

            if isTriple and newScore > score:
                filteredCard = val
                score = newScore

        remainingCards = list(filter(lambda x: x.value != filteredCard, sortedCards))
        return remainingCards, score

    def straight(self, cards: list[Card]) -> tuple[list[Card], int]:
        sortedCards = sorted(cards)
        valueSet = set([card.value for card in sortedCards])

        highest_straight = set((10, 11, 12, 13, 1))
        if highest_straight.issubset(valueSet):
            straightCards = list(
                filter(lambda x: x.value in highest_straight, sortedCards)
            )
            score = 14
            return straightCards, score

        score = 0
        for val in valueSet:
            straight = set((val, val + 1, val + 2, val + 3, val + 4))
            newScore = val + 4
            if val < 10 and straight.issubset(valueSet) and newScore > score:
                straightCards = list(filter(lambda x: x.value in straight, sortedCards))
                score = newScore

        return straightCards if score > 0 else sortedCards, score

    def flush(self, cards: list[Card]) -> tuple[list[Card], int]:
        suites = [card.suite for card in cards]
        isFlush = False
        flushSuite = ""
        for suite in ["spade", "heart", "club", "diamond"]:
            count = suites.count(suite)
            isFlush = True if count >= 5 else isFlush
            flushSuite = suite if count >= 5 else flushSuite

        if isFlush:
            flushCards = sorted(list(filter(lambda x: x.suite == flushSuite, cards)))
            score = 14 if flushCards[0].value == 1 else flushCards[-1].value

        return (flushCards, score) if isFlush else (sorted(cards), 0)

    def fullHouse(self, cards: list[Card]) -> tuple[list[Card], int, int]:
        remainingCards, score1 = self.threeOfAKind(cards)
        remainingCards, score2 = self.pair(cards)
        return remainingCards, score1, score2

    def fourOfAKind(self, cards: list[Card]) -> tuple[list[Card], int]:
        sortedCards = sorted(cards)
        values = [card.value for card in sortedCards]
        unique_values = set(values)

        score = 0
        filteredCard = 0

        for val in unique_values:
            isTriple = values.count(val) == 4
            newScore = 14 if val == 1 else val

            if isTriple and newScore > score:
                filteredCard = val
                score = newScore

        remainingCards = list(filter(lambda x: x.value != filteredCard, sortedCards))
        return remainingCards, score

    def straightFlush(self, cards: list[Card]) -> tuple[list[Card], int]:
        remainingCards, score1 = self.flush(cards)
        remainingCards, score2 = self.straight(remainingCards)
        if score1 > 0 and score2 > 0:
            return remainingCards, score2
        else:
            return sorted(cards), 0

    def eval(self, cards: list[Card]) -> int:
        straightFlushHand, score = self.straightFlush(cards)
        if score > 0:
            return score * self.STRAIGHT_FLUSH_MULT

        remainingHand, score = self.fourOfAKind(cards)
        if score > 0:
            return score * self.FOUR_OF_A_KIND_MULT + self.highCard(remainingHand)[1]

        remainingHand, score1, score2 = self.fullHouse(cards)
        if score1 > 0 and score2 > 0:
            return score1 * self.FULL_HOUSE_MULT + score2 * self.FULL_HOUSE_MULT / 100
        
        flushHand, score = self.flush(cards)
        if score > 0:
            return score * self.FLUSH_MULT
        
        straightHand, score = self.straight(cards)
        if score > 0:
            return score * self.STRAIGHT_MULT
        
        remainingHand, score = self.threeOfAKind(cards)
        if score > 0:
            return score * self.THREE_OF_A_KIND_MULT + self.highCard(remainingHand)[1]
        
        score1 = 0
        score2 = 0
        remainingHand, score1, score2 = self.twoPair(cards)
        if score1 > 0 and score2 > 0:
            return score1 * self.TWO_PAIR_MULT + score2 * self.PAIR_MULT + self.highCard(remainingHand)[1]
        
        remainingHand, score = self.pair(cards)
        if score > 0:
            return score * self.PAIR_MULT + self.highCard(remainingHand)[1]
        
        return self.highCard(cards)[1]

    def compare(self, hand1: list[Card], hand2: list[Card]):
        pass
