def value_of_card(card: str) -> int:
    """
    Returns the numeric value of a card.
    Cards Jack, Queen and K return 10
    Ace returns 1
    """
    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    if card == 'A':
        return 1
    return int(card)


def higher_card(card_one: str, card_two: str) -> str:
    """
    Returns the highest value card, if both are the same
    value, both are returned
    """
    letters = ['J', 'Q', 'K', 'A']
    if card_one in letters:
        card_one_value = value_of_card(card_one)
    else:
        card_one_value = int(card_one)
    if card_two in letters:
        card_two_value = value_of_card(card_two)
    else:
        card_two_value = int(card_two)
    if card_one_value > card_two_value:
        return card_one
    if card_one_value < card_two_value:
        return card_two
    return card_one, card_two
