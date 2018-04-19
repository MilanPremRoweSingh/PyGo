from GoGame import GoGame
import sys

game = GoGame(3)
print(game.to_string())

game.place_stone( 1, 2, "w")
game.place_stone( 2, 2, "b")
game.place_stone( 1, 3, "e")
game.place_stone( 3, 2, "w")
game.place_stone( 0, 0, "w")
game.place_stone( 1, 2, "w")

print(game.to_string())
