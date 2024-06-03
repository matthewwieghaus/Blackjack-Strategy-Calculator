def card_value(card):
    card_values = {'K': 10, 'Q': 10, 'J': 10, 'A': 11}
    try:
        if card in card_values:
            return card_values[card]
        return int(card)
    except ValueError:
        raise ValueError(f"Invalid card value: {card}")

def compute_total(player_values):
    total = sum(player_values)
    ace_count = player_values.count(11)
    while total > 21 and ace_count:
        total -= 10
        ace_count -= 1
    return total

def compute_totals(player_values):
    total = compute_total(player_values)
    soft_total = total
    if 11 in player_values:
        soft_total = total - 10 if total > 21 else total
    return total, soft_total

def should_split(pair_card, dealer_upcard):
    split_rules = {
        8: True,
        11: True,
        2: dealer_upcard in [2, 3, 4, 5, 6, 7],
        3: dealer_upcard in [2, 3, 4, 5, 6, 7],
        7: dealer_upcard in [2, 3, 4, 5, 6, 7],
        6: dealer_upcard in [2, 3, 4, 5, 6],
        9: dealer_upcard in [2, 3, 4, 5, 6, 8, 9]
    }
    return split_rules.get(pair_card, False)

def get_strategy(player_cards, dealer_card):
    player_values = [card_value(card) for card in player_cards]
    total, soft_total = compute_totals(player_values)
    dealer_upcard = card_value(dealer_card)

    # Check for pair splitting
    if len(player_values) == 2 and player_values[0] == player_values[1]:
        pair_card = player_values[0]
        if should_split(pair_card, dealer_upcard):
            return "Split"

    # Hard totals
    if total >= 17:
        return "Stand"
    if total >= 13 and dealer_upcard in [2, 3, 4, 5, 6]:
        return "Stand"
    if total == 12 and dealer_upcard in [4, 5, 6]:
        return "Stand"
    if total == 11:
        return "Double Down"
    if total == 10 and dealer_upcard in [2, 3, 4, 5, 6, 7, 8, 9]:
        return "Double Down"
    if total == 9 and dealer_upcard in [3, 4, 5, 6]:
        return "Double Down"

    # Soft totals (Aces)
    if 11 in player_values:
        if soft_total >= 8:
            return "Stand"
        if soft_total == 7 and dealer_upcard in [2, 7, 8]:
            return "Stand"
        if soft_total == 7 and dealer_upcard in [3, 4, 5, 6]:
            return "Double Down"
        if soft_total == 6 and dealer_upcard in [3, 4, 5, 6]:
            return "Double Down"
        return "Hit"

    return "Hit"

def main():
    while True:
        try:
            player_input = input("Enter your cards (separated by spaces, use K, Q, J, A for face cards): ")
            player_cards = player_input.split()
            if not all(card in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J', 'A'] for card in player_cards):
                raise ValueError("Invalid card input.")
            dealer_card = input("Enter the dealer's up card (use K, Q, J, A for face cards): ")
            if dealer_card not in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J', 'A']:
                raise ValueError("Invalid dealer card input.")
            
            player_values = [card_value(card) for card in player_cards]
            total_value = compute_total(player_values)
            print(f"Total value of your cards: {total_value}")
            strategy = get_strategy(player_cards, dealer_card)
            print(f"Recommended strategy: {strategy}")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter card values as integers or face cards (K, Q, J, A).")
        except KeyboardInterrupt:
            print("\nExiting the strategy calculator.")
            break

if __name__ == "__main__":
    main()
