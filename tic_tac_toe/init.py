# To use another dimensions change values below
BOARD_SIZE = 3
BOARD_SQUARE = BOARD_SIZE * BOARD_SIZE
WIN_PRICES = {3: 300, 2: 60, 1: 10, 0: 0}
NEW_POSITION = ((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2))
DEFAULTFILLVALUE = 0
ZEROVALUE = -1
CROSSVALUE = 1

BOARD_TEMPLATE = \
"""
 {0[0]} | {0[1]} | {0[2]}
--- --- ---
 {0[3]} | {0[4]} | {0[5]}
--- --- ---
 {0[6]} | {0[7]} | {0[8]}
"""
