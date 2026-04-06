from data import timetable, exams

def chatbot():
    print("🎓 Welcome to College AI Assistant 🤖\n")
    
    name = input("Enter your name: ")
    print(f"\nHello {name}! Ask me about timetable, subjects, exams.")
    print("Type 'bye' to exit.\n")
    
    while True:
        user = input("You: ").lower()
        
        # Greetings
        if any(word in user for word in ["hello", "hi", "hey"]):
            print("Bot: Hi! How can I help you?\n")
        
        elif "how are you" in user:
            print("Bot: I'm fine! How can I assist you?\n")
        
        # Weekly Timetable
        elif "timetable" in user or "schedule" in user:
            print("\n📅 Weekly Timetable:\n")
            for day, schedule in timetable.items():
                print(f"{day}:")
                for time, subject in schedule.items():
                    print(f"  {time} → {subject}")
                print()
        
        # Specific Day
        elif any(day.lower() in user for day in timetable.keys()):
            for day in timetable.keys():
                if day.lower() in user:
                    print(f"\n📅 {day} Timetable:")
                    for time, subject in timetable[day].items():
                        print(f"{time} → {subject}")
                    print()
        
        # Subjects
        elif "subject" in user:
            subjects = set()
            for day in timetable.values():
                for sub in day.values():
                    subjects.add(sub)
            print("\n📚 Subjects:")
            for sub in subjects:
                print(f"- {sub}")
            print()
        
        # Exam Info
        elif "exam" in user:
            print("\n📝 Exam Details:")
            print(f"Mid Exams: {exams['mid_exam']['start_date']} to {exams['mid_exam']['end_date']}")
            print(f"Final Exams: {exams['final_exam']['start_date']} to {exams['final_exam']['end_date']}\n")
        
        # Exit
        elif user == "bye":
            print("Bot: Goodbye! Have a nice day 😊")
            break
        
        # Unknown
        else:
            print("Bot: Sorry, I didn't understand. Please try again.\n")

chatbot()