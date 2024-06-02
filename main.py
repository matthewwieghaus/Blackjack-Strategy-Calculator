def card_value(card):
    if card in ['K', 'Q', 'J']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

def compute_total(player_values):
    total = sum(player_values)
    if 11 in player_values and total > 21:
        total -= 10
    return total

def compute_totals(player_values):
    total = sum(player_values)
    if 11 in player_values:
        return total, total - 10
    return total, total

def should_split(pair_card, dealer_upcard):
    if pair_card in [8, 11]:
        return True
    if pair_card in [2, 3, 7] and dealer_upcard in [2, 3, 4, 5, 6, 7]:
        return True
    if pair_card == 6 and dealer_upcard in [2, 3, 4, 5, 6]:
        return True
    if pair_card == 9 and dealer_upcard in [2, 3, 4, 5, 6, 8, 9]:
        return True
    return False

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
    elif total >= 13 and dealer_upcard in [2, 3, 4, 5, 6]:
        return "Stand"
    elif total == 12 and dealer_upcard in [4, 5, 6]:
        return "Stand"
    elif total == 11:
        return "Double Down"
    elif total == 10 and dealer_upcard in [2, 3, 4, 5, 6, 7, 8, 9]:
        return "Double Down"
    elif total == 9 and dealer_upcard in [3, 4, 5, 6]:
        return "Double Down"

    # Soft totals (Aces)
    if 11 in player_values:
        if soft_total >= 8:
            return "Stand"
        elif soft_total == 7 and dealer_upcard in [2, 7, 8]:
            return "Stand"
        elif soft_total == 7 and dealer_upcard in [3, 4, 5, 6]:
            return "Double Down"
        elif soft_total == 6 and dealer_upcard in [3, 4, 5, 6]:
            return "Double Down"
        else:
            return "Hit"

    return "Hit"

def main():
    while True:
        try:
            player_input = input("Enter your cards (separated by spaces, use K, Q, J, A for face cards): ")
            player_cards = player_input.split()
            dealer_card = input("Enter the dealer's up card (use K, Q, J, A for face cards): ")
            player_values = [card_value(card) for card in player_cards]
            total_value = compute_total(player_values)
            print(f"Total value of your cards: {total_value}")
            strategy = get_strategy(player_cards, dealer_card)
            print(f"Recommended strategy: {strategy}")
        except ValueError:
            print("Invalid input. Please enter card values as integers or face cards (K, Q, J, A).")
        except KeyboardInterrupt:
            print("\nExiting the strategy calculator.")
            break

if __name__ == "__main__":
    main()
