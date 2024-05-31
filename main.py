def get_strategy(player_cards, dealer_card):
    total = sum(player_cards)
    dealer_upcard = dealer_card

    # Check for pair splitting
    if len(player_cards) == 2 and player_cards[0] == player_cards[1]:
        pair_card = player_cards[0]
        if pair_card in [8, 11]:
            return "Split"
        elif pair_card in [2, 3, 7] and dealer_upcard in [2, 3, 4, 5, 6, 7]:
            return "Split"
        elif pair_card == 6 and dealer_upcard in [2, 3, 4, 5, 6]:
            return "Split"
        elif pair_card == 9 and dealer_upcard in [2, 3, 4, 5, 6, 8, 9]:
            return "Split"
        else:
            return get_strategy([pair_card * 2], dealer_card)
    
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
    else:
        return "Hit"

    # Soft totals (Aces)
    if 11 in player_cards:
        soft_total = total - 10
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

def main():
    while True:
        try:
            player_cards = list(map(int, input("Enter your cards (separated by spaces): ").split()))
            dealer_card = int(input("Enter the dealer's up card: "))
            strategy = get_strategy(player_cards, dealer_card)
            print(f"Recommended strategy: {strategy}")
        except ValueError:
            print("Invalid input. Please enter card values as integers.")
        except KeyboardInterrupt:
            print("\nExiting the strategy calculator.")
            break

if __name__ == "__main__":
    main()
