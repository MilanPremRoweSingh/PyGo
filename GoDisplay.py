import pygame
import sys
import math
from GoGame import GoGame
from GoGame import Stone


class GoDisplay:
    def __init__(self, game):
        pygame.init()

        self.game = game
        self.boardSidelength = 800
        self.size = [self.boardSidelength, self.boardSidelength]
        self.gridSquareSize = math.floor(self.boardSidelength / (game.numSquares + 1))  # Size of each gridsquare
        self.borderSize = math.floor(self.gridSquareSize / 2) # Size of outer border

        self.backgroundColor = pygame.Color(180, 130, 45)

        self.gridLineColor = pygame.Color(86, 46, 14)
        self.gridLineWidth = 2

        self.stoneRadius = math.floor((self.gridSquareSize - self.gridSquareSize/5)/2)
        self.blackStoneColor = pygame.Color(0, 0, 0)
        self.whiteStoneColor = pygame.Color(255, 255, 255)

        self.screen = pygame.display.set_mode(self.size)

    def drawGrid(self):
        # Draw grid horizontal lines
        for y in range(0, self.game.numSquares + 1):
            lineY = self.borderSize + y * self.gridSquareSize
            pygame.draw.line(self.screen, self.gridLineColor, [self.borderSize, lineY], [self.boardSidelength - self.borderSize, lineY], self.gridLineWidth)

        # Draw grid vertical lines
        for x in range(0, self.game.numSquares + 1):
            lineX = self.borderSize + x * self.gridSquareSize
            pygame.draw.line(self.screen, self.gridLineColor, [lineX, self.borderSize],[lineX, self.boardSidelength - self.borderSize], self.gridLineWidth)

    def drawStone(self, x, y, color):
        xpos = math.floor(self.borderSize + self.gridSquareSize * (x + 0.5))
        ypos = math.floor(self.borderSize + self.gridSquareSize * (y + 0.5))
        pygame.draw.circle(self.screen, color, [xpos, ypos], self.stoneRadius)

    def drawStones(self):
        for y in range(0,self.game.numSquares):
            for x in range(0,self.game.numSquares):
                if self.game.get_stone(x,y).color == 'e':
                    pass
                elif self.game.get_stone(x,y).color == 'w':
                    self.drawStone(x, y, self.whiteStoneColor)
                elif self.game.get_stone(x,y).color == 'b':
                    self.drawStone(x, y, self.blackStoneColor)

    def start(self):
        while 1:
            for event in pygame.event.get():
                # Handle Quit event
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    gridx = math.floor((event.pos[0] - self.borderSize)/self.gridSquareSize)
                    gridy = math.floor((event.pos[1] - self.borderSize)/self.gridSquareSize)
                    self.game.play_on_square(gridx, gridy)

            # Draw board background
            self.screen.fill(self.backgroundColor)

            self.drawGrid()
            self.drawStones()

            pygame.display.flip()
