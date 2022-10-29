import CaesorPhraseHack as ph
import CaesorBasicFs as bf

message = 'I Love Olga very much'
encrypted_message = bf.encrypter(message, 18)
print(message)
print(encrypted_message)
print(ph.phrase_brute_force(phrase = encrypted_message))
