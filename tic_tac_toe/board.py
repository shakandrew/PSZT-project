import logging
from tic_tac_toe.init import *

logger = logging.getLogger("Board")


class Board:
    def __init__(self, size):
        self.size = size
        self.table = self.generate_board()
        self.estimation = 0
        self.turns = 0
        self.mode = 1
        logging.debug(self.__str__())

    def generate_board(self):
        result = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(DEFAULTFILLVALUE)
            result.append(row)
        return result

    def set_board_value(self, x, y, value):
        if self.table[x][y] == 0:
            self.table[x][y] = value
            self.turns += 1
            return True
        elif value == DEFAULTFILLVALUE:
            self.table[x][y] = 0
            self.turns -= 1
        return False

    # Estimates the cost of the board
    # Writes estimated value to self.estimation and returns this value
    # + : positive x's | - : negative x's
    # - : positive o's | + : negative o's
    def estimate_board(self):
        self.estimation = 0

        # horizontal
        for i in range(self.size):
            line = []
            for j in range(self.size):
                line.append(self.table[i][j])
            self.estimation += Board.estimate_line(line)
        logging.debug("Estimation after horizontal check={0}".format(self.estimation))

        # vertical
        for i in range(self.size):
            line = []
            for j in range(self.size):
                line.append(self.table[j][i])
            self.estimation += Board.estimate_line(line)
        logging.debug("Estimation after vertical check={0}".format(self.estimation))

        # diagonal up
        line = []
        for i in range(self.size):
            line.append(self.table[i][i])
        self.estimation += Board.estimate_line(line)

        # diagonal down
        line = []
        for i in range(self.size):
            line.append(self.table[self.size - i - 1][i])
        self.estimation += Board.estimate_line(line)
        logging.debug("Estimation after all checks={0}".format(self.estimation))
        self.estimation *= self.mode
        return self.estimation

    @staticmethod
    def estimate_line(checklist):
        x = 0
        o = 0
        for elem in checklist:
            if elem == CROSSVALUE:
                x += 1
            if elem == ZEROVALUE:
                o += 1

        if x != 0 and o != 0:
            return 0
        if x > 0:
            return WIN_PRICES[x]
        else:
            return -WIN_PRICES[o]

    def __str__(self):
        return "Board status:\n\n" \
               "size = {}\n".format(self.size) + \
               "table = {}\n".format(table_list_to_table_str(self.table)) + \
               "estimation = {}\n".format(self.estimation) + \
               "turns = {}".format(self.turns)

    def board_str(self):
        return table_list_to_table_str(self.table)


# For correct table show
def table_list_to_table_str(table):
    table_str = []
    for pos in NEW_POSITION:
        table_str.append(value_to_sign(table[pos[0]][pos[1]]))
    return BOARD_TEMPLATE.format(table_str)


def value_to_sign(value):
    if value == 1:
        return 'X'
    if value == 0:
        return ' '
    if value == -1:
        return 'O'
