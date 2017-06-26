def break_words(stuff):
    #splits sentence on the space to a list
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    #uses the sorted function to sort alphabetically
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    #grabs the first word from list
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    #grabs last word from the list
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    #break words to a list, then sort alphabetically
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    #break words to a list, then print functionality
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    #sort_sentence calls break_words to make it a list
    #then perform action
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
