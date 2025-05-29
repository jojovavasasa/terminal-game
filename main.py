import time
import random

players = int(input("Hoeveel spelers zijn er? (1-4): "))
if players in [1, 2, 3, 4]:
    pass
else:
    print("Ongeldig aantal spelers. Voer een getal in tussen 1 en 4.")
    exit()

lives = int(input("Hoeveel levens wil je hebben?: "))
rounds = int(input("Hoeveel rondes moet elke speler spelen?: "))

# Vraag alleen om namen van spelers
player_names = {}
for i in range(1, players + 1):
    name = input(f"Voer de naam in van speler {i}: ")
    player_names[i] = name

# Define categories with names
categories = {
    "Historisch Bewustzijn": {
        "Welk jaar is de tweede wereldoorlog gestopt?": "1945",
        "Wanneer begon de middeleeuwen?": "500",
        "Wie was de eerste president van de Verenigde Staten?": "George Washington",
        "In welk jaar viel de Berlijnse Muur?": "1989",
    },
    "Wiskunde": {
        "Wat is 2 + 2?": "4",
        "Hoeveel zijden heeft een kubus?": "6",
        "Wat is de oppervlakte van een kubus met een zijde van 3 cm?": "54cm²",
        "Wat is de vierkantswortel van 81?": "9",
        "Wat is 12 x 12?": "144",
    },
    "Nederlands": {
        "Hoe schrijf je het woord dat je uitspreekt als 'h œy s'?": "Huis",
        "Wat is de verleden tijd van 'lopen'?": "Liepen",
        "Wat is het meervoud van 'huis'?": "Huizen",
        "Hoe spel je het woord 'paraplu'?": "Paraplu",
    },
    "Engels": {
        "Wat is de Engelse vertaling van 'hond'?": "Dog",
        "Hoe zeg je 'dank je wel' in het Engels?": "Thank you",
        "Wat is de Engelse vertaling van 'kat'?": "Cat",
        "Hoe zeg je 'goedenavond' in het Engels?": "Good evening",
    },
    "Frans": {
        "Wat is de Franse vertaling van 'kat'?": "Chat",
        "Hoe zeg je 'goedemorgen' in het Frans?": "Bonjour",
        "Wat is de Franse vertaling van 'hond'?": "Chien",
        "Hoe zeg je 'tot ziens' in het Frans?": "Au revoir",
    },
    "Techniek": {
        "Hoe noemt het ding waarmee je hout snijdt?": "Zaag",
        "Wat doet een schroevendraaier?": "Draaien",
        "Wat is de eenheid van elektrische stroom?": "Ampère",
        "Hoe heet het gereedschap om een moer vast te draaien?": "Steeksleutel",
    },
    "Ruimtelijk Bewustzijn": {
        "Wat is de hoofdstad van België?": "Brussel",
        "Wat is de hoofdstad van Nederland?": "Amsterdam",
        "Welke zee is noord van belgië?": "Noordzee",
        "Welke planeet staat het dichtst bij de zon?": "Mercurius",
        "Wat is de grootste oceaan op aarde?": "Stille Oceaan",
    },
}

# Initialize player scores and lives
player_lives = {player: lives for player in range(1, players + 1)}
player_scores = {player: 0 for player in range(1, players + 1)}

total_rounds = rounds * players

for current_round in range(total_rounds):
    current_player_number = (current_round % players) + 1
    current_player_name = player_names[current_player_number]
    print(f"\nSpeler {current_player_name} is aan de beurt!")

    if player_lives[current_player_number] <= 0:
        print(f"Speler {current_player_name} heeft geen levens meer en slaat deze beurt over.")
        continue

    chosen_category_name, chosen_category = random.choice(list(categories.items()))
    print(f"Categorie: {chosen_category_name}")

    question, correct_answer = random.choice(list(chosen_category.items()))
    print(question)

    user_answer = input("Jouw antwoord: ")

    if user_answer.strip().lower() == correct_answer.strip().lower():
        print("Correct!")
        player_scores[current_player_number] += 1
    else:
        player_lives[current_player_number] -= 1
        if player_lives[current_player_number] <= 0:
            print(f"Fout! Het juiste antwoord is: {correct_answer}")
            print(f"Speler {current_player_name} heeft geen levens meer. Game over voor deze speler!")
        else:
            print(f"Fout! Het juiste antwoord is: {correct_answer}")
            print(f"Speler {current_player_name} heeft nog maar {player_lives[current_player_number]} levens over.")

print("\nEindscore:")
for player, score in player_scores.items():
    print(f"Speler {player_names[player]}: {score} punten en {player_lives[player]} levens over.")
winner = max(player_scores, key=player_scores.get)
print(f"\nDe winnaar is {player_names[winner]} met {player_scores[winner]} punten en {player_lives[winner]} levens over!")