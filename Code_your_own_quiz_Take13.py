
quiz_level = ["easy", "medium", "hard"]

quiz = ['''
A computer is a ___(1)___. Unlike a toaster or a refrigerator, you can write any kind of ___(2)___ --a precise
sequence of instructions--for a ___(1)___, and it can execute it. In fact, with only four things (simple arithmetic,
operators, if statements, and functions), you can in theory write any ___(2)___. In practice, this simplicity
requires a precise grammar that determines how code must be written and the order in which code is evaluated.
For example, in ___(3)___, as in many computer languages, variables are assigned using this form: NAME = EXPRESSION.
And ___(3)___, like any language using a Backus-Naur form of notation, always evaluates the ___(4)___ side
of an assignment statement first.''',
'''
To create a ___(1)___, use an assignment statement with expressions and operators to identify the ___(1)___'s value.
Use ___(1)___s to make code readable and reduce the amount of code you have to write; a number without a ___(1)___ is
a ___(2)___. Avoid them because ___(2)___s make code harder to read, harder to generalize, and prone to errors.

Like ___(1)___s, ___(3)___s are reusable and reduce the amount of code you have to write. Unlike a ___(1)___, a ___(3)___
can perform an action. In Python, ___(1)___s assigned inside a ___(3)___ are ___(4)___ while ___(1)___s assigned outside
of a ___(3)___ are global.''',
'''
A ___(1)___ is a type of structured ___(2)___ that can combine multiple ___(2)___ types (integers and strings, for example).
It's also a ___(3)___ object, which means it can be modified. In addition, ___(1)___s support ___(4)___--multiple variables
can be assigned to the same ___(1)___.''']

possible_answers = [[[],["universal machine", "um"], ["program", "computer program"], ["python"], ["right"]],
[[],["variable"], ["magic number"], ["function"], ["local"]],
[[],["list"], ["data"], ["mutable"], ["aliasing", "aliases"]]]

answers = [["", "universal machine", "program", "Python", "right"], ["", "variable", "magic number", "function", "local"],
["", "list", "data", "mutable", "aliasing"]]

welcome = '''Welcome! Please choose one of the following three levels by typing it in: easy, medium, hard.'''

follow_the_rules = '''
That's not an option. Please type easy, medium, or hard.'''

rules = '''
For each blank, you'll get five chances to fill it in correctly.
If you fail to answer correctly in five attempts, the quiz will end.

Here's your quiz. Some answers may be two-word answers.'''


blanks_list = ["___(0)___", "___(1)___", "___(2)___", "___(3)___", "___(4)___"]


def strip_punctuation(learner_input, approved_response):
    #Behavior: determines if one of the approved strings is a substring of learner's input
    #Input: 'learner_input' parameter takes a user-generated string--either 'level_input' or 'answer_input';
    #the 'approved_response' paramater takes a list of approved strings (either 'quiz_level' or nested list from 'possible_answers')
    #Output: returns matching string or None
    for element in approved_response:
        if element in learner_input:
            return element

def determine_level(level_input):
    #Behavior: sets quiz difficulty level
    #Input: 'level_input' string, which is user's preferred difficulty level
    #Output: value of 'index_level' variable, which is integer [0-2] or None if no match
    level_input = level_input.lower()
    level_input = strip_punctuation(level_input, quiz_level)
    if level_input in quiz_level:
        index_level = quiz_level.index(level_input)
        return index_level
    else:
        return None


def review_answer(answer_input, current_possible_answers, blanks):
    #Behavior: marks user answer as correct or incorrect
    #Input: 'answer_input' string, which is user's suggested answer, 'current_possible_answers' list,
    #which is a sublist of possible_answers, and 'blanks' integer [1-4], which is used to index current_possible_answers
    #Output: True if match; False if no match
    answer_input = answer_input.lower()
    if 'immutable' in answer_input:
        return False
        #I don't think this looks like an elegant solution, but 'mutable' is currently the only answer that is embedded in
        #a wrong answer that is both common and likely; if there were more such exceptions, I'd add them here. If there were
        #lots of exceptions, I'd create a function to cylce through a list of exceptions.
    answer_input = strip_punctuation(answer_input, current_possible_answers[blanks])
    if answer_input in current_possible_answers[blanks]:
        return True
    return False


def replace_blanks(current_quiz, blanks_list, blanks, current_answers):
    #Behavior: replace blank(s) in quiz with answer
    #Inputs: (1)'current_quiz' string, which is string from 'quiz' list; (2) 'blanks_list' list;
    #(3)'blanks' integer [1-4]; (4) 'current_answers' list
    #Output: returns a 'replaced' string, which is filled-in-blank version of 'current_quiz' string
    replaced = []
    current_quiz = current_quiz.split()
    for text in current_quiz:
        if blanks_list[blanks] in text:
            text = text.replace(blanks_list[blanks], current_answers[blanks])
            replaced.append(text)
        else:
            replaced.append(text)
    replaced = " ".join(replaced)
    return replaced


def start_game():
    #Behavior: welcome learner and then display rules and chosen quiz
    #Inputs: 'raw_input' from learner (regarding choice of level)
    #Output: multiple print statements to welcome and request level, confirm level, name rules, and initiate quiz/game
    level_input = raw_input(welcome)
    while determine_level(level_input) == None:
        level_input = raw_input(follow_the_rules)
    current_quiz = quiz[determine_level(level_input)]
    current_answers = answers[determine_level(level_input)]
    current_possible_answers = possible_answers[determine_level(level_input)]
    print "\n" + "You chose " + quiz_level[determine_level(level_input)] + "."
    print rules
    play_game(current_quiz, current_answers, current_possible_answers)




def play_game(current_quiz, current_answers, current_possible_answers):
    #Behavior: display quiz, give learner five chances to answer each question, and end game
    #Inputs: 'raw_input' from learner; the three parameters are sublists of 'quiz,' 'answers,' and 'possible answers';
    #the sublist is identified via the 'determine_level(level_input)' function (integer 0-2),
    #which is used to assign the sublists in the 'start_game()' function
    #Outputs: prints the quiz and prints a response to every input from user
    #I think I implemented this function as the previous reviewer requested, and I think it's just under the length requirement
    #when excluding variable assignments. If I'm incorrect, please give me some pointers on how to shorten this
    #(and on how you count length). Thanks!
    blanks = 1
    chances = 5
    last_chance = 1
    no_more_chances = 0
    print current_quiz
    while blanks < len(blanks_list):
        answer_input = raw_input("\n" +"What belongs in" + blanks_list[blanks] + "?")
        if review_answer(answer_input, current_possible_answers, blanks):
            print "\n" + "Well done." + "\n"
            current_quiz = replace_blanks(current_quiz, blanks_list, blanks, current_answers)
            print current_quiz
            blanks += +1
            chances = 5
            if blanks == len(blanks_list):
                 print "\n" + "Congratulations! You've successfully completed the quiz."
        else:
            print "\n" + "Nope."
            chances -= 1
            if chances == last_chance:
                print "This is your last chance."
            elif chances == no_more_chances:
                print "That's not correct. Your quiz is over."
                break
            else:
                print "You have " + str(chances) + " chances left to answer correctly."

start_game()

