import datetime
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

predefined_responses = {
    "hi": "Hello! How can I help you today?",
    "how are you": "I'm just a bot, I don't have feelings! How can I assist you?",
    "what is your name": "I am a simple rule-based chatbot.",
    "what is today's date": None,
    "what time is it": None,
    "tell me a joke": "Why don’t skeletons fight each other?\nThey don’t have the guts",
    "tell me another joke": "Why did the golfer bring two pairs of pants?\nIn case he got a hole in one!"
}

def generate_response(user_input):
    tokenized_input = word_tokenize(user_input.lower())  # Tokenize and lowercase the user input
    if 'date' in tokenized_input and 'today' in tokenized_input:
        return f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}."
    elif 'time' in tokenized_input:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        return f"The current time is {current_time}."

    # Default reply
    for question in predefined_responses:
        tokenized_question = word_tokenize(question)
        if all(token in tokenized_input for token in tokenized_question):
            return predefined_responses[question]

    return "I'm sorry, I don't understand that question. Can you please rephrase?"

# Execution starts here
while True:
    print("\n")
    user_input = input("You: ").lower()  # Prompt user input and convert to lowercase
    exit_commands = ['exit', 'bye', 'quit']
    if user_input in exit_commands:
        print("Chatbot: Goodbye! Have a great day!")
        break
    bot_response = generate_response(user_input)
    print(f"Chatbot: {bot_response}")
