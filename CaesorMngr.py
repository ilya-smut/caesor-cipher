import CaesorBasicFs, CaesorPhraseHack
class Caesor:
    def __init__(self, path_to_wordset = 'dict.txt'):
        self.phrase =''
        self.wordset = CaesorBasicFs.get_set(path_to_wordset)
    
    def change_input(self, phrase):
        if type(phrase) == tuple:
            self.phrase, _ = phrase
        else:
            self.phrase = phrase
    
    def change_wordset(self, path_to_file):
        self.wordset = CaesorBasicFs.get_set(path_to_file)
    
    def encrypt(self, key):
        return CaesorBasicFs.encrypter(self.phrase, key)

    def decrypt(self, key):
        return CaesorBasicFs.decrypter(self.phrase, key)

    def brute_force(self):
        return CaesorPhraseHack.phrase_brute_force(self.phrase, self.wordset)
    
    def print(self):
        print(self.phrase)

