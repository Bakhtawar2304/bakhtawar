print("DEBUG: Script started running")

import colorama
from colorama import Fore, Style
from textblob import TextBlob
import nltk

# Make sure TextBlob corpora are available
try:
    _ = TextBlob("test").sentiment
except LookupError:
    print("Downloading TextBlob corpora...")
    nltk.download("punkt")
    nltk.download("averaged_perceptron_tagger")
    nltk.download("brown")
    nltk.download("wordnet")
    nltk.download("movie_reviews")

# Initialize colorama for colored output
colorama.init(autoreset=True)

# Emojis for the start of the program
print(f"{Fore.CYAN}💥 Welcome to Sentiment Spy! 💥")

user_name = input(f"{Fore.MAGENTA}Please enter your name: ").strip()
if not user_name:
    user_name = "Mystery Agent"  # Fallback if user doesn't provide a name

# Store conversation as a list of tuples: (text, polarity, sentiment_type)
conversation_history = []

print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(f"Type a sentence and I will analyze it with TextBlob and show you the sentiment. 😊")
print(f"(Type {Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, "
      f"or {Fore.YELLOW}'exit'{Fore.CYAN} to quit.)\n")

while True:
    user_input = input(f"{Fore.GREEN}>> ").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.")
        continue

    # Check for commands
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE}💨 Exiting Sentiment Spy. Farewell, Agent {user_name}! 💫")
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}🗑 All conversation history cleared!")
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                # Choose color & emoji based on sentiment
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(f"{idx}. {color}{emoji} {text} "
                      f"(Polarity: {polarity:.2f}, {sentiment_type})")
        continue

    # Analyze sentiment
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    # Store in history
    conversation_history.append((user_input, polarity, sentiment_type))

    # Print result with color, emojis, and polarity
    print(f"{color}{emoji} {sentiment_type} sentiment detected! (Polarity: {polarity:.2f})")
