
## 🧠 ChatBot — Personalized Python Chat Assistant

A simple, friendly **Python-based chatbot** that remembers your name between sessions!
It can tell you jokes, show the current time/date, greet you personally, and even forget you when you ask.


### 🚀 Features

* 💬 Greets you personally by name
* 🕒 Tells the current **time** and **date**
* 😂 Shares funny **programmer jokes**
* 💾 **Remembers your name** using a local text file (`user_info.txt`)
* 🧹 You can reset memory anytime by saying **“forget me”**
* 👋 Simple and beginner-friendly code — perfect for learning Python


### 🧩 How It Works

When you first run the chatbot, it asks for your name and saves it to a file:

```
user_info.txt
```

Next time you open it, it will greet you with your name automatically!

Example:

```
🤖 ChatBot: Hi there! What’s your name? Sangeetha
🤖 ChatBot: Nice to meet you, Sangeetha! I'll remember you next time. 😊

🤖 ChatBot: Welcome back, Sangeetha! Type 'bye' to end the chat.
```


### 🖥️ Installation & Setup

#### 1️⃣ Clone or Download the Project

```bash
git clone https://github.com/<your-username>/chatboat.git
cd chatboat
```

#### 2️⃣ Run the ChatBot

Make sure you have **Python 3** installed.
Then run:

```bash
python chatboat.py
```

or (if using a specific version):

```bash
py -3.11 chatboat.py
```


### 💬 Example Conversation

```
🤖 ChatBot: Hi there! What’s your name? Sangeetha
🤖 ChatBot: Nice to meet you, Sangeetha! I'll remember you next time. 😊

🤖 ChatBot: Welcome back, Sangeetha! Type 'bye' to end the chat.

Sangeetha: hi
🤖 ChatBot: Hello Sangeetha! 😊

Sangeetha: tell me a joke
🤖 ChatBot: Why don’t programmers like nature? It has too many bugs!

Sangeetha: forget me
🤖 ChatBot: Okay, I’ve forgotten your name. You can tell me again next time 😊
```


### 📁 Project Structure

```
chatboat/
│
├── chatboat.py        # Main chatbot program
├── user_info.txt      # Stores user name (auto-created)
└── README.md          # Project description
```


### 🧰 Built With

* 🐍 **Python 3**
* 📦 Standard libraries: `datetime`, `random`, `os`



