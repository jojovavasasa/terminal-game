import time
import random

print("Welkom bij het spel!")

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

players = int(input("Hoeveel spelers zijn er?: "))
lives = int(input("Hoeveel levens wil je hebben?: "))
rounds = int(input("Hoeveel rondes moet elke speler spelen?: "))
screw = int(input("Hoeveel vragen moet de 'screw' upgrade beantwoorden?: "))
helpline = int(input("Hoeveel antwoorden krijg je met de 'helpline' upgrade?: "))

if players <= 0:
    print("Je bent een beetje te alleen, probeer het opnieuw met meer spelers.")
    exit()
elif lives <= 0:
    print("Ben je al dood? probeer het opnieuw met meer levens.")
    exit()
elif rounds <= 0:  
    print("Amai, het spel is al gedaan, probeer het opnieuw met meer rondes.")
    exit()
elif screw <= 0:
    print("Het is de bedoeling als je de screw ability gebruikt, dat je gescrewd wordt, probeer het opnieuw met meer vragen voor de 'screw' upgrade.")
    exit()

upgrades = {"helpline", "pill", "skipper", "switcher", "screw"} 

# Vraag alleen om namen van spelers
player_names = {}
player_upgrades = {}

for i in range(1, players + 1):
    player_upgrades[f"player_{i}"] = random.choice(list(upgrades))
    name = input(f"Voer de naam in van speler {i}: ")
    if name.isnumeric():
        print("bro wat doe je nu?")
        exit()
    if name == "":
        print("oh hallo _ dat is een HEEL mooie naam")
        exit()  
    if name in player_names.values():
        print(f"De naam '{name}' is al in gebruik. De naam wordt aangepast naar 'Speler {i}'.")
        player_names[i] = f"Speler {i}"
    else:
        player_names[i] = name
    print("Jij krijgt...")
    time.sleep(1)
    print(f"Een {player_upgrades[f'player_{i}']} upgrade!")

# Initialize player scores and lives
player_lives = {player: lives for player in range(1, players + 1)}
player_scores = {player: 0 for player in range(1, players + 1)}

total_rounds = rounds * players

