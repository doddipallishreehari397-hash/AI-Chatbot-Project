from day1 import run as day1
from day2 import run as day2
from day3 import run as day3
from day4 import run as day4
from day5 import run as day5

print("🎓 AI Student Chatbot Project")
print("1. Day 1 - Basic Chatbot")
print("2. Day 2 - Data Chatbot")
print("3. Day 3 - NLP Chatbot")
print("4. Day 4 - JSON Chatbot")
print("5. Day 5 - Login System")


choice = input("Enter your choice: ")

if choice == "1":
    day1()

elif choice == "2":
    day2()

elif choice == "3":
    day3()

elif choice == "4":
    day4()

else:
    print("Invalid choice")
