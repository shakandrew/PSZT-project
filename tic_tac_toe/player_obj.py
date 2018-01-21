import sys
import logging
from tic_tac_toe.board import Board
from tic_tac_toe.init import *
from tic_tac_toe.minimax import alpha_beta_minimax_recursive

logger = logging.getLogger("PlayerObj")


class Player:
    def __init__(self, mode, name):
        self.mode = mode
        self.name = name

    def win_message(self):
        logger.info(self.name + " won")

    def make_turn(self, board):
        raise NotImplementedError("Subclass must implement abstract method")


class AI(Player):
    # Type - 1 crosses | 0 - zeros
    def __init__(self, mode, name, depth):
        super().__init__(mode, name)
        self.depth = depth
        logger.info("Created AI with mode={0}, depth={1}".format(str(self.mode), str(self.depth)))

    def make_turn(self, board):
        logger.info(self.name + " turn :")
        pos = self.alpha_beta_minimax(board)
        board.set_board_value(pos[0], pos[1], self.mode)
        board.estimate_board()
        logger.info("######################\n")

    def alpha_beta_minimax(self, board):
        alpha = -sys.maxsize
        beta = sys.maxsize
        board.mode = self.mode
        ans = alpha_beta_minimax_recursive(
            board, self.mode, self.depth, 0, alpha, beta
        )
        board.mode = 1
        return ans


class User(Player):
    def __init__(self, mode, name):
        super().__init__(mode, name)

    def make_turn(self, board):
        logger.info(self.name + " turn :")
        while True:
            x = None
            y = None

            # Read X
            while type(x) is not int or x < 1 or x > 4:
                try:
                    x = int(input("Row: "))
                except ValueError as err:
                    logger.error(err)
                    x = None

            # Read Y
            while type(y) is not int or y < 1 or y > 4:
                try:
                    y = int(input("Column: "))
                except ValueError as err:
                    logger.error(err)
                    y = None

            # Check: If this pos is filled choose another one, if no fill it
            if board.set_board_value(x - 1, y - 1, self.mode):
                logger.info("######################\n")
                return
