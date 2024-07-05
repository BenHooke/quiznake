from questions import questions

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

def get_question():
    print("Question goes here")
#     #start the quiz with a random question from question.py

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


def start_quiz():
    print("Welcome to Quiznake, enter one of the following comands:\n")
    print('''-start
-help
-quit\n''')
    user_input = input()
    while user_input != "start" or "help" or "quit":
        user_input = input("Try something else:\n")
        if user_input == "start":
            return get_question()
        elif user_input == "help":
            return get_help()
        elif user_input == "quit":
            return exit_game()

    
start_quiz()