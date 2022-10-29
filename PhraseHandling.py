def into_words(phrase):
    wordlist = []
    phraseset = set()
    current_word = ''
    for character in phrase+' ':
        if character == ' ':
            if current_word !='':
                wordlist.append(current_word)
                phraseset.add(current_word)
            current_word = ''
        else:
            current_word += character
    return wordlist, phraseset