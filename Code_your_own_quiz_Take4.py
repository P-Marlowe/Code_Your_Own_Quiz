quiz_level = ["easy", "medium", "hard"]

quiz = ['''
A computer is a ___(1)___. Unlike a toaster or a refrigerator, you can write any kind of ___(2)___ --a precise
sequence of instructions--for a ___(1)___, and it can execute it. In fact, with only four things (simple arithmetic,
operators, if statements, and functions), you can in theory write any ___(2)___. In practice, this simplicity
requires a precise grammar. For example, in ___(3)___, variables are assigned using this form: NAME = EXPRESSION,
and ___(3)___ always evaluates the ___(4)___ side of an assignment statement first.''',
'''
To create a ___(1)___, use an assignment statement with expressions and operators to identify the ___(1)___’s value.
Use ___(1)___s to make code readable and reduce the amount of code you have to write; a number without a ___(1)___ is
a ___(2)___. Avoid them because ___(2)___s make code harder to read, harder to generalize, and prone to errors.

Like ___(1)___s, ___(3)___s are reusable and reduce the amount of code you have to write. Unlike a ___(1)___, a ___(3)___
can perform an action. In Python, ___(1)___s assigned inside a ___(3)___ are ___(4)___ while ___(1)___s assigned outside
of a ___(3)___ are global.''',
'''
A ___(1)___ is a type of structured ___(2)___ that can combine multiple ___(2)___ types (integers and strings, for example).
While strings and ___(1)___s are both Python objects, ___(1)___s are different from strings because ___(1)___s can be
modified; they are ___(3)___ objects. Also, ___(1)___s are different from strings or integers because you can assign multiple
variables to the same ___(1)___. That is, ___(1)___s support ___(4)___.''']

possible_answers = [[[],["universal machine", "UM", "Universal Machine"], ["program", "Program", "computer program",
"Computer program", "Computer Program"], ["Python", "python", "most computer languages", "Most computer languages"],
["right", "Right"]],
[[],["variable", "Variable",], ["magic number", "Magic Number", "Magic number"], ["function", "Function"], ["local", "Local"]],
[[],["list", "List"], ["data", "Data"], ["mutable", "Mutable"], ["aliasing", "Aliasing", "aliases", "Aliases"]]]

answers = [["", "universal machine", "program", "Python", "right"], ["", "variable", "magic number", "function", "local"],
["", "list", "data", "mutable", "aliasing"]]



welcome = '''Welcome! Please choose one of the following three levels by typing it in: easy, medium, hard.'''

follow_the_rules = '''
That's not an option. Please type easy, medium, or hard.'''

rules = '''
For each blank, you'll get five chances to answer correctly.
If you fail to answer correctly in five attempts, the quiz will end.

Here's your quiz.'''

difficulty_level = [["easy", "Easy", "Easy.", "Easy!", "EASY", "EASY!"],
["medium", "Medium", "Medium.", "Medium!", "MEDIUM", "MEDIUM!"],
["hard", "Hard", "Hard.", "Hard!", "HARD", "HARD!"]]

blanks_list = ["___(0)___", "___(1)___", "___(2)___", "___(3)___", "___(4)___"]

def determine_level(user_input):
    #evaluates user's suggested quiz level
    if user_input in difficulty_level[0]:
        return 0
    if user_input in difficulty_level[1]:
        return 1
    if user_input in difficulty_level[2]:
        return 2
    else:
        return None


def review_answer(answer_input):
    #evaluates user answers
    if answer_input in possible_answers[level][blanks]:
        return True
    return False


def replace_blanks(current_quiz, blanks_list):
    #replace blanks with correct answers
    replaced = []
    current_quiz = current_quiz.split()
    for text in current_quiz:
        if blanks_list[blanks] in text:
            text = text.replace(blanks_list[blanks], answers[level][blanks])
            replaced.append(text)
        else:
            replaced.append(text)
    replaced = " ".join(replaced)
    return replaced


user_input = raw_input(welcome)
while determine_level(user_input) == None:
    user_input = raw_input(follow_the_rules)
level = determine_level(user_input)
print "\n" + "You chose " + quiz_level[level] + "."
print rules
current_quiz = quiz[level]
blanks = 1
chances = 5 #this needs to be changed; needs to be in a function so that it resets after every right answer.
print current_quiz
while blanks < len(blanks_list):
    answer_input = raw_input("\n" +"What belongs in" + blanks_list[blanks] + "?")
    if review_answer(answer_input):
        print "\n" + "Well done." + "\n"
        current_quiz = replace_blanks(current_quiz, blanks_list)
        print current_quiz
        blanks += +1
    else:
        print "\n" + "Nope."
        chances -= 1
        if chances == 1:
            print "This is your last chance."
        elif chances == 0:
            print "That's not correct.Your quiz is over."
            break
        else:
            print "You have " + str(chances) + " chances left to answer correctly."
        #print current_quiz







