
questions = [
    "What does CPU stand for?",
    "Which language is used for web development?",
    "What is the output of 2 + 2?",
    "Which keyword is used to define a function in Python?",
    "Which data type stores True or False?",
    "Which Language is used to add a logic in websites code?"
]

options = [
    ["Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Control Processing Unit"],
    ["Python", "HTML", "CSS", "All of these"],
    ["3", "4", "5", "6"],
    ["function", "def", "define", "fun"],
    ["String", "Integer", "Boolean", "List"],
    ["HTML","CSS","Javascript","C"]
]
answers = [0, 3, 1, 1, 2 , 2]

def display_menu():
    print("\n==============================")
    print("     PYTHON LEARNING QUIZ")
    print("==============================")
    print("1. Start Quiz")
    print("2. View Instructions")
    print("3. Let me know your Name!")
    print("4. Description of the Quiz")
    print("5. Exit")

def start_quiz():

    score = 0

    for i in range(len(questions)):

        print("\nQuestion", i + 1, "of", len(questions))
        print(questions[i])

        for j in range(len(options[i])):
            print(j + 1, ".", options[i][j])

        answer = int(input("Enter your answer (1-4): "))

        if answer - 1 == answers[i]:
            print("Correct Answer!")
            score = score + 1

        else:
            print("Wrong Answer!")

    print("\n========== QUIZ RESULTS ==========")
    print("Your Score:", score, "/", len(questions))       


    

def main():
    print("Welcome to Python Learning Quiz!")

    display_menu()

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        print("Starting Quiz...")
        start_quiz()

    elif choice == "2":
        print("Instructions:")
        print("1. Answer the questions.")
        print("2. Each correct answer gives you one point.")
        print("3. Your final score will be displayed.")
        

    elif choice == "4":
        print("About the Game!")
        print("This is a Python-based multiple-choice quiz.")
        print("Test your Python knowledge and earn points!")

    elif choice == "3":
        name = input("Please Enter your name?")
        print("Hello")
        print(name)
        print("Let's play the Game!")

    elif choice == "5":
        print("Thank you for visiting!")    

    else:
        print("Invalid choice. Please select a number between 1 and 5.")


main()
