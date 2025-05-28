from enum import Enum

class Suit(Enum):
    CLUBS = 3
    DIAMONDS = 2
    HEARTS = 1
    SPADES = 0

class BidSuit(Enum):
    PASS = 5
    CLUBS = 3
    DIAMONDS = 2
    HEARTS = 1
    SPADES = 0
    NOTRUMP = 4
    DOUBLE = 7
    REDOUBLE = 8

class Card():
    suit: Suit
    rank: int

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return str(self.rank) + self.suit.name
    
    def __lt__(self, other):
        if self.suit.value == other.suit.value:
            return self.rank < other.rank
        else: return self.suit.value < other.suit.value
    
    def __eq__(self, value):
        return self.suit == value.suit and self.rank == value.rank

class Bid():
    suit: BidSuit
    rank: int

    def __init__(self, suit, rank):
        assert suit == BidSuit.PASS or (rank >= 0 and rank <= 7), "Invalid bid rank!"
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return str(self.rank) + self.suit.name
    
    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit.value < other.suit.value
        else: return self.rank < other.rank

    def __eq__(self, value):
        return self.suit == value.suit and self.rank == value.rank