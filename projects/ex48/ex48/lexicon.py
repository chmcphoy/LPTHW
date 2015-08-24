directions = ('north', 'south', 'east', 'west')
verbs = ('go', 'kill', 'eat')
stops = ('the', 'in', 'of') 
nouns = ('bear', 'princess')  

# lower() Returns a copy of the characters; in lowercase
def get_tuple(word):
    test_word = word.lower()
    
    if test_word in directions:
        return ('direction', word)
    elif test_word in verbs:
        return ('verb', word)
    elif test_word in stops:
        return ('stop', word)
    elif test_word in nouns:
        return ('noun', word)
    elif test_word.isdigit():
        return ('number', int(word))
    else:
        return ('error', word)
        
def scan(sentence):
    words = sentence.split()
    return [get_tuple(word) for word in words]

# isdigit() Returns true if all characters in the string are digits, false otherwise.
# summary: Check whether word matches any of the variables; return the tuple
