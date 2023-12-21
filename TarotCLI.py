import random
import openai
from argparse import ArgumentParser

def get_tarot_reading(question):
    tarot_cards = ["The Fool", "The Magician", "The High Priestess", ...]  # Complete list of tarot cards
    selected_cards = random.sample(tarot_cards, 3)

    prompt = f"Hello! I am Psychic Charlotte. You asked: '{question}'. The cards drawn are: {', '.join(selected_cards)}. What do these cards mean in relation to the question?"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or the latest available model
        messages=[{"role": "system", "content": "You are a tarot card reader."}, 
                  {"role": "user", "content": prompt}]
    )
    
    return selected_cards, response.choices[0].message['content']

if __name__ == "__main__":
    parser = ArgumentParser(description="Tarot Reading App")
    parser.add_argument("question", help="Your question for the tarot reading")
    args = parser.parse_args()

    selected_cards, reading = get_tarot_reading(args.question)
    print(f"Selected Cards: {', '.join(selected_cards)}")
    print(f"Psychic Charlotte says: {reading}")
