from tic_tac_toe.init import *
import logging

logger = logging.getLogger("MiniMax")


# player - X : 1 | O : -1
def alpha_beta_minimax_recursive(board, player, top_level, level, alpha, beta):

    logging.debug("Current level = {0}".format(level))

    # Check: situation, when we should return our value
    board.estimate_board()
    if level == top_level or abs(board.estimation) > WIN_PRICES[3] / 2 or board.turns == BOARD_SQUARE:
        return board.estimation

    choice = None
    for pos in NEW_POSITION:

        # Check: filled position | if it's free, fill it with the "player"
        if board.set_board_value(pos[0], pos[1], player) is False:
            continue

        logger.debug("Try to run alphabetaminimax with board={0};\n" +
                     "player = {1}; top_level = {2}; level = {3};" +
                     "alpha = {4}; beta = {5}".
                     format(board, -1 * player, top_level, level + 1, alpha, beta))

        # Recursive request
        estimation = alpha_beta_minimax_recursive(board,
                                                  -1 * player,
                                                  top_level,
                                                  level + 1,
                                                  alpha,
                                                  beta)
        # Set zero to checked position
        board.set_board_value(pos[0], pos[1], DEFAULTFILLVALUE)
        logger.debug("Estimate value = {0}".format(estimation))

        # Alpha - Beta
        if level % 2 == 0:
            # Maximization
            if estimation > alpha:
                alpha = estimation
                choice = pos
            if alpha > beta:
                logger.debug("[MAX] We are using alpha-beta. Alpha = {0}".format(alpha))
                return alpha
        else:
            # Minimization
            if estimation < beta:
                beta = estimation
            if alpha >= beta:
                logger.debug("[MIN] We are using alpha-beta. Beta = {0}".format(alpha))
                return beta

    if level % 2 == 0:
        # If level == 0 we should return best position for our algo
        if level == 0:
            return choice
        return alpha
    else:
        return beta
