# Simple  AI-Powered Chatbot 🤖💬

A simple AI-powered chatbot using spaCy NLP for natural language processing. The bot can greet users, respond to basic questions, and process user input intelligently.



## Features ✨
- Asks for the user's name and greets them.
- Recognizes greetings, farewells, and common questions.
- Provides a default response for unknown inputs.
- Uses Natural Language Processing (NLP) with spaCy.
- Keeps chatting until the user types "bye".

## Installation & Setup 🛠️  

1. **Clone the Repository**  
   ```bash
   git clone <https://github.com/annumaryroy/Basic-Chatbot.git>
   cd <your-project-folder>
2. **Create & Activate a Virtual Environment**  
   ```bash
   python3 -m venv venv  
   source venv/bin/activate  # Mac/Linux  
   venv\Scripts\activate  # Windows  

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   
## How to Run 🚀
   ```bash
python chatbot.py 
```

##  Example Usage
Bot: Hey there! What's your name? 😃  
You: Anu  
Bot: Nice to meet you, Anu! Let's chat. 💬 Type 'bye' to exit.  
You: Hello  
Bot: Hi Anu! 😊  
You: How are you?  
Bot: I'm just a bot, but I'm doing great! 🤖 How about you, Anu?  
You: Bye  
Bot: See you later, Anu! 😊  

