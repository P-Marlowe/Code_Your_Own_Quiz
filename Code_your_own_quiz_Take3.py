quiz_level = ["easy", "medium", "hard"]

quiz = ['''Easy A ___(1)___ is created with the def keyword. You specify the inputs a ___(1)___ takes by
adding ___(2)___ separated by commas between the parentheses. ___(1)___s by default return ___(3)___ if you
don't specify the value to return. ___(2)___ can be standard data types such as string, number, dictionary,
tuple, and ___(4)___ or can be more complicated such as objects and lambda functions.
''',  '''Medium A ___(1)___ is created with the def keyword. You specify the inputs a ___(1)___ takes by
adding ___(2)___ separated by commas between the parentheses. ___(1)___s by default return ___(3)___ if you
don't specify the value to return. ___(2)___ can be standard data types such as string, number, dictionary,
tuple, and ___(4)___ or can be more complicated such as objects and lambda functions.
''', '''Hard A ___(1)___ is created with the def keyword. You specify the inputs a ___(1)___ takes by
adding ___(2)___ separated by commas between the parentheses. ___(1)___s by default return ___(3)___ if you
don't specify the value to return. ___(2)___ can be standard data types such as string, number, dictionary,
tuple, and ___(4)___ or can be more complicated such as objects and lambda functions.
''']

possible_answers = [[[],["function", "Function"], ["arguments", "Arguments"], ["None"], ["list", "List"]], [[],["MEDfunction", "MEDFunction"], ["MEDarguments", "MEDArguments"], ["MEDNone"], ["MEDlist", "MEDList"]], [[],["HARDfunction", "HARDFunction"], ["HARDarguments", "HARDArguments"], ["HARDNone"], ["HARDlist", "HARDList"]]] 

answers = [["", "function", "arguments", "None", "list"], ["", "MEDfunction", "MEDarguments", "MEDNone", "MEDlist"], ["", "HARDfunction", "HARDarguments", "HARDNone", "HARDlist"]]



welcome = '''Welcome! Please choose one of the following three
levels by typing it in: easy, medium, hard.'''

follow_the_rules = '''
That's not an option. Please type easy, medium, or hard.'''

rules = '''
For each blank, you'll get five chances to answer correctly.
If you fail to answer correctly in five attempts, the quiz will end.

Here's your quiz.
'''

difficulty_level = [["easy", "Easy", "Easy.", "Easy!", "EASY", "EASY!"], ["medium", "Medium", "Medium.", "Medium!", "MEDIUM", "MEDIUM!"], ["hard", "Hard", "Hard.", "Hard!", "HARD", "HARD!"]]

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

user_input = raw_input(welcome)
while determine_level(user_input) == None:
    user_input = raw_input(follow_the_rules)
level = determine_level(user_input)
print ""
print "You chose " + quiz_level[level] + "."
print rules


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



current_quiz = quiz[level]
blanks = 1
print current_quiz
while blanks < len(blanks_list):
    answer_input = raw_input("What belongs in" + blanks_list[blanks] + "?")
    if review_answer(answer_input):
        print "Well done."
        current_quiz = replace_blanks(current_quiz, blanks_list)
        print current_quiz
        blanks += +1
    else:
        #blanks += +1
        print "Nope."
    





#test_list = [[["dog"], ["cat", "horse", "uncle"], ["fish"]], ["meddog", "medcat", "medfish"], ["harddog", "hardcat", "hardfish"]]

#print len(blanks)




