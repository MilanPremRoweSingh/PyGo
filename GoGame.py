class BoardSize:   # enum representing board sizes
    Small, Medium, Large = range(3)


class GoGame:
    board = []

    def __init__(self, boardSize):
        # Change BoardSize
        numSquares = 9 if boardSize == BoardSize.Small else 0
        numSquares = 13 if boardSize == BoardSize.Medium else 0
        numSquares = 19 if boardSize == BoardSize.Large else 0

        self.numSquares = numSquares
        for y in range(0, numSquares):
            self.board.append([])
            for x in range(0, numSquares):
                self.board[y].append("e")

    def to_string(self):
        retStr = ""
        for x in range(0, self.numSquares):
            for y in range(0, self.numSquares):
                retStr += self.board[y][x]
            retStr += "\n"
        return retStr

    def place_stone(self, x, y, color):
        numStonesRemoved = -1   # -1 indicated invalid moved

        if x < 0 or x >= self.numSquares:     #if out of bounds -> fail
            return numStonesRemoved
        if y < 0 or y >= self.numSquares:     #if out of bounds -> fail
            return numStonesRemoved

        if self.board[y][x] != "e":     #if non-empty -> fail
            return numStonesRemoved

        if (color != "w") and (color != "b"):     #if invalid color -> fail
            return numStonesRemoved

        self.board[y][x] = color
        numStonesRemoved = 0;   #For now we do this, will come back after graphics implemented

        return numStonesRemoved

    def add_stone_to_chain(self, x, y, color, chain):
        stone = self.get_stone(x ,y)

        if stone is not None:
            if not stone in chain:
                chain.append(stone)

    def get_stone(self, x, y):
        if x < 0 or x >= self.numSquares:     #if out of bounds -> fail
            return None
        if y < 0 or y >= self.numSquares:     #if out of bounds -> fail
            return None

        return Stone(x, y, self.board[y][x])


class Stone:
    x = -1
    y = -1
    color = "e"

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


