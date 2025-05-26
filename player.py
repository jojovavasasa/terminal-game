class Player:
    def __init__(self, name, birth_year, likes_ice_cream, lives):
        self.name = name
        self.birth_year = birth_year
        self.likes_ice_cream = likes_ice_cream
        self.lives = lives
        self.score = 0

    def lose_life(self):
        self.lives -= 1

    def add_score(self):
        self.score += 1


def create_players(num_players):
    players = []
    for i in range(1, num_players + 1):
        name = input(f"Voer de naam in van speler {i}: ")
        birth_year = input(f"In welk jaar ben je geboren, {name}?: ")
        likes_ice_cream = input(f"Hou je van ijs, {name}? (ja/nee): ")
        player = Player(
            name=name,
            birth_year=birth_year,
            likes_ice_cream=likes_ice_cream.lower() == "ja",
            lives=None  # Placeholder, to be set later
        )
        players.append(player)
    return players
