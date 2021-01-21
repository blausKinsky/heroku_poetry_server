import nltk
import random
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
import re
prondict = nltk.corpus.cmudict.dict()
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
# z = nltk.corpus.gutenberg.fileids()
f = open('artistStatements.txt')
raw2 = f.read()
sentence = sent_tokenize(raw2)
phonemes = ['AH0', 'N']

def find_phonemes_ngram(num, ph_list, sentences,ngrm):
    output = []
    for i in sentences:
        sent = i.split()
        for j in range(len(sent)):
            word = re.sub(r'[^\w\s]', '', sent[j].lower())
            if word in prondict:
                syl = prondict[word]
                pho = syl[-1][num:]
                location = j
                phrase = sent[location-ngrm:location+1]
                # if pho == ph_list then it's definitely longer than 1, so we don't need to check that
                if pho == ph_list and len(word)>3 and len(phrase)>0:
                    # print('pho: ', pho)
                    # print('phrase: ', phrase)
                    output.append(phrase)
    return output

def remove_punctuation(w):
    word = re.sub(r'[^\w\s]', '', w.lower())
    return word

def r_punct_list(w):
    output = []
    for i in range(len(w)):
        word = re.sub(r'[^\w\s]', '', w[i].lower())
        output.append(word)
    return output

def list_to_str(input_seq):
   # Join all the strings in list
   final_str = ' '.join(input_seq)
   return final_str

def list_to_str_nospace(input_seq):
   # Join all the strings in list
   final_str = ''.join(input_seq)
   return final_str

def ret_no_punct_string(w):
    # print('w is ', w)
    phrase = r_punct_list(w)
        # print('the phrase is ', phrase)
        # phrase_list.append(phrase)
    phrase_string = list_to_str_nospace(phrase)
    return phrase_string