used_questions = []

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
    while question not in used_questions:
        question, correct_answer = random.choice(list(chosen_category.items()))
    used_questions.append(question)

    print(question)

    while True:
        user_answer = input("Jouw antwoord: ")

        if user_answer.strip().lower() == correct_answer.strip().lower():
            print("Correct!")
            player_scores[current_player_number] += 1
            break
        elif (
            player_upgrades[f"player_{current_player_number}"] is not None
            and user_answer.strip().lower() == player_upgrades[f"player_{current_player_number}"]
        ):
            if player_upgrades[f"player_{current_player_number}"] == "skipper":
                    print("Je hebt de 'skipper' upgrade gebruikt! Je mag deze beurt overslaan.")
                    player_upgrades[f"player_{current_player_number}"] = None
                    break
            elif player_upgrades[f"player_{current_player_number}"] == "switcher":
                    print("Je hebt de 'switcher' upgrade gebruikt! Een andere speler moet nu de beurt overnemen!")
                    other_player = random.choice([p for p in range(1, players + 1) if p != current_player_number])
                    print(f"Speler {player_names[other_player]} neemt de beurt over.")
                    # Kies alleen een andere speler die nog levens heeft
                    alive_players = [p for p in range(1, players + 1) if p != current_player_number and player_lives[p] > 0]
                    if not alive_players:
                        print("Er zijn geen andere spelers met levens over om de beurt over te nemen.")
                        break
            elif player_upgrades[f"player_{current_player_number}"] == "screw":
                    print("Je hebt de 'screw' upgrade gebruikt! Je mag een andere speler kiezen die 2 vragen moet beantwoorden!")
                    alive_players = [p for p in range(1, players + 1) if p != current_player_number and player_lives[p] > 0]
                    if not alive_players:
                        print("Er zijn geen andere spelers met levens over om te kiezen.")
                        break
                    if alive_players:
                        other_player = random.choice(alive_players)
                        other_player_name = player_names[other_player]
                        print(f"{other_player_name}, jij moet nu {screw} vragen beantwoorden!")
                        for _ in range(screw):
                            other_question, other_correct_answer = random.choice(list(chosen_category.items()))
                            print(other_question)
                            other_answer = input("Jouw antwoord: ")
                            if other_answer.strip().lower() == other_correct_answer.strip().lower():
                                print("Correct!")
                                player_scores[other_player] += 1
                            else:
                                player_lives[other_player] -= 1
                                if player_lives[other_player] <= 0:
                                    print(f"Fout! Het juiste antwoord is: {other_correct_answer}")
                                    print(f"Speler {other_player_name} heeft geen levens meer. Game over voor deze speler!")
                                    break
                                else:
                                    print(f"Fout! Het juiste antwoord is: {other_correct_answer}")
                                    print(f"Speler {other_player_name} heeft nog maar {player_lives[other_player]} levens over.")
            elif player_upgrades[f"player_{current_player_number}"] == "pill":
                print("Je hebt de 'pill' upgrade gebruikt! Nu wordt het spannend! Als je het antwoord fout hebt, verlies je een punt, maar als je het goed hebt, krijg je er 2!")
                player_upgrades[f"player_{current_player_number}"] = None
                pill_answer = input("Jouw antwoord: ")
                if pill_answer.strip().lower() == correct_answer.strip().lower():
                    print("Correct! Je krijgt 2 punten!")
                    player_scores[current_player_number] += 2
                else:
                    print(f"Fout! Het juiste antwoord is: {correct_answer}")
                    print("Je verliest 1 punt!")
                    player_scores[current_player_number] -= 1
                    player_lives[current_player_number] -= 1
                    if player_lives[current_player_number] <= 0:
                        print(f"Speler {current_player_name} heeft geen levens meer. Game over voor deze speler!")
                    else:
                        print(f"Speler {current_player_name} heeft nog maar {player_lives[current_player_number]} levens over.")
                break
            elif player_upgrades[f"player_{current_player_number}"] == "helpline":
                print("Je hebt de 'helpline' upgrade gebruikt! Je krijgt 3 antwoorden, waarvan er 1 correct is!")
                possible_answers = [correct_answer] #HEIR IERG
                for B in range(helpline =- 1):
                    possible_answers.append(random.choice(list(chosen_category.values())))
                random.shuffle(possible_answers)
                print("Mogelijke antwoorden:", possible_answers)
                user_answer = input("Kies het juiste antwoord: ")
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
            other_player = random.choice([p for p in range(1, players + 1) if p != current_player_number and player_lives[p] > 0])
            other_player_name = player_names[other_player]
            print(f"{other_player_name}, jij moet nu antwoorden!")
            other_answer = input("Jouw antwoord: ")
            if other_answer.strip().lower() == correct_answer.strip().lower():
                print("Correct!")
                player_scores[other_player] += 2
            else:
                player_scores[other_player] -= 1
                player_lives[other_player] -= 1
                if player_lives[other_player] <= 0:
                    print(f"Fout! Het juiste antwoord is: {correct_answer}")
                    print(f"Speler {other_player_name} heeft geen levens meer. Game over voor deze speler!")
                else:
                    print(f"Fout! Het juiste antwoord is: {correct_answer}")
                    print(f"Speler {other_player_name} heeft nog maar {player_lives[other_player]} levens over.")
                break
            player_upgrades[f"player_{current_player_number}"] = None
            break
        elif user_answer.strip().lower() in upgrades:
            print("Jij hebt die upgrade niet, probeer de vraag opnieuw.")
            continue
        else:
            player_lives[current_player_number] -= 1
            if player_lives[current_player_number] <= 0:
                print(f"Fout! Het juiste antwoord is: {correct_answer}")
                print(f"Speler {current_player_name} heeft geen levens meer. Game over voor deze speler!")
            else:
                print(f"Fout! Het juiste antwoord is: {correct_answer}")
                print(f"Speler {current_player_name} heeft nog maar {player_lives[current_player_number]} levens over.")
            break

print("\nEindscore:")
for player, score in player_scores.items():
    print(f"Speler {player_names[player]}: {score} punten en {player_lives[player]} levens over.")
winner = max(player_scores, key=player_scores.get)
print(f"\nDe winnaar is {player_names[winner]} met {player_scores[winner]} punten en {player_lives[winner]} levens over!")