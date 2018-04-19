

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

    def place_stone(self, x, y, color):
        numStonesRemoved = -1   # -1 indicated invalid moved

        if x < 0 or x >= self.boardSize:     #if out of bounds -> fail
            return numStonesRemoved
        if y < 0 or y >= self.boardSize:     #if out of bounds -> fail
            return numStonesRemoved

        if self.board[y][x] != "e":     #if non-empty -> fail
            return numStonesRemoved

        if (color != "w") and (color != "b"):     #if invalid color -> fail
            return numStonesRemoved

        self.board[y][x] = color

        return numStonesRemoved
