import re
import random

patterns = [
    (r"\bhi|hello|hey\b", [
        "Hello!",
        "Hi there! How can I help you?",
        "Hey! Nice to meet you."
    ]),

    (r"my name is (.*)", [
        "Nice to meet you, %1.",
        "Hello, %1! How are you today?"
    ]),

    (r"\bhow are you\b", [
        "I'm just a bot, but I'm doing fine! How about you?",
        "I'm doing great! What about you?"
    ]),

    (r"\bi feel (.*)", [
        "Why do you feel %1?",
        "Can you tell me more about why you feel %1?",
        "I'm listening. What's making you feel %1?"
    ]),

    (r"\b(sad|upset|depressed|down)\b", [
        "I'm sorry to hear that. Want to talk about what's bothering you?",
        "It's okay to feel sad sometimes. I'm here for you.",
        "Don't be too hard on yourself. Things will get better."
    ]),

    (r"\b(angry|mad|furious)\b", [
        "It's okay to feel angry. Do you want to tell me what happened?",
        "Anger can be tough. Try taking a deep breath first.",
        "I understand. Sometimes we just need to talk it out."
    ]),

    (r"\b(happy|good|great)\b", [
        "That's awesome! What made you feel happy today?",
        "I'm glad to hear that! Keep smiling.",
        "Wonderful! I hope your day stays just as good."
    ]),

    (r"\b(excited|thrilled|energetic)\b", [
        "That's so cool! What's got you excited?",
        "Sounds like something fun is happening!",
        "Excitement looks good on you. Tell me more!"
    ]),

    (r"\bmotivat|inspire|encourage\b", [
        "You're doing better than you think!",
        "Every small step counts. Keep going!",
        "Believe in yourself - you've got this!",
        "Don't stop now; your future self will thank you!"
    ]),

    (r"\bjoke|funny|laugh\b", [
        "Why did the computer get cold? Because it left its Windows open!",
        "Why do programmers hate nature? Too many bugs.",
        "Why was the math book sad? It had too many problems!"
    ]),

    (r"\bhobby|hobbies|bored|what should i do\b", [
        "You could try painting, playing guitar, or reading a book.",
        "How about going for a walk, journaling, or trying a new recipe?",
        "Maybe pick up a new hobby - photography, music, or gardening!"
    ]),

    (r"what is your name", [
        "I am Nova, your friendly chatbot.",
        "You can call me Nova.",
        "I'm Nova, your friendly virtual friend."
    ]),

    (r"thank you|thanks", [
        "You're welcome!",
        "No problem at all!",
        "Glad I could help!"
    ]),

    (r"quit|bye|exit", [
        "Goodbye!",
        "See you later!",
        "Thanks for chatting!"
    ]),

    (r"(.*)", [
        "I'm not sure I understand.",
        "Could you please elaborate?",
        "Tell me more.",
        "That's interesting - go on."
    ])
]

def get_response(user_input):
    for pattern, responses in patterns:
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            response = random.choice(responses)
            if "%1" in response:
                try:
                    word = match.group(1)
                    response = response.replace("%1", word)
                except IndexError:
                    pass
            return response
    return "Hmm... I'm not sure I understand that."

def chat():
    print("Welcome! I'm Nova - your friendly virtual companion.")
    print("You can talk to me about your mood, hobbies, motivation, or just chat casually.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Nova:", random.choice(["Goodbye!", "See you soon!", "Take care!"]))
            break
        response = get_response(user_input)
        print("Nova:", response)

if __name__ == "__main__":
    chat()
