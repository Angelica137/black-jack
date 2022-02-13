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
