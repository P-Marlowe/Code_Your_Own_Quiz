quiz = """A ___(1)___ is created with the def keyword. You specify the inputs a ___(1)___ takes by
adding ___(2)___! separated by commas between the parentheses. ___(1)___, by default return None if you
don't specify the value to return. Note that ___(2)___ can be standard data types such as string, number, dictionary,
tuple, and list or can be more complicated such as objects and lambda functions."""

answers = ["function", "Function"]

blanks_list = ["___(1)___", "___(2)___", "___(3)___", "___(4)___", "___(5)___", "___(6)___"]


def blanks_in_text(text, blanks_list):
    #function locates blanks in quiz text
    for blank in blanks_list:
        if blank in text:
            return blank
    return None

def review_input(user_input):
    #evaulates user answers
    if user_input in answers:
        return "You got it!"
    else:
        return "That's not quite right. Try again."

def take_quiz(quiz_string, blanks_list):
    #In current iteration, this function replaces the blanks
    print quiz
    replaced = []
    quiz_string = quiz_string.split()
    for text in quiz_string:
        replacement = blanks_in_text(text, blanks_list)
        if replacement != None:
            user_input = raw_input("What is the answer to" + replacement +"?")
            text = text.replace(replacement, user_input)
            replaced.append(text)
        else:
            replaced.append(text)
    replaced = " ".join(replaced)
    return replaced                     
    
print take_quiz(quiz, blanks_list)
