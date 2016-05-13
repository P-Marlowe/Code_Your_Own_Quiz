def blanks_in_text(text, blanks_list):
    #function locates blanks in quiz text
    for blank in blanks_list:
        if blank in text:
            return blank
    return None
