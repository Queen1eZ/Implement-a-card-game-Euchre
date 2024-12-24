NUM_CARDS_IN_HAND = 5
NUM_CARDS_IN_DECK = 24

SUIT_CLUBS = 'Clubs'
SUIT_SPADES = 'Spades'
SUIT_HEARTS = 'Hearts'
SUIT_DIAMONDS = 'Diamonds'

JACK = 'Jack'
QUEEN = 'Queen'
KING = 'King'
ACE = 'Ace'
VAL_9 = '9'
VAL_10 = '10'

SUITS = [SUIT_CLUBS, SUIT_SPADES, SUIT_HEARTS, SUIT_DIAMONDS]
FACES = [JACK, QUEEN, KING, ACE]
NUMBERED = [VAL_9, VAL_10]
COLOR_BLACK = 'BLACK'
COLOR_RED = 'RED'

CARD_TO_VALUE_MAP = {
	VAL_9: 9,
	VAL_10: 10,
	JACK: 11,
	QUEEN: 12,
	KING: 13,
	ACE: 14
}

## card is a tuple of (name, suit, color, value)

## deck is a list structured as a stack

## card_node is a dict of {next_card, prev_card, payload}

## hand is a linked list, represented by a dict of {first_card, num_cards_in_hand}

# ----------------------------------------
#  Deck functions
# ---------------------------------------
#  Assume that the value of cards are:
#  Nine=9; Ten=10; Jack=11; and so on, up to Ace=14.
def create_card(card, suit):
	card_name = '{face} of {suit}'.format(face = card, suit = suit)
	card_color = COLOR_RED if suit in [SUIT_HEARTS, SUIT_DIAMONDS] else COLOR_BLACK
	return (card_name, suit, card_color, CARD_TO_VALUE_MAP[card])

# Creates the deck, initializing any fields necessary.
# Returns a deck.
def create_deck():
	deck = []
	for suit in SUITS:
		for card in FACES + NUMBERED:
			deck.append(create_card(card, suit))
	return deck

# Adds a card to the top of the deck.
# Returns the deck.
def push_card_to_deck(deck, card):
	deck.append(card)
	return deck

# Shows the top card, but does not remove it from the stack.
# Returns the top card.
def peek_card(deck):
	return deck[-1]

# Removes the top card from the deck and returns it.
# Returns to the top card in the deck.
def pop_card(deck):
	return deck.pop(-1)

# Determines if the deck is empty.
# Returns True if the Deck has any cards; False otherwise.
def is_deck_empty(deck):
	return len(deck) == 0

## Prints the provided deck
## Do a little more than just calling "print()"-- make it look nice!
def print_deck(deck):
	print("Show the deck:")
	for card in deck:
		print(card)

#----------------------------------------
# Hand functions
#----------------------------------------

## A Hand is a linked list, so we define Card_Nodes before
## defining the Hand

def create_card_node(card):
	return { 'payload': card,
			 'next': None,
			 'prev': None }

def get_next_card_node(card_node):
	return card_node['next']

def set_next_card_node(card_node_src, card_node_dest):
	card_node_src['next'] = card_node_dest

def get_prev_card_node(card_node):
	return card_node['prev']

def set_prev_card_node(card_node_src, card_node_dest):
	card_node_src['prev'] = card_node_dest

def get_card_from_node(card_node):
	return card_node['payload']

# Creates a Hand and initializes any necessary fields.
# Returns a new empty hand
def create_hand():
	return {'first_card': None,
			'num_cards_in_hand': 0}

def get_first_card_in_hand(hand):
	return hand['first_card']

def set_first_card_in_hand(hand, new_first_card_node):
	hand['first_card'] = new_first_card_node

def get_num_cards_in_hand(hand):
	return hand['num_cards_in_hand']

def increment_num_cards_in_hand(hand):
	hand['num_cards_in_hand'] += 1

def decrement_num_cards_in_hand(hand):
	hand['num_cards_in_hand'] -= 1

# Adds a card to the hand.
def add_card_to_hand(hand, card):
	new_node = create_card_node(card)
	new_node['next'] = get_first_card_in_hand(hand)
	if hand['num_cards_in_hand'] > 0:
		get_first_card_in_hand(hand)['prev'] = new_node
	hand['first_card'] = new_node
	hand['num_cards_in_hand'] += 1

# Removes a card from the hand via card value
# Returns the card (not a card_node) that was removed from the hand
# Returns None if the specified card is not in the hand
def remove_card_from_hand(hand, card):
	next_node = get_first_card_in_hand(hand)
	prev_node = None
	while next_node:
		if get_card_from_node(next_node) == card:
			if prev_node:
				set_next_card_node(prev_node, get_next_card_node(next_node))
			else:
				set_first_card_in_hand(hand, get_next_card_node(next_node))
			decrement_num_cards_in_hand(hand)
			return get_card_from_node(next_node)
		prev_node = next_node
		next_node = get_next_card_node(next_node)
	return None

# Removes a card from the hand via index
# Returns the card, not a card_node
# Returns None if index is < 0 or greater than the length of the hand/list.
def get_card_from_hand(hand, index):
	if index < 0 or index >= get_num_cards_in_hand(hand):
		return None

	next_node = get_first_card_in_hand(hand)
	pick_index = 0
	prev_node = None
	while next_node is not None:
		if next_node is not None:
			if pick_index == index:
				if prev_node:
					set_next_card_node(prev_node, get_next_card_node(next_node))
				else:
					set_first_card_in_hand(hand, get_next_card_node(next_node))
				decrement_num_cards_in_hand(hand)
				return get_card_from_node(next_node)
			pick_index += 1
			prev_node = next_node
			next_node = get_next_card_node(next_node)
	return None

# Returns the card in the hand at the specified index
# Returns the card, not a card_node
# Returns None if index is < 0 or greater than the length of the hand/list.
def get_card_from_hand_at_index(hand, index):
	if index < 0 or index >= get_num_cards_in_hand(hand):
		return None

	next_node = get_first_card_in_hand(hand)
	for i in range(index):
		next_node = get_next_card_node(next_node)
	if next_node is not None:
		return get_card_from_node(next_node)
	return None

def is_card_in_hand(hand, card):
	next_node = get_first_card_in_hand(hand)

	while next_node is not None:
		if get_card_from_node(next_node) == card:
			return True
		next_node = get_next_card_node(next_node)
	return False

# Determines if there are any cards in the hand.
# Return 0 if the hand is empty; 1 otherwise.
def is_hand_empty(hand):
	return hand['first_card'] is None ## Could also be num_cards_in_hand == 0

def print_card(card,index):
	print('{index}: {face} with {color}'.format(index=index, face = card[0], color = card[2]))

def print_hand(hand):
	print('====')
	cur_card_node = hand['first_card']
	index = 0
	while cur_card_node is not None:
		print_card(cur_card_node['payload'],index)
		cur_card_node = cur_card_node['next']
		index += 1
	print('====')
