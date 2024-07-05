from questions import questions
import random


print('''        __________                                             
       /  ____   /                                             
      /  /   /  /____________________ __   __ __    __ __ _____
     /  /   /  //________________   //  | / //  |  / //_// ___/
    /  /   /  /  __  __ _______ /  // /||/ // / | /  /  / __/  
   /  /   /  /  / / / //__  __//  //_/ |__//_/|_|/_/\\_\\/____/  
  /  /____\\ /  / /_/ /__/ /_  /  /__________________________   
 /___________\\/_____//_____/ /_____________________________/   
                                                               ''')

# def start_quiz():
#     #welome user with breif instructions and a start command

# def get_hint():
#     #display a hint associated with list item in questions.py

# def get_user_guess():
#     #get user input to compare with 'answer' key value in questions.py

# def user_guess_result()
#     #choose whether to display 'Correct Answer' or 'Wrong Answer' message

# def show_example():
#     #display 'example' key value from questions.py if user_guess is correct

def get_help():
    print("Help goes here")
#     #display a set of commands if user is stuck i.e. 'quit', 'skip' etc. until UI is made

def exit_game():
    print("Exit strategy goes here")

key = ""

def start_quiz():
    print("Welcome to Quiznake, enter one of the following commands:\n")
    print('''-start
-help
-quit\n''')
    user_input = input()
    if user_input == "start":
        print("\n")
        get_question()
        play_game()
    elif user_input == "help":
        print("\n")
        get_help()
    elif user_input == "quit":
        print("\n")
        return exit_game()
    while user_input != "start" or "help" or "quit":
        user_input = input("\nEnter command:\n\n")

def get_question():
    global key
    key = random.choice(list(questions))
    print(questions[key]['question'] + "\n")
    play_game()

def play_game():
    global key
    user_guess = input("Your guess: ")
    
    if user_guess == questions[key]['answer']:
        print("\nThat's right! It would look something like this:\n\n" + questions[key]['example'] + "\n\n---NEXT QUESTION---\n")
        get_question()
    while user_guess != str(questions[key]['answer']):
        # user_guess = input("Your guess:\n")
        if user_guess == "hint":
            print("\n---HINT---\n\n" + questions[key]['hint'] + "\n")
            play_game()
        else:
            print("\nNot quite! Try again. ***Don't forget to add punctuation like function() or .function***\n")
            play_game()

    
start_quiz()