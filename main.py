import time
import random

questions = ["Geschiedenis", "Wiskunde", "Nederlands"]

Geschiedenis = {"Welk jaar is de tweede wereldoorlog gestopt?": "1945",}
Wiskunde = {"Wat is 2 + 2?": "4",}
Nederlands = {"Wat is de betekenis van het woord 'huis'?": "Een gebouw waarin mensen wonen",}

categories = {"Geschiedenis": Geschiedenis, "Wiskunde": Wiskunde, "Nederlands": Nederlands}

# Kies een willekeurige categorie
gekozen_categorie = random.choice(questions)
print(f"Categorie: {gekozen_categorie}")

# Kies een willekeurige vraag uit de gekozen categorie
vraag, correct_antwoord = random.choice(list(categories[gekozen_categorie].items()))
print(vraag)

# Vraag de gebruiker om een antwoord
gebruiker_antwoord = input("Jouw antwoord: ")

# Controleer of het antwoord correct is
if gebruiker_antwoord.strip().lower() == correct_antwoord.strip().lower():
    print("Correct!")
else:
    print(f"Fout! Het juiste antwoord is: {correct_antwoord}")