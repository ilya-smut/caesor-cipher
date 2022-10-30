characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def get_set(path = 'dict.txt'):
    with open (path) as dt:
        lines = dt.readlines()
        
    wordset = set()
    
    for word in lines:
        word = word.upper().strip()
        wordset.add(word)
        
    return wordset

def encrypter(word, argument):

    if (argument < 0) or (argument > 26):
        print('ERROR: Choose key {0..26}')
        return None
    
    word = word.upper()
    en_word = ''
    for char in word:
        if char == ' ':
            new_char = char
        else:
        
            if ((characters.index(char) + argument) < 26):
                new_char = characters[characters.index(char)+argument]
            else:
                new_char = characters[characters.index(char)+argument-26]
            
        en_word += new_char
        
    return en_word


def decrypter(word, argument):

    if (argument < 0) or (argument > 26):
        print('ERROR: Choose key {0..26}')
        return None
    
    en_word = word.upper()
    dec_word = ''
    
    for char in en_word:
        if ((characters.index(char) - argument) >= 0):
            new_char = characters[characters.index(char)-argument]
        else:
            new_char = characters[characters.index(char)-argument+26]
            
        dec_word += new_char

    return dec_word


def brute_force(en_word, wordset):
    en_word = en_word.upper()
    possible_keys = set()

    for key in range(26):
        plainword = decrypter(en_word, key)
        if plainword in wordset:
            possible_keys.add(key)

    return possible_keys
      

