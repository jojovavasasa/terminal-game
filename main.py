import time
import random

# Define categories with names
categories = {
    "Geschiedenis": {"Welk jaar is de tweede wereldoorlog gestopt?": "1945"},
    "Wiskunde": {"Wat is 2 + 2?": "4"},
    "Nederlands": {"Wat is de betekenis van het woord 'huis'?": "Een gebouw waarin mensen wonen"},
}

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
    print(f"Fout! Het juiste antwoord is: {correct_answer}")