

'''import random
user_name=input("Bot: Hey there! What's your name? 😃\nYou: ")
print(f"Bot: Nice to meet you {user_name}!!Let's chat. 💬 Type 'bye' to exit")
responses = {
    "hello": [f"Hi {user_name}! 😊", f"Hello {user_name}! 👋", f"Hey there, {user_name}! 😃"],
    "how are you": [f"I'm just a bot, but I'm doing great! 🤖 How about you, {user_name}?", f"I am doing well, {user_name}. What about you? 😃"],
    "bye": [f"Goodbye {user_name}! 👋", f"See you later, {user_name}! 😊", f"Take care, {user_name}! 💙"],
    "default": ["I don't understand. Can you rephrase that? 🤔", "Hmm, tell me more! 👀"]
}
while True:
    user_input = input("You: ").lower()
    if user_input=="bye":
        print("Bot:", random.choice(responses["bye"]))
        break
    response = random.choice(responses.get(user_input, responses["default"]))

    print("Bot:", response)'''
import spacy
import random

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Ask for the user's name
user_name=input("Bot: Hey there! What's your name? 😃\nYou: ")
print(f"Bot: Nice to meet you {user_name}!! Let's chat. 💬 Type 'bye' to exit")

# Predefined responses
responses = {
    "greet": [f"Hi {user_name}! 😊", f"Hello {user_name}! 👋", f"Hey there, {user_name}! 😃"],
    "goodbye": [f"Goodbye {user_name}! 👋", f"See you later, {user_name}! 😊", f"Take care, {user_name}! 💙"],
    "feeling": [f"I'm just a bot, but I'm doing great! 🤖 How about you, {user_name}?", f"I am doing well, {user_name}. What about you? 😃"],
    "default": ["I don't quite understand. Can you rephrase that? 🤔", "Hmm, tell me more! 👀"]
}

# Function to process user input
def get_response(user_input):
    doc = nlp(user_input.lower())  # Process the text with spaCy NLP

    # Check for greetings
    for token in doc:
        if token.lemma_ in ["hello", "hi", "hey"]:
            return random.choice(responses["greet"])
        elif token.lemma_ in ["bye", "goodbye", "see", "later"]:
            return random.choice(responses["goodbye"])
        elif token.lemma_ in ["how", "feel", "doing"]:
            return random.choice(responses["feeling"])

    return random.choice(responses["default"])

# Chatbot loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit"]:
        print("Bot:", random.choice(responses["goodbye"]))
        break
    response = get_response(user_input)
    print("Bot:", response)

