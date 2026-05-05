import json

# Load users data safely
try:
    with open("users.json") as file:
        users_data = json.load(file)
except FileNotFoundError:
    print("❌ users.json file not found!")
    users_data = {"users": []}


def login():
    print("🔐 Login System\n")

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    for user in users_data.get("users", []):
        if user.get("username") == username and user.get("password") == password:
            print("✅ Login successful!\n")
            return True

    print("❌ Invalid username or password\n")
    return False


def chatbot():
    print("🤖 Welcome to Secure Student Chatbot")
    print("Type 'exit' to stop\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "exit":
            print("Bot: Goodbye! 👋")
            break
        elif user_input in ["hi", "hello"]:
            print("Bot: Hello! How can I help you?")
        elif "exam" in user_input:
            print("Bot: Your exams are coming soon. Stay prepared!")
        elif "subject" in user_input:
            print("Bot: You can check your subjects in the timetable.")
        else:
            print("Bot: You are logged in and chatting securely!")


# 👇 MAIN RUN FUNCTION
def run():
    if login():
        chatbot()


# 👇 THIS LINE WAS MISSING (IMPORTANT)
if __name__ == "__main__":
    run()