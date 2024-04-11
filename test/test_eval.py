from os import path
import sys
sys.path.append(path.abspath('/home/kd/poker/'))
sys.path.append(path.abspath('/home/kd/poker/src'))

from src import evaluation
from src import card
Card = card.Card
Evaluation = evaluation.Evaluation
e = Evaluation()


def test_two_pair_ace():
    hand = [
        Card(5, 1),
        Card(5, 2),
        Card(4, 1),
        Card(4, 3),
        Card(8, 3),
        Card(9, 4),
        Card(1, 4),
    ]
    score = e.eval(hand)
    assert score == 50414
    
def test_two_pair_with_three_pairs():
    hand = [
        Card(9, 1),
        Card(9, 2),
        Card(4, 1),
        Card(8, 1),
        Card(8, 3),
        Card(1, 2),
        Card(1, 4),
    ]
    score = e.eval(hand)
    assert score == 140908
    
def test_high_card():
    hand = [
        Card(5, 1),
        Card(11, 2),
        Card(4, 1),
        Card(6, 3),
        Card(8, 3),
        Card(9, 4),
        Card(12, 4),
    ]
    score = e.eval(hand)
    assert score == 12


def test_high_card_ace():
    hand = [
        Card(5, 1),
        Card(11, 2),
        Card(4, 1),
        Card(6, 3),
        Card(8, 3),
        Card(9, 4),
        Card(1, 4),
    ]
    score = e.eval(hand)
    assert score == 14
    
def test_three_of_a_kind():
    hand = [
        Card(4, 3),
        Card(4, 2),
        Card(4, 1),
        Card(6, 3),
        Card(8, 3),
        Card(9, 4),
        Card(1, 4),
    ]
    assert e.eval(hand) == 4000014
    
def test_four_of_a_kind():
    hand = [
        Card(4, 3),
        Card(4, 2),
        Card(4, 1),
        Card(4, 4),
        Card(8, 3),
        Card(9, 4),
        Card(1, 4),
    ]
    assert e.eval(hand) == 4 * e.FOUR_OF_A_KIND_MULT + 14
    
def test_straight():
    hand = [
        Card(4, 3),
        Card(5, 2),
        Card(6, 1),
        Card(7, 4),
        Card(8, 3),
        Card(9, 4),
        Card(1, 4),
    ]
    assert e.eval(hand) == 9 * e.STRAIGHT_MULT
    
def test_straight_ace_high():
    hand = [
        Card(10, 3),
        Card(13, 2),
        Card(12, 1),
        Card(11, 4),
        Card(8, 3),
        Card(9, 4),
        Card(1, 4),
    ]
    assert e.eval(hand) == 14 * e.STRAIGHT_MULT
    
def test_straight_ace_low():
    hand = [
        Card(2, 3),
        Card(3, 2),
        Card(4, 1),
        Card(5, 4),
        Card(8, 3),
        Card(9, 4),
        Card(1, 4),
    ]
    assert e.eval(hand) == 5 * e.STRAIGHT_MULT
    
if __name__ == "__main__":
    test_high_card()
    test_high_card_ace()
    test_two_pair_ace()
    test_two_pair_with_three_pairs()
    test_three_of_a_kind()
    test_four_of_a_kind()
    test_straight()
    test_straight_ace_low()
    test_straight_ace_high()
    