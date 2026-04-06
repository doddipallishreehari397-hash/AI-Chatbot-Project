def chatbot():
    print("🎓 Welcome to Siddharth Institute of Engineering and Technology, puttur College AI Assistant 🤖\n")
    
    name = input("Enter your name: ")
    print(f"\nHello {name}! You can ask about timetable, subjects, exams.")
    print("Type 'bye' to exit.\n")
    
    while True:
        user = input("You: ").lower()
        
        # Greetings
        if "hello" in user or "hi" in user:
            print("Bot: Hi! How can I help you?")
        
        # Timetable
        elif "timetable" in user:
            print("\n📅 Timetable:")
            print("Monday: Maths, Physics, English")
            print("Tuesday: Chemistry, Python Lab\n")
        
        # Subjects
        elif "subjects" in user:
            print("\n📚 Subjects:")
            print("Maths, Physics, Chemistry, Python\n")
        
        # Exam Info
        elif "exam" in user:
            print("\n📝 Exams will start next month.\n")
        
        # Exit
        elif user == "bye":
            print("Bot: Goodbye! Have a nice day 😊")
            break
        
        # Unknown input
        else:
            print("Bot: Sorry, I didn't understand. Please ask something else.\n")

# Run chatbot
chatbot()