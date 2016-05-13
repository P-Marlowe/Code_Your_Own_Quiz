def blanks_in_text(text, blanks_list):
    #function locates blanks in quiz text
    for blank in blanks_list:
        if blank in text:
            return blank
    return None

def take_quiz(quiz_string, blanks_list):
    #In current iteration, this function replaces the blanks
    replaced = []
    quiz_string = quiz_string.split()
    for text in quiz_string:
        replacement = blanks_in_text(text, blanks_list)
        if replacement != None:
            text = text.replace(replacement, "corgi")
            replaced.append(text)
        else:
            replaced.append(text)
    replaced = " ".join(replaced)
    return replaced 
                    
    
print take_quiz(quiz, blanks_list)
