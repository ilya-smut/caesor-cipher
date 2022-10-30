import CaesorBasicFs as caesor
import PhraseHandling as handler

def phrase_brute_force(phrase, wordset):
    orgnl_phrs_list, orgnl_phrs_set = handler.into_words(phrase)
    key_nums = {}
    decrypted_phrase = ''
    for en_word in orgnl_phrs_set:
        key_set = caesor.brute_force(en_word, wordset)
        for key in key_set:
            if key not in key_nums.keys():
                key_nums[key] = 1
            else:
                key_nums[key] += 1
    max_key = max(key_nums, key=key_nums.get)
    
    for en_word in orgnl_phrs_list:
        decrypted_phrase += caesor.decrypter(en_word, max_key)
        decrypted_phrase += ' ' 
    
    return decrypted_phrase, max_key