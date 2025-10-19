import datetime
import random
import os

def get_user_name():
    """Check if username is already saved, else ask for it"""
    if os.path.exists("user_info.txt"):
        with open("user_info.txt", "r") as file:
            name = file.read().strip()
            if name:
                return name
    # If no name is saved, ask and store it
    name = input("🤖 ChatBot: Hi there! What’s your name? ").strip().capitalize()
    with open("user_info.txt", "w") as file:
        file.write(name)
    print(f"🤖 ChatBot: Nice to meet you, {name}! I'll remember you next time. 😊\n")
    return name


def chatbot_reply(user_input, user_name):
    """Function to return chatbot response based on user input"""
    user_input = user_input.lower()

    greetings = ["hello", "hi", "hey", "hola"]
    jokes = [
        "Why don’t programmers like nature? It has too many bugs!",
        "Why did the computer show up at work late? It had a hard drive!",
        "I told my computer I needed a break, and it said 'No problem — I’ll go to sleep!'",
    ]

    if any(word in user_input for word in greetings):
        return random.choice([
            f"Hello {user_name}! 😊",
            f"Hey {user_name}! How’s your day going?",
            f"Hi {user_name}! Nice to see you again!",
        ])

    elif "how are you" in user_input:
        return f"I'm just a bot, but I'm doing great! What about you, {user_name}?"

    elif "your name" in user_input:
        return "I'm ChatBot — your friendly assistant 🤖"

    elif "my name" in user_input:
        return f"You said your name is {user_name}, right?"

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today’s date is {current_date}."

    elif "joke" in user_input:
        return random.choice(jokes)

    elif "forget me" in user_input:
        if os.path.exists("user_info.txt"):
            os.remove("user_info.txt")
        return "Okay, I’ve forgotten your name. You can tell me again next time 😊"

    elif "help" in user_input:
        return "You can ask me about the time, date, a joke, or even tell me to forget you!"

    elif "bye" in user_input:
        return f"Goodbye {user_name}! Have a wonderful day 😊"

    else:
        return f"Hmm, I didn't get that, {user_name}. Could you say it differently?"


def main():
    """Main function to handle the chat loop"""
    user_name = get_user_name()
    print(f"🤖 ChatBot: Welcome back, {user_name}! Type 'bye' to end the chat.\n")

    while True:
        user_message = input(f"{user_name}: ")
        bot_response = chatbot_reply(user_message, user_name)
        print("🤖 ChatBot:", bot_response)

        if "bye" in user_message.lower():
            break


# Run the chatbot
if __name__ == "__main__":
    main()
