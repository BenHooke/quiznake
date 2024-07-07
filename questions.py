completed_keys = []

#template for copy/pasting

#'' : {
#'question' : '',
#'answer' : '',
#'hint' : '',
#'example' : 'Input: >>>\nOutput:',
#},

questions = {
    'append' : {
        'question' : 'Which function would you use to add an element to the end of a list?',
        'answer' : '.append()',
        'hint' : '''It's a commonly used word. From Oxford Languages: "the results of the survey are ______ed to this chapter".''',
        'example' : 'Input:  >>>people_who_miss_bob = [Fred, Linda, Janice]\n        >>>people_who_miss_bob.append("Bob")\n        >>>print(people_who_miss_bob)\nOutput: [Fred, Linda, Janice, Bob]',
    },
    'capitalize' : {
        'question' : 'What is the command to make the first letter of a string upper case?',
        'answer' : '.capitalize()',
        'hint' : "This is a longer word, but the function name is very direct and literal.",
        'example' : "Input:  >>>bad_grammar = 'start of the sentence'\n        >>>better_grammar = bad_grammar.capitalize()\n        >>>print(better_grammar)\nOutput: Start of the sentence",
    },
    'center' : {
        'question' : "This command will add an equal amount characters to either end of a string.",
        'answer' : '.center()',
        'hint' : "This command takes two arguments, first is the length of your line (int), second is the symbol that will dress your string (char).",
        'example' : 'Input:  >>>website = "website"\n        >>>adult_website = website.center(13, "X")\n        print(adult_website)\nOutput: XXXwebsiteXXX',
    },
    'count' : {
        'question' : "Tell me the function I would want to use if I wanted to find the number of recurrences of a word in a string.",
        'answer' : '.count()',
        'hint' : "I'm thinking of a certain vampire puppet. (Not from Forgetting Sarah Marshall)",
        'example' : '''Input:  >>>lyrics = "die, die, die... I can't"\n        >>>count = lyrics.count("die")\n        >>>print(count)\nOutput: 3''',
    },
    'False' : {
       'question' : 'What are you typing in to state that a certain toggle is considered OFF.',
       'answer' : 'False',
       'hint' : 'Boolean 0. Remember, this quiz is case sensitive.',
       'example' : 'Input:  >>>accurate = False\n        >>>print(accurate)\nOutput: False',
    },
    'find' : {
        'question' : "Use this command if you want to locate the index/position of a certain part of your string.",
        'answer' : '.find()',
        'hint' : "It's like you're playing hide and seek with that pesky index, and you're the seeker.",
        'example' : "Input:  >>>string = 'Which index does word start at?'\n        >>>word = string.find('word')\n        >>>print(word)\nOutput: 17",
    },
    'input' : {
        'question' : 'What function are you going to use if you want to prompt a user to type something in?',
        'answer' : 'input()',
        'hint' : "It's another word you would use if you wanted to get someone's thoughts or opinions.",
        'example' : "Input:  >>>input('Tell me something good: ')\nOutput: Tell me something good: Tell me that you love me.\n        'Tell me that you love me.'",
    },
    'isalnum' : {
        'question' : 'This command checks to see if a string consists of only letters and numbers, then returns True or False.',
        'answer' : '.isalnum()',
        'hint' : "It's checking to see if your string is alphanumeric, this means no punctuation marks or special characters.",
        'example' : "Input:  >>>aging_millennial = '42069lol'\n        >>>out_of_touch = aging_millennial.isalnum()\n        >>>print(out_of_touch)\nOutput: True\n\nDisclaimer: I am an againg millennial, please don't come after me.",
    },
    'len' : {
        'question' : 'What function would you use to find out the length of characters in a string?',
        'answer' : 'len()',
        'hint' : "If you're thinking about the length of a string, think about the length of this command.",
        'example' : 'Input:  >>>len("string")\nOutput: 6',
    },
    'pop' : {
        'question' : "What's the function to pick one element from a list and return it in a new one?",
        'answer' : '.pop()',
        'hint' : 'Imagine you have a bottle of soda and the cap is an element that you want to add to your cap collection.\nWhat are you going to do to the cap?',
        'example' : "Input:  >>>canadian_soda = ['Cola', 'Seltzer', 'Beer']\n        >>>not_soda = canadian_soda.pop(2)\n        >>>print(canadian_soda)\n        >>>print(not_soda)\nOutput: ['Cola', 'Seltzer']\n        Beer",
    },
    'print' : {
        'question' : 'What function would you use to display text to the user?',
        'answer' : 'print()',
        'hint' : '''The name of the function is very literal, if you wanted to display text on paper you would also ____ it.''',
        'example' : 'Input:  >>>print("Hello Squirrel")\nOutput: Hello Squirrel',
    },
    'range' : {
        'question' : "What's the function for generating a specific sequence of integers?",
        'answer' : 'range()',
        'hint' : "It's often used in loops, it can take 3 arguments, but only one is necessary.",
        'example' : "Input:  >>>print(list(range(2, 22, 2)))\nOutput: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]\n\nThe three arguments are: (start, stop, step), but only stop is required.",
    },
    'round' : {
        'question' : "Which function can turn a float into and integer, but can also control a float's number of decimal places?",
        'answer' : 'round()',
        'hint' : "This function would be good for doing simple math, especially with money.\nIt can have one or two arguments.",
        'example' : 'Input:  >>>round(45.60)\nOutput: 46\n\nInput:  >>>round(45.6012,2)\nOutput: 45.60',
    },
    'True' : {
        'question' : 'What are you typing in to state that a certain toggle is considered ON.',
        'answer' : 'True',
        'hint' : 'Boolean 1. Remember, this quiz is case sensitive.',
        'example' : 'Input:  >>>accurate = True\n        >>>print(accurate)\nOutput: True',
    },
    'type' : {
        'question' : "What function would you use to figure out what kind of thing you're looking at?",
        'answer' : 'type()',
        'hint' : 'Is it a string? or an integer? What is the class?',
        'example' : '''Input:  >>>type("string")\nOutput: <class 'str'>''',
    },
    'upper' : {
        'question' : "What's the function that will capitalize every character in a string?",
        'answer' : '.upper()',
        'hint' : 'Think about what you wanna do to the case of the characters. Not to be mistaken for the .capitalize() function.',
        'example' : 'Input:  >>>regular_phrase = "i am so excited"\n        >>>excited_phrase = regular_phrase.upper()\n        >>>print(excited_phrase)\nOutput: I AM SO EXCITED',
    },
}

#template for copy/pasting

#'' : {
#'question' : '',
#'answer' : '',
#'hint' : '',
#'example' : 'Input: >>>\nOutput:',
#},


# print(len(list(questions)))

# print('capitalize' in questions)