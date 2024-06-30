# pip install nltk
import nltk
from nltk.chat.util import Chat, reflections

# Define a set of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created for our conversation.",]
    ],
    [
        r"how are you?",
        ["I'm doing good\nHow about You?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great!",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, I don't have an age.",]
    ],
    [
        r"what (.*) want?",
        ["I just want to chat with you!",]
    ],
    [
        r"(.*) created?",
        ["I was created by a programmer using Python's NLTK library.",]
    ],
    [
        r"(.*) (location|city)?",
        ["I'm in the cloud, anywhere you want me to be.",]
    ],
    [
        r"how is the weather in (.*)?",
        ["Weather in %1 is amazing like always", "Too hot here in %1", "Too cold here in %1", "Never even heard about %1"]
    ],
    [
        r"(.*) (sports|game)?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["I love Robert Downey Jr.",]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ["That is interesting!", "Tell me more!", "I'm not sure I understand."]
    ],
]

# Initialize the chat
def chatbot():
    print("Hi! I'm a chatbot created using NLTK. Let's talk!")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
chatbot()
