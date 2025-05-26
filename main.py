import time
from game import Game
from player import create_players, Player

players = int(input("Hoeveel spelers zijn er? (1-4): "))
if players in [1, 2, 3, 4]:
    pass
else:
    print("Ongeldig aantal spelers. Voer een getal in tussen 1 en 4.")
    exit()

lives = int(input("Hoeveel levens wil je hebben?: "))
rounds = int(input("Hoeveel rondes moet elke speler spelen?: "))

players_list = create_players(players)
for player in players_list:
    player.lives = lives

game = Game(players, lives, rounds, players_list)
game.play()