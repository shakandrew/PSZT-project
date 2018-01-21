import logging
import logging.config
from tic_tac_toe.board import Board
from tic_tac_toe.player_obj import AI, User
from tic_tac_toe.init import *

logging.config.fileConfig("logs/logging.ini")
logger = logging.getLogger()


def test_all_possible_bots():
    counter = {1: 0, 2: 0, 0: 0}
    for i in range(9):
        for j in range(9):
            board = Board(BOARD_SIZE)
            first_player = AI(1, "first", i+1)
            second_player = AI(-1, "second", j+1)
            counter[play(first_player,second_player,board)] += 1

    print(counter)

def play(first_player, second_player, board):
    temp = 2
    while True:
        first_player.make_turn(board)
        temp = check_for_win(board, first_player)
        if temp != 2:
            return temp
        second_player.make_turn(board)
        temp = check_for_win(board, second_player)
        if temp != 2:
            return temp


def check_for_win(board, player):
    board.estimate_board()
    logger.info(board.board_str())
    if abs(board.estimation) >= WIN_PRICES[3] / 2:
        player.win_message()
        print("######################\n")
        return player.mode
    if board.turns == BOARD_SQUARE:
        logger.info("Draw")
        print("######################\n")
        return 0
    return 2


if __name__=="__main__":
    test_all_possible_bots()