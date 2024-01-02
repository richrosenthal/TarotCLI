import os
import random
from openai import OpenAI  # Updated import statement
from argparse import ArgumentParser

# Create an OpenAI client with the API key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
if not client.api_key:
    raise ValueError("The OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

def get_tarot_reading(question):
    # List of tarot cards
    tarot_cards = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
        "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
        "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
        "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
        "Judgement", "The World",
        "Ace of Wands", "Two of Wands", "Three of Wands", "Four of Wands", "Five of Wands",
        "Six of Wands", "Seven of Wands", "Eight of Wands", "Nine of Wands", "Ten of Wands",
        "Page of Wands", "Knight of Wands", "Queen of Wands", "King of Wands",
        "Ace of Cups", "Two of Cups", "Three of Cups", "Four of Cups", "Five of Cups",
        "Six of Cups", "Seven of Cups", "Eight of Cups", "Nine of Cups", "Ten of Cups",
        "Page of Cups", "Knight of Cups", "Queen of Cups", "King of Cups",
        "Ace of Swords", "Two of Swords", "Three of Swords", "Four of Swords", "Five of Swords",
        "Six of Swords", "Seven of Swords", "Eight of Swords", "Nine of Swords", "Ten of Swords",
        "Page of Swords", "Knight of Swords", "Queen of Swords", "King of Swords",
        "Ace of Pentacles", "Two of Pentacles", "Three of Pentacles", "Four of Pentacles", "Five of Pentacles",
        "Six of Pentacles", "Seven of Pentacles", "Eight of Pentacles", "Nine of Pentacles", "Ten of Pentacles",
        "Page of Pentacles", "Knight of Pentacles", "Queen of Pentacles", "King of Pentacles"1]  # Complete this list
    selected_cards = random.sample(tarot_cards, 3)

    # Creating a prompt for the OpenAI API
    prompt = f"Psychic Charlotte, using tarot cards, what does the future hold in regard to this question: '{question}'? The cards drawn are: {', '.join(selected_cards)}."

    # Sending a request to OpenAI using the client
    response = client.completions.create(
        model="text-davinci-003",  # Or the latest model you prefer
        prompt=prompt,
        max_tokens=150
    )

    return selected_cards, response.choices[0].text

if __name__ == "__main__":
    parser = ArgumentParser(description="Tarot Reading App")
    parser.add_argument("question", help="Your question for the tarot reading")
    args = parser.parse_args()

    selected_cards, reading = get_tarot_reading(args.question)
    print(f"Selected Cards: {', '.join(selected_cards)}")
    print(f"Psychic Charlotte says: {reading}")
