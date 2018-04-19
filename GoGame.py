

class GoGame:
    boardSize = 0
    board = []

    def __init__(self, boardSize):
        self.boardSize = boardSize
        for y in range(0, boardSize):
            self.board.append([])
            for x in range(0, boardSize):
                self.board[y].append("e")

    def to_string(self):
        retStr = ""
        for x in range(0, self.boardSize):
            for y in range(0, self.boardSize):
                retStr += self.board[y][x]
            retStr += "\n"
        return retStr

    def place_stone(self, x, y):
        validMove = False



        return validMove