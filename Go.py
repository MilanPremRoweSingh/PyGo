from GoGame import GoGame
from GoGame import BoardSize
from GoDisplay import GoDisplay
import sys
import pygame

game = GoGame(BoardSize.Large)
print(game.to_string())

gameDisplay = GoDisplay(game)

gameDisplay.start()