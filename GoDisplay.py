import pygame
import sys


class GoDisplay:
    def __init__(self, game):
        pygame.init()

        self.game = game
        self.boardSidelength = 800
        self.size = [self.boardSidelength, self.boardSidelength]
        self.gridSquareSize = self.boardSidelength / (game.numSquares + 1)  # Size of each gridsquare
        self.borderSize = self.gridSquareSize / 2  # Size of outer border
        self.backgroundColor = pygame.Color(180, 130, 45)
        self.gridLineColor = pygame.Color(86, 46, 14)
        self.gridLineWidth = 2

        self.screen = pygame.display.set_mode(self.size)

    def drawGrid(self):
        # Draw grid horizontal lines
        for y in range(0, self.game.numSquares + 1):
            lineY = self.borderSize + y * self.gridSquareSize
            pygame.draw.line(self.screen, self.gridLineColor, [self.borderSize, lineY],
                             [self.boardSidelength - self.borderSize, lineY], self.gridLineWidth)

        # Draw grid vertical lines
        for x in range(0, self.game.numSquares + 1):
            lineX = self.borderSize + x * self.gridSquareSize
            pygame.draw.line(self.screen, self.gridLineColor, [lineX, self.borderSize],
                             [lineX, self.boardSidelength - self.borderSize], self.gridLineWidth)

    def start(self):
        while 1:
            for event in pygame.event.get():
                # Handle Quit event
                if event.type == pygame.QUIT:
                    sys.exit()

            # Draw board background
            self.screen.fill(self.backgroundColor)

            self.drawGrid()

            pygame.display.flip()
