import logging
import logging.config
from tic_tac_toe.board import Board
from tic_tac_toe.player_obj import AI, User
from tic_tac_toe.init import *

logging.config.fileConfig("logs/logging.ini")
logger = logging.getLogger()

WIN3 = (100, 200, 300)
WIN2 = (20, 30, 40, 50, 60)
WIN1 = (5, 10, 15)


def test_all_possible_bots():
    file = open("res.txt", "w")
    for i1 in WIN3:
        for i2 in WIN2:
            for i3 in WIN1:
                WIN_PRICES[3] = i1
                WIN_PRICES[2] = i2
                WIN_PRICES[1] = i3
                counter = {1: 0, 2: 0, 0: 0}
                for i in range(9):
                    for j in range(9):
                        board = Board(BOARD_SIZE)
                        first_player = AI(1, "first", i + 1)
                        second_player = AI(-1, "second", j + 1)
                        counter[play(first_player, second_player, board)] += 1
                file.write(
                    "For WIN3={0} WIN2={1} WIN3={2} results look like this ".format(i1, i2, i3) + str(counter) + "\n")


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


if __name__ == "__main__":
    test_all_possible_bots()
