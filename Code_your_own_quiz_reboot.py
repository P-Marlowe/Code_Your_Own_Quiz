#Code_Your_Own_Quiz_Reboot


easy = '''Easy A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''


medium = '''Medium A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

hard = '''Hard A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

welcome = '''Welcome! Please choose one of the following three
levels by typing it in: easy, medium, hard.'''

follow_the_rules = "That's not an option. Please type easy, medium, or hard."

rules = '''
For each item, you'll get five chances to answer correctly.
If you fail to answer correctly in five attempts, the quiz will end.'''

difficulty_level = [["easy", "Easy", "Easy.", "Easy!"], ["medium", "Medium", "Medium.", "Medium!"], ["hard", "Hard", "Hard.", "Hard!"]]



def intro(welcome):
    level = raw_input(welcome)
    print ""
    while determine_level(level) == None:
        level = raw_input(follow_the_rules)
    print ""
    print "You chose " + determine_level(level) + "."
    print rules

        

def determine_level(level):
    if level in difficulty_level[0]:
        return "easy"
    if level in difficulty_level[1]:
        return "medium"
    if level in difficulty_level[2]:
        return "hard"
    else:
        return None


        
    
        


intro(welcome)

    
#def select_quiz(level):
    



    
    
    
    
