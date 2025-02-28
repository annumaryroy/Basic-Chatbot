import random
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

    print("Bot:", response)



