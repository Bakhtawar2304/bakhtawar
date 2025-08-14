import re
import random
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Destination & joke data
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# Normalize user input
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Travel recommendation
def recommend():
    print("\n" + Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print("\n" + Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = normalize_input(input(Fore.YELLOW + "You: "))

        if answer == "yes":
            print("\n" + Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!\n")
        elif answer == "no":
            print("\n" + Fore.RED + "TravelBot: Let's try another.\n")
            recommend()
        else:
            print("\n" + Fore.RED + "TravelBot: I’ll suggest again.\n")
            recommend()
    else:
        print("\n" + Fore.RED + "TravelBot: Sorry, I don't have that type of destination.\n")
        show_help()

# Packing tips
def packing_tips():
    print("\n" + Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))

    while True:
        print(Fore.CYAN + "TravelBot: How many days?")
        days = input(Fore.YELLOW + "You: ")
        if days.isdigit():
            days = int(days)
            break
        else:
            print(Fore.RED + "Please enter a valid number of days.\n")

    print("\n" + Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.\n")

# Tell a joke
def tell_joke():
    print("\n" + Fore.YELLOW + f"TravelBot: {random.choice(jokes)}\n")

# Show help
def show_help():
    print("\n" + Fore.MAGENTA + "I can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.GREEN + "- Type 'exit' or 'bye' to end.\n")

# Chat loop
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.\n")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"\nNice to meet you, {name}!\n")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print("\n" + Fore.CYAN + "TravelBot: Safe travels! Goodbye!\n")
            break
        else:
            print("\n" + Fore.RED + "TravelBot: Could you rephrase?\n")

# Run chatbot
if __name__ == "__main__":
    chat()
