from game_structures import *
import random

## Shuffle the cards.
def shuffle(deck):
	random.shuffle(deck)
	return deck

## Given a deck and two hands, deal 5 cards to each hand.
## The first hand (p1_hand) gets the first card, the second
## hand gets the next, and alternate until each hand has
## the right number of cards.
def deal(deck, p1_hand, p2_hand):
	for i in range(NUM_CARDS_IN_HAND):
		add_card_to_hand(p1_hand, pop_card(deck))  # Player 1 gets the card
		add_card_to_hand(p2_hand, pop_card(deck))  # Player 2 gets the card

# If the player has a card of the same suit as the lead_card, they
# must play a card of the same suit.
# If the player does not have a card of the same suit, they can
# play any card.
def hand_has_suit(hand, suit):
	current_node = get_first_card_in_hand(hand)
	while current_node is not None:
		card = get_card_from_node(current_node)
		if get_card_suit(card) == suit:
			return True
		current_node = get_next_card_node(current_node)
	return False

def is_legal_move(hand, lead_card, played_card):
	lead_suit = get_card_suit(lead_card)
	played_suit = get_card_suit(played_card)

	if hand_has_suit(hand, lead_suit):
		return played_suit == lead_suit # Player must play a card of the same suit as the lead card
	else:
		return True # Player can play any card if they don't have a card of the lead suit

def get_card_suit(card):
	return card[1]

def get_card_value(card):
	return card[-1]

## Return True if the followed card is not the same suit as the lead card,
##   unless the followed card is trump, and the lead card is NOT trump.
## If the cards are the same suit,
##   return True if the lead card is higher than the followed card
##   Return False if the lead card is lower than the followed card
def who_won(lead_card, followed_card, trump):
	lead_suit = get_card_suit(lead_card)
	followed_suit = get_card_suit(followed_card)

	lead_value = get_card_value(lead_card)
	followed_value = get_card_value(followed_card)

	# Return True if the followed card is not the same suit as the lead card
	if lead_suit != followed_suit:
		# unless the followed card is trump, and the lead card is NOT trump
		if followed_suit == trump and lead_suit != trump:
			return False
		else:
			return True

	# If the cards are the same suit
	else:
		# Return True if the lead card is higher than the followed card
		if lead_value > followed_value:
			return True
		# Return False if the lead card is lower than the followed card
		else:
			return False

# Given the player1 hand, play a card.
# Player 1 is always the computer.
# This function should choose a card from the hand,
# remove it from the hand, print out a message
# saying what card was played, and return the played card.
# I recommend beginning with choosing the card in a very simple
# manner: just remove/return the first card in the hand, regardless
# if it's a "good" card or not.
def take_player1_turn(hand, trump):
	# Get the first card from the hand
	first_card_node = get_first_card_in_hand(hand)

	# If the hand is empty, return None
	if first_card_node is None:
		return None # No cards in hand

	# Get the card from the node
	first_card = get_card_from_node(first_card_node)
	remove_card_from_hand(hand, first_card) # Remove the card from the hand

	# Print a message about the card that was played
	print("Player 1 played the card: {face} with {color} \n".format(face=first_card[0], color=first_card[2]))

	# Return the card that was played
	return first_card

