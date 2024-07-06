completed_keys = []

#template for copy/pasting

#    '' : {
#        'question' : '',
#        'answer' : '',
#        'hint' : '',
#        'example' : '',
#    },

questions = {
    'print' : {
        'question' : 'What function would you use to display text to the user?',
        'answer' : 'print()',
        'hint' : '''The name of the function is very literal, if you wanted to display text on paper you would also ____ it.''',
        'example' : 'Input: >>>print("Hello Squirrel")\nOutput:Hello Squirrel',
    },
    'type' : {
        'question' : "What function would you use to figure out what kind of thing you're looking at?",
        'answer' : 'type()',
        'hint' : 'Is it a string? or an integer? What is the class?',
        'example' : '''Input: >>>type("string")\nOutput: <class 'str'>''',
    },
    'len' : {
        'question' : 'What function would you use to find out the length of characters in a string?',
        'answer' : 'len()',
        'hint' : "If you're thinking about the length of a string, think about the length of this command.",
        'example' : 'Input: >>>len("string")\nOutput: 6',
    },
    'round' : {
        'question' : "Which funtion can turn a float into and integer, but can also control a float's number of decimal places?",
        'answer' : 'round()',
        'hint' : "This function would be good for doing simple math, especially with money.\nIt can have one or two arguments.",
        'example' : 'Input: >>>round(45.60)\nOutput: 46\n\nInput: >>>round(45.6012,2)\nOutput: 45.60',
    },
    'input' : {
        'question' : 'What function are you going to use if you want to prompt a user to type something in?',
        'answer' : 'input()',
        'hint' : "It's another word you would use if you wanted to get someone's thoughts or opinions.",
        'example' : "Input: >>>input('Tell me something good: ')\nOutput: Tell me something good: Tell me that you love me.\n       'Tell me that you love me.'",
   },
}