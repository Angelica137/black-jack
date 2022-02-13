from scripts.black_jack import *


def test_value_of_card_returns_10():
    assert value_of_card('K') == 10


def test_value_of_card_returns_4():
    assert value_of_card('4') == 4


def test_value_of_card_returns_1():
    assert value_of_card('A') == 1
