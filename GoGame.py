class BoardSize:   # enum representing board sizes
    Small, Medium, Large = range(3)


class GoGame:
    board = []

    def __init__(self, boardSize):
        # Change BoardSize
        if boardSize == BoardSize.Small:
            numSquares = 9
        elif boardSize == BoardSize.Medium:
            numSquares = 13
        elif boardSize == BoardSize.Large:
            numSquares = 19
        else:
            numSquares = 19     # Default to large board

        self.numSquares = numSquares
        for y in range(0, numSquares):
            self.board.append([])
            for x in range(0, numSquares):
                self.board[y].append("e")

        self.isBlacksTurn = True

    def to_string(self):
        retStr = ""
        for x in range(0, self.numSquares):
            for y in range(0, self.numSquares):
                retStr += self.board[y][x]
            retStr += "\n"
        return retStr

    def place_stone(self, x, y, color):
        numStonesRemoved = 0   # -1 indicated invalid moved

        if not self.is_spot_in_board(x,y):
            return numStonesRemoved

        if self.board[y][x] != "e":     # if non-empty -> fail
            return numStonesRemoved

        if (color != "w") and (color != "b"):     # if invalid color -> fail
            return numStonesRemoved

        self.board[y][x] = color     # Provisionally add stone to board to build chains

        # Remove stones
        adjChains = []
        otherColor = "w" if color == "b" else "b"


        chain = []
        if self.is_spot_in_board(x, y + 1):
            if self.board[y + 1][x] == otherColor:
                self.build_chain(x, y + 1, otherColor, chain)
                adjChains.append(chain)
                chain = []
        if self.is_spot_in_board(x + 1, y):
            if self.board[y][x + 1] == otherColor:
                self.build_chain(x + 1, y, otherColor, chain)
                adjChains.append(chain)
                chain = []
        if self.is_spot_in_board(x, y - 1):
            if self.board[y - 1][x] == otherColor:
                self.build_chain(x, y - 1, otherColor, chain)
                adjChains.append(chain)
                chain = []
        if self.is_spot_in_board(x - 1, y):
            if self.board[y][x - 1] == otherColor:
                self.build_chain(x - 1, y, otherColor, chain)
                adjChains.append(chain)
                chain = []

        for chain in adjChains:
            if self.get_chain_liberties(chain) <= 0:
                for stone in chain:
                    numStonesRemoved += 1
                    self.remove_stone(stone)

        newChain = []
        self.build_chain(x, y, color, newChain)

        # Calculate liberties of chain created
        chainLiberties = self.get_chain_liberties(newChain)
        if chainLiberties <= 0:
            self.board[y][x] = "e"  # Remove prosionally added stone if chain created has no liberites
            return -1

        return numStonesRemoved

    def build_chain(self, x, y, chainColor, chain):
        if not self.is_spot_in_board(x,y):
            return

        stoneInChain = False
        for stone in chain:
            if stone.x == x and stone.y == y:
                stoneInChain = True
                break

        if stoneInChain:
            return
        else:
            chain.append(Stone(x,y,chainColor))
            if self.is_spot_in_board(x,y+1):
                if self.board[y+1][x] == chainColor:
                    self.build_chain(x,y+1,chainColor,chain)
            if self.is_spot_in_board(x+1,y):
                if self.board[y][x+1] == chainColor:
                    self.build_chain(x+1,y,chainColor,chain)
            if self.is_spot_in_board(x,y-1):
                if self.board[y-1][x] == chainColor:
                    self.build_chain(x,y-1,chainColor,chain)
            if self.is_spot_in_board(x-1,y):
                if self.board[y][x-1] == chainColor:
                    self.build_chain(x-1,y,chainColor,chain)

    def get_stone(self, x, y):
        if not self.is_spot_in_board(x,y):
            return None

        return Stone(x, y, self.board[y][x])

    def remove_stone(self,stone):
        if not self.is_spot_in_board(stone.x,stone.y):
            return None
        self.board[stone.y][stone.x] = "e"

    def play_on_square(self, x, y):
        numStonesRemoved = -1
        if self.isBlacksTurn:
            numStonesRemoved = self.place_stone(x,y,"b")
        else:
            numStonesRemoved = self.place_stone(x,y,"w")

        if numStonesRemoved >= 0:
            self.isBlacksTurn = not self.isBlacksTurn

    def is_spot_in_board(self, x, y):
        if x < 0 or x >= self.numSquares:     #if out of bounds -> fail
            return False
        if y < 0 or y >= self.numSquares:     #if out of bounds -> fail
            return False
        return True

    def get_stone_liberties(self, stone):
        numLiberties = 0
        x = stone.x
        y = stone.y

        if self.is_spot_in_board(x, y + 1):
            if self.board[y + 1][x] == "e":
                numLiberties += 1
        if self.is_spot_in_board(x + 1, y):
            if self.board[y][x + 1] == "e":
                numLiberties += 1
        if self.is_spot_in_board(x, y - 1):
            if self.board[y - 1][x] == "e":
                numLiberties += 1
        if self.is_spot_in_board(x - 1, y):
            if self.board[y][x - 1] == "e":
                numLiberties += 1

        return numLiberties

    def get_chain_liberties(self, chain):
        chainLiberties = 0
        for stone in chain:
            chainLiberties += self.get_stone_liberties(stone)
        return chainLiberties

class Stone:
    x = -1
    y = -1
    color = "e"

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


