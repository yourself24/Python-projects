#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################
from collections import namedtuple
# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you and the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face-down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import random
from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


# Card = namedtuple('Card', ['rank', 'suit'])


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        self.cards = []
        # self.cards.append((r, s) for r in RANKS for s in SUITE)
        for s in SUITE:
            for r in RANKS:
                self.cards.append((s, r))
        shuffle(self.cards)

    def split(self, start, finish):
        slicer = slice(start, finish)
        return self.cards[slicer]

    def __str__(self):
        return str(self.cards)

    def __len__(self):
        return len(self.cards)


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    cards = []

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return f"There are {len(self.cards)} cards left in this hand!"

    def add(self, addedCard):
        self.cards.extend(addedCard)

    def remove(self):
        return self.cards.pop()



class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_cards(self):
        card = self.hand.remove()
        print(f"Player {self.name} has played {card} \n ")
        return card

    def draw_war(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for i in range(3):
                war_cards.append(self.hand.remove())
            return war_cards

    def has_cards(self):
        return len(self.hand.cards) != 0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
print(SUITE)
print(RANKS)
deck1 = Deck()
print(deck1)
print(len(deck1))
start1 = 0
start2 = int(len(deck1) / 2)
print(start2)
hand1 = Hand(deck1.split(start1, start2))
hand2 = Hand(deck1.split(start2, len(deck1)))
player1 = Player("Yourself", hand1)
player2 = Player("Computer", hand2)
rounds = 0
war = 0
while player1.has_cards() and player2.has_cards():
    rounds += 1
    cards_on_table = []
    print(f"Round {rounds} is starting! \n")
    print(f"Player {player1.name} has {str(len(player1.hand.cards))} cards left")
    print(f"Player {player2.name} has {str(len(player2.hand.cards))} cards left")
    p1_card = player1.play_cards()
    p2_card = player2.play_cards()

    cards_on_table.append(p1_card)
    cards_on_table.append(p2_card)

    if p1_card[1] == p2_card[1]:
        print("WAR \n")
        war += 1
        cards_on_table.extend(player1.draw_war())
        cards_on_table.extend(player2.draw_war())
        p1_card = player1.play_cards()
        p2_card = player2.play_cards()
        if RANKS.index(p1_card[1]) > RANKS.index(p2_card[1]):
            player1.hand.add(cards_on_table)
        else:
            player2.hand.add(cards_on_table)

    else:
        if RANKS.index(p1_card[1]) > RANKS.index(p2_card[1]):
            print("Player's card is of higher rank! \n")
            player1.hand.add(cards_on_table)
        else:
            print("Computer's card is of higher rank! \n")
            player2.hand.add(cards_on_table)

if player1.has_cards():
    print("YOU WIN!")
else:
    print("COMPUTER WINS :((")

# Use the 3 classes along with some logic to play a game of war!
