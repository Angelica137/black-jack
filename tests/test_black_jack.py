from operator import is_
from scripts.black_jack import *


def test_value_of_card_returns_10():
    assert value_of_card('K') == 10


def test_value_of_card_returns_4():
    assert value_of_card('4') == 4


def test_value_of_card_returns_1():
    assert value_of_card('A') == 1


def test_value_of_card_returns_10_for_J():
    assert value_of_card('J') == 10


def test_vlue_of_card_returns_Q():
    assert value_of_card('Q') == 10


def test_higher_card_K_10():
    assert higher_card('K', '10') == ('K', '10')


def test_higher_card_4_6():
    assert higher_card('4', '6') == '6'


def test_higher_card_K_A():
    assert higher_card('K', 'A') == 'K'


def test_value_of_ace_6_K():
    assert value_of_ace('6', 'K') == 1


def test_value_of_ace_7_3():
    assert value_of_ace('7', '3') == 11


def test_is_blackjack_A_K():
    assert is_blackjack('A', 'K') == True


def test_is_black_jack_10_9():
    assert is_blackjack('10', '9') == False


def test_can_split_pairs_Q_K():
    assert can_split_pairs('Q', 'K') == True
