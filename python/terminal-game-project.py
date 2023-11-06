# Portfolio Project assigment from Codecademy.
# Build a basic terminal program of your choice for your friends and family of your choice.

#BlackJack Game

import random

#Function to create a deck of cards
def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck


# Function to calulate the value of a hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        rank = card['rank']
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            value += 11
            num_aces += 1
        else:
            value += int(rank)
    
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    
    return value

# Function to display of hand
def display_hand(hand):
    for card in hand:
        print("{} of {}". format(card['rank'], card['suit']))

# Main game logic
def play_blackjack():
    deck = create_deck()

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("Welcom to Blackjack!\n")

    print("Your Hand:")
    display_hand(player_hand)
    print("\n Yout current total is: {}\n".format(calculate_hand_value(player_hand)))

    #Player's turn 
    while calculate_hand_value(player_hand) < 21:
        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player_hand.append(deck.pop())
            print("\nYour hand:")
            display_hand(player_hand)
            print("\n Yout current total is: {}\n".format(calculate_hand_value(player_hand)))
        elif action == 'stand':
            break
        else:
            print("invalid input. Please enter 'hit' or 'stand'.")
    
    #Dealer's turn, if < 17 then must play.
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    
    print("\nDealer's hand:")
    display_hand(dealer_hand)
    print("\n Dealer's total is: {}\n".format(calculate_hand_value(dealer_hand)))

    #Determine Winner
    if calculate_hand_value(player_hand) > 21:
        print("You busted! Dealer wins.")
    elif calculate_hand_value(dealer_hand) > 21:
        print("Dealer busted! You win.")
    elif calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
        print("You win!")
    elif calculate_hand_value(player_hand) < calculate_hand_value(dealer_hand):
        print("Dealer wins.")
    else:
        print("It's a tie!")

# Start the game
play_blackjack()