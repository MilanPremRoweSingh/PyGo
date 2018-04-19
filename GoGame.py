

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

        #Detech any formed enclosed areas
        connected = True
        chain = []
        toVisit = [stone(x, y, color)]

        for curr in toVisit:
            pass

        self.board[y][x] = color

        return numStonesRemoved

    def add_stone_to_chain(self, x, y, color, chain):
        stone = self.get_stone(x ,y)

        if stone is not None:
            if not stone in chain:
                chain.append(stone)


    def get_stone(self, x, y):
        if x < 0 or x >= self.boardSize:     #if out of bounds -> fail
            return None
        if y < 0 or y >= self.boardSize:     #if out of bounds -> fail
            return None

        return stone(x, y, self.board[y][x])


class stone:
    x = -1
    y = -1
    color = "e"

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color