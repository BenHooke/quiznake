from questions import questions, completed_keys
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
print("Welcome to Quiznake, enter one of the following commands:\n")
print('''-start
-help
-quit\n''')


def get_help():
    print('''          ------------------HELP------------------
Everything is case sensitive, so if you're feeling stuck think about how you would write in Python.

Commands:
          -help: List of commands (You're here now.)
          -hint: Get a question specific hint.
          -skip: Generate a new question for now.
          -QTM: Quit To Menu\n''')

key = ""

def start_quiz():
    user_input = input()
    if user_input == "start":
        print("\n")
        get_question()
        play_game()
    elif user_input == "help":
        print("\n")
        get_help()
        start_quiz()
    elif user_input == "quit":
        exit()

def get_question():
    global key
    key = random.choice(list(questions))
    if key in completed_keys and len(completed_keys) != len(questions):
        get_question()
    elif len(completed_keys) == len(questions):
        game_over()
    else:
        print(questions[key]['question'] + "\n")
        play_game()

def play_game():
    global key
    user_guess = input("Your guess: ")
    
    if user_guess == questions[key]['answer']:
        print("\nThat's right! It would look something like this:\n\n" + questions[key]['example'] + "\n\n---NEXT QUESTION---\n")
        completed_keys.append(key)
        get_question()
    while user_guess != str(questions[key]['answer']):
        if user_guess == "hint":
            print("\n--------------HINT--------------\n\n" + questions[key]['hint'] + "\n\n~~~Enter QTM to quit to menu~~~\n")
            play_game()
        elif user_guess == "help":
            get_help()
            play_game()
        elif user_guess == "QTM":
            print('\n-start\n-help\n-quit\n')
            start_quiz()
        elif user_guess == "skip":
            print("\n")
            get_question()
            play_game()
        else:
            print("\nNot quite! Try again. ***Don't forget to add punctuation like function() or .function***\n")
            play_game()

def game_over():
    print("Actually...\n\nThat's all of them for now! Great job!\n\n")
    start_quiz()
    completed_keys.clear()
    #Still looking for a way to start the quiz over again from this point, but it seems to be reading completed_keys as full still.



start_quiz()