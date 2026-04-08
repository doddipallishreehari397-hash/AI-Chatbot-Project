from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Training data
questions = [
    "What is my timetable?",
    "Show my timetable",
    "Give class schedule",
    "What classes do I have?",
    
    "When are mid exams?",
    "Mid exam dates",
    "Exam schedule",
    
    "Show Monday schedule",
    "What classes on Monday?",
    
    "List all subjects",
    "What subjects do I have?",
    "Show subjects list"
]

answers = [
    "Weekly Timetable:\nMonday: Math, Physics, English\nTuesday: Chemistry, Math, Lab...",
    "Weekly Timetable:\nMonday: Math, Physics, English\nTuesday: Chemistry, Math, Lab...",
    "Weekly Timetable:\nMonday: Math, Physics, English\nTuesday: Chemistry, Math, Lab...",
    "Weekly Timetable:\nMonday: Math, Physics, English\nTuesday: Chemistry, Math, Lab...",
    
    "Mid exams start from 10th October",
    "Mid exams start from 10th October",
    "Mid exams start from 10th October",
    
    "Monday Schedule: Math, Physics, English",
    "Monday Schedule: Math, Physics, English",
    
    "Subjects: Math, Physics, Chemistry, English, Computer Science",
    "Subjects: Math, Physics, Chemistry, English, Computer Science",
    "Subjects: Math, Physics, Chemistry, English, Computer Science"
]

# Train model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def chatbot(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    index = similarity.argmax()
    return answers[index]


# 👇 REQUIRED for main.py
def run():
    print("🤖 NLP Student Chatbot (type 'exit' to stop)\n")

    while True:
        user = input("You: ")

        if user.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        print("Chatbot:", chatbot(user))