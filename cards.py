from structs import Suit, BidSuit, Card, Bid

R2 = 0x0004
R3 = 0x0008
R4 = 0x0010
R5 = 0x0020
R6 = 0x0040
R7 = 0x0080
R8 = 0x0100
R9 = 0x0200
RT = 0x0400
RJ = 0x0800
RQ = 0x1000
RK = 0x2000
RA = 0x4000

holding_notation_table = [None, None, R2, R3, R4, R5, R6, R7, R8, R9, RT, RJ, RQ, RK, RA]

def to_holding_notation(cards: list[Card]):
    holding_representation = None
    for card in cards:
        if not holding_representation: holding_representation = holding_notation_table[card.rank]
        else: holding_representation |= holding_notation_table[card.rank]
    return holding_representation