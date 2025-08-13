# Import necessary libraries
# - TextBlob for natural language processing tasks like sentiment analysis
# - Colorama for colored terminal output
# - sys and time for animations and delays

# Initialize Colorama to reset terminal colors automatically after each output

# Define global variables
# - `user_name`: To store the name of the user (Agent)
# - `conversation_history`: A list to store all user inputs
# - Sentiment counters (`positive_count`, `negative_count`, `neutral_count`) to track sentiment trends

# Define a function to simulate a processing animation
# - Prints "loading dots" to make the chatbot feel interactive
# - Use a loop to display three dots with a slight delay

# Define a function to analyze sentiment of the text
# - Use TextBlob to calculate the polarity of the input text
# - Categorize the sentiment into "Very Positive," "Positive," "Neutral," "Negative," or "Very Negative"
# - Append the user input to `conversation_history`
# - Update the sentiment counters based on the category
# - Handle exceptions to avoid crashes

# Define a function to handle commands
# - Handle commands like `summary`, `reset`, `history`, and `help`
# - `summary`: Displays the count of positive, negative, and neutral sentiments
# - `reset`: Clears the conversation history and resets counters
# - `history`: Shows all previous user inputs
# - `help`: Displays a list of available commands
# - Return appropriate responses for each command

# Define a function to validate the user's name
# - Continuously prompt the user for a name until they enter a valid alphabetic string
# - Strip any extra spaces and ensure the input is not empty or invalid

# Define the main function to start the chatbot
# - Display a welcome message and introduce the Sentiment Spy activity
# - Ask the user for their name and store it in the `user_name` variable
# - Enter an infinite loop to interact with the user:
#   - Prompt the user to enter a sentence or command
#   - Check for empty input and prompt the user to enter a valid sentence
#   - If the input matches specific commands (`exit`, `summary`, `reset`, `history`, `help`), execute the corresponding functionality
#   - Otherwise, call the `analyze_sentiment` function to analyze the input text
#   - Display the sentiment analysis result with color-coded feedback
# - Exit the loop and display a final summary when the user types `exit`

# Define the entry point for the script
# - Ensure the chatbot starts only when the script is run directly (not imported)
# - Call the `start_sentiment_chat` function to begin the activity
