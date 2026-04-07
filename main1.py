import json

# Load JSON data
with open("data.json") as file:
    data = json.load(file)

# Keywords mapping (NLP logic)
keywords = {
    "timetable": ["timetable", "schedule", "time table"],
    "subjects": ["subjects", "courses"],
    "exam": ["exam", "tests"],
    "fees": ["fees", "fee payment"],
    "holiday": ["holiday", "leave"],
    "principal": ["principal", "head"],
    "college_time": ["college time", "opening time"],
    "library": ["library"],
    "canteen": ["canteen", "food"],
    "contact": ["contact", "phone"]
}

def chatbot():
    print("🤖 Smart Student Assistant Chatbot")
    print("Type 'exit' to stop\n")

    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("Bot: Goodbye! 👋")
            break

        found = False

        # NLP matching
        for key, words in keywords.items():
            for word in words:
                if word in user:
                    print("Bot:", data[key])
                    found = True
                    break
            if found:
                break

        if not found:
            print("Bot: Sorry, I don't understand. Try asking differently.")

chatbot()