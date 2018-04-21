from GoGame import GoGame
import sys
import pygame

game = GoGame(9)
print(game.to_string())

pygame.init()
boardSidelength = 800
size = [boardSidelength, boardSidelength]

gridSquareSize = boardSidelength / (game.boardSize+1)    # Size of each gridsquare
borderSize = gridSquareSize / 2     # Size of outer border
backgroundColor = pygame.Color(180, 130, 45)
gridLineColor = pygame.Color(86, 46, 14)
gridLineWidth = 2

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        # Handle Quit event
        if event.type == pygame.QUIT:
            sys.exit()

    # Draw board background
    screen.fill(backgroundColor)

    # Draw grid horizontal lines
    for y in range(0, game.boardSize+1):
        lineY = borderSize + y*gridSquareSize
        pygame.draw.line(screen, gridLineColor, [borderSize, lineY], [boardSidelength-borderSize, lineY], gridLineWidth)

    for x in range(0, game.boardSize+1):
        lineX = borderSize + x*gridSquareSize
        pygame.draw.line(screen, gridLineColor, [lineX, borderSize], [lineX, boardSidelength-borderSize], gridLineWidth)

    pygame.display.flip()