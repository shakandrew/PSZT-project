import logging
import logging.config
from tic_tac_toe.board import Board
from tic_tac_toe.player_obj import AI, User
from tic_tac_toe.init import *

logging.config.fileConfig("logs/logging.ini")
logger = logging.getLogger()


def main():
    run_this_game = None
    while run_this_game != 0:
        # set the game mode | user vs AI / AI vs AI
        run_this_game = None
        while run_this_game is None:
            run_this_game = communicate_with_user("welcome")

        if run_this_game == 1:
            print("######################\n")
            logger.info("Let's init first player")
            first_player = init_player(1, "First player")
            print("######################\n")
            logger.info("Let's init second player")
            second_player = init_player(-1, "Second player")
            board = Board(BOARD_SIZE)
            logger.info(board.board_str())
            print("######################\n")
            play(first_player, second_player, board)


# Anyone could be player
def init_player(mode, name):
    player_type = None
    while player_type is None or player_type > 2 or player_type < 0:
        player_type = communicate_with_user("player_type")
    if player_type == 1:
        return init_user(mode, name)
    else:
        return init_ai(mode, name)


def init_user(player_sign, name):
    return User(player_sign, name)


def init_ai(ai_mode, name):
    ai_difficulty = None
    while ai_difficulty is None or ai_difficulty > 9 or ai_difficulty < 1:
        ai_difficulty = communicate_with_user("difficulty")
    return AI(ai_mode, name, ai_difficulty)


def play(first_player, second_player, board):
    while True:
        first_player.make_turn(board)
        check_for_win(board, first_player)
        second_player.make_turn(board)
        check_for_win(board, second_player)


def check_for_win(board, player):
    board.estimate_board()
    logger.info(board.board_str())
    if abs(board.estimation) >= WIN_PRICES[3] / 2:
        player.win_message()
        print("######################\n")
        exit(0)
    if board.turns == BOARD_SQUARE:
        logger.info("Draw")
        print("######################\n")
        exit(0)


def communicate_with_user(request):
    try:
        logger.info(requests[request])
        result = int(input("Your choice: "))
        return result
    except TypeError as err:
        logger.error(err)
        return None


requests = {
    "welcome":
        """"
Hi. You have opened the program. Now you have to make a choice!

1) Start game
0) Exit
(just a number without brackets)   
        """,

    "player_type":
        """
Please, define type for current player:

1) Real person (you (I expect) )
2) AI
(just a number without brackets / crosses start first)
        """,

    "difficulty":
        """
Please, set the difficulty ( 1 - 9 "depth")
        """
}

if __name__ == "__main__":
    main()
