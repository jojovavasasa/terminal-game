import time
import random

lives = 3
rounds = 5

# Define categories with names
categories = {
    "Historisch Bewustzijn": {"Welk jaar is de tweede wereldoorlog gestopt?": "1945", "Wanneer begon de middeleeuwen?": "500"},
    "Wiskunde": {"Wat is 2 + 2?": "4", "Hoeveel zijden heeft een kubus?": "6", "Wat is de oppervlakte van een kubus met een zijde van 3 cm?": "54cm²"},
    "Nederlands": {"Hoe schrijf je het woord dat je uitspreekt als 'h œy s'?": "Huis", "Wat is de verleden tijd van 'lopen'?": "Liepen"},
    "Engels": {"Wat is de Engelse vertaling van 'hond'?": "Dog", "Hoe zeg je 'dank je wel' in het Engels?": "Thankyou"},
    "Frans": {"Wat is de Franse vertaling van 'kat'?": "Chat", "Hoe zeg je 'goedemorgen' in het Frans?": "Bonjour"},
    "Techniek": {"Hoe noemt het ding waarmee je hout snijdt?": "Zaag", "Wat doet een schroevendraaier?": "Draaien"},
    "Ruimtelijk Bewustzijn": {"Wat is de hoofdstad van België?": "Brussel", "Wat is de hoofdstad van Nederland?": "Amsterdam", "Welke zee is noord van belgië?": "Noordzee"},
}

for _ in range(rounds):
    # Choose a random category
    chosen_category_name, chosen_category = random.choice(list(categories.items()))
    print(f"Categorie: {chosen_category_name}")

    # Choose a random question from the chosen category
    question, correct_answer = random.choice(list(chosen_category.items()))
    print(question)

    # Ask the user for an answer
    user_answer = input("Jouw antwoord: ")

    # Check if the answer is correct
    if user_answer.strip().lower() == correct_answer.strip().lower():
        print("Correct!")
    else:
        if lives == 1:
            print("Je hebt geen levens meer over. Game over!")
            break
        else:
            lives -= 1
            print(f"Fout! Het juiste antwoord is: {correct_answer}")
            print(f"Je hebt nog maar {lives} levens over")
else:
    print("Je hebt alle rondes voltooid! Goed gedaan!")