# Given the player2 hand, play a card.
# Player 2 is always a human.
# This function should prompt the user to choose a card to play.
# It probably should print out the cards that are available to play.
# Once the human player chooses,
# remove it from the hand, print a message
# saying what card was played, and return the played card.
# This function does not have to enforce that a valid card is chosen.
def take_player2_turn(hand, trump):
	# Print the available cards in the player's hand
	print("Your are Player 2, here are your available cards:")
	print_hand(hand)  # Assuming this prints the cards in a readable format

	# Get the number of cards in the hand
	num_cards = get_num_cards_in_hand(hand)

	# Prompt the player to choose a card by index
	choice = -1
	while choice < 0 or choice >= num_cards:
		try:
			choice = int(input(f"Please choose a card to play (0 to {num_cards - 1}); trump is {trump}: "))
		except ValueError:
			print(f"Invalid choice. Please choose an index between 0 to {num_cards - 1}")
			continue  # Skip the rest of the loop and prompt again
		if choice < 0 or choice >= num_cards:
			print(f"Invalid choice. Please choose an index between 0 to {num_cards - 1}")

	# Get the selected card based on the index chosen
	selected_card = get_card_from_hand_at_index(hand, choice)
	if selected_card is None:
		return None  # Invalid choice

	# Remove the chosen card from the hand
	remove_card_from_hand(hand, selected_card)

	# Print a message about the card that was played
	print("Player 2 played: {face} with {color}".format(face=selected_card[0], color=selected_card[2]))

	# Return the card that was played
	return selected_card

# Take all the cards out of a given hand, and put them
# back into the deck.
def return_hand_to_deck(hand, deck):
	while not is_hand_empty(hand):
		card = get_card_from_hand(hand, 0)
		push_card_to_deck(deck, card)

def swap_card_with_next(hand, index):
	if index < 0 or index >= get_num_cards_in_hand(hand) - 1:
		return   # No need to swap if the index is invalid or if it's the last card

	current_node = get_first_card_in_hand(hand)
	for i in range(index):
		current_node = get_next_card_node(current_node)

	next_node = get_next_card_node(current_node)
	if next_node is None:
		return  # No next card to swap with

	# Swap the nodes in the linked list
	prev_node = get_prev_card_node(current_node)
	next_next_node = get_next_card_node(next_node)

	# Adjust links for the previous node
	if prev_node:
		set_next_card_node(prev_node, next_node)
	else:
		set_first_card_in_hand(hand, next_node)

	# Adjust links for the current and next nodes
	set_next_card_node(next_node, current_node)
	set_prev_card_node(next_node, prev_node)
	set_next_card_node(current_node, next_next_node)
	set_prev_card_node(current_node, next_node)

	if next_next_node:
		set_prev_card_node(next_next_node, current_node)

## Returns True if the value of this_card is greater than the value of that_card, accounting for trump
## True if this_card is trump and that_card is not
## True if this_card is the same suit of that_card, and the value of this_card is > than the value of that card
## True if that_card has a different suit than this_card
## True if that_card is None
def is_this_card_bigger_than_that_card(this_card, that_card, trump):
	# True if that_card is None
	if that_card is None:
		return True

	# Get suits and values for both cards
	this_suit = get_card_suit(this_card)
	that_suit = get_card_suit(that_card)
	this_value = get_card_value(this_card)
	that_value = get_card_value(that_card)

	# True if this_card is trump and that_card is not
	if this_suit == trump and that_suit != trump:
		return True

	if that_suit == trump and this_suit != trump:
		return False

	if this_suit == trump and that_suit == trump:
		return this_value > that_value

	# True if this_card is the same suit of that_card, and the value of this_card is > than the value of that card
	if this_suit == that_suit and this_value > that_value:
		return True

	# True if that_card has a different suit than this_card
	if this_suit != that_suit and this_suit != trump and that_suit != trump:
		return True

	return False

# Sort the given hand in descending order of power.
# For full credit, implement your own sort algorithm (a Bubble Sort is easy with the Swap!).
#
# The sort order should be: all cards of the given trump suit should
# be the "highest", and A high down to 9;
# The other suits can be in random order, but the card values must go
# from high to low.
def sort_hand(hand, trump):
	"""Sort the hand such that trump is first and everything else is in decreasing order"""
	num_cards = get_num_cards_in_hand(hand)
	for i in range(num_cards):
		current_card = get_card_from_hand_at_index(hand, i)
		next_card = get_card_from_hand_at_index(hand, i + 1)
		if not is_this_card_bigger_than_that_card(current_card, next_card, trump):
			swap_card_with_next(hand, i)
