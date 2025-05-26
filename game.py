import random
from player import Player
from categories import categories

class Game:
    def __init__(self, players, lives, rounds, player_details):
        self.players = [
            Player(
                details["name"],
                details["birth_year"],
                details["likes_ice_cream"],
                lives
            ) for details in player_details.values()
        ]
        self.rounds = rounds
        self.total_rounds = rounds * len(self.players)
        self.categories = categories

    def play(self):
        for current_round in range(self.total_rounds):
            current_player = self.players[current_round % len(self.players)]
            print(f"\nSpeler {current_player.name} is aan de beurt!")
            if current_player.lives <= 0:
                print(f"Speler {current_player.name} heeft geen levens meer en slaat deze beurt over.")
                continue
            chosen_category_name, chosen_category = random.choice(list(self.categories.items()))
            print(f"Categorie: {chosen_category_name}")
            question, correct_answer = random.choice(list(chosen_category.items()))
            if "jaar" in question.lower() and current_player.birth_year:
                question = question.replace("jaar", f"jaar (je bent geboren in {current_player.birth_year})")
            if "ijs" in question.lower() and current_player.likes_ice_cream:
                question += " (Je houdt van ijs!)"
            print(question)
            user_answer = input("Jouw antwoord: ")
            if user_answer.strip().lower() == correct_answer.strip().lower():
                print("Correct!")
                current_player.add_score()
            else:
                current_player.lose_life()
                if current_player.lives <= 0:
                    print(f"Fout! Het juiste antwoord is: {correct_answer}")
                    print(f"Speler {current_player.name} heeft geen levens meer. Game over voor deze speler!")
                else:
                    print(f"Fout! Het juiste antwoord is: {correct_answer}")
                    print(f"Speler {current_player.name} heeft nog maar {current_player.lives} levens over.")
        self.show_results()

    def show_results(self):
        print("\nEindscore:")
        for player in self.players:
            print(f"Speler {player.name}: {player.score} punten en {player.lives} levens over.")
        winner = max(self.players, key=lambda p: p.score)
        print(f"\nDe winnaar is {winner.name} met {winner.score} punten en {winner.lives} levens over!")
