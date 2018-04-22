from GoGame import GoGame
from GoGame import BoardSize
from GoDisplay import GoDisplay
import sys
import pygame

game = GoGame(BoardSize.Small)
game.place_stone(1, 1, "w")
print(game.to_string())


gameDisplay = GoDisplay(game)

gameDisplay.start()