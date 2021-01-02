import nltk
import random
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
import re
prondict = nltk.corpus.cmudict.dict()

from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
z = nltk.corpus.gutenberg.fileids()
f = open('artistStatements.txt')
raw2 = f.read()
sentence = sent_tokenize(raw2)

phonemes = ['AH0', 'N']
# print(type(phonemes))

def refactored_find_phonemes(num, ph_list, sentences):
    #if outputlist is, presumably, an empty list, there's no reason to include it in the declaration
    output = []
    #same thing with range - if we're just using array[i], it's simpler to just use for in on the array itself
    for i in sentences:
        sent = i.split()
        for j in range(len(sent)):
            word = re.sub(r'[^\w\s]', '', sent[j].lower())
            #why are we checking "isalpha?"
            if word in prondict:
                syl = prondict[word]
                pho = syl[-1][num:]
                location = j
                phrase = sent[location-3:location+1]
                # if pho == ph_list then it's definitely longer than 1, so we don't need to check that
                if pho == ph_list and len(word)>3 and len(phrase)>0:
                    # print('pho: ', pho)
                    # print('phrase: ', phrase)
                    output.append(phrase)
    return output


# this_phone = refactored_find_phonemes(-2, phonemes, sentence)
# print(type(this_phone), this_phone[0])

class FP:
    '''returns a phoneme combination that user is seeking plus the prior 3 words. It is intended to be used to find rhyming couplets'''
    # def __init__(self, num_of_phonemes: int, ph_list: list[str], sentence: list[str]):
    def __init__(self, num_of_phonemes: int, ph_list: list, sentence: list, ngrm: int):
        self.num_of_phonemes = num_of_phonemes
        self.ph_list = ph_list
        self.sentence = sentence
        self.nrgram = ngrm

    def phonemeList(num_of_phonemes, ph_list, sentence) -> list:

        # def phoneme_list(self, num_of_phonemes, ph_list, sentence) ->list:
        '''return the a list of phonemes you are interested in'''
        output = []
        for i in sentence:
            sent = i.split()
            for j in range(len(sent)):
                word = re.sub(r'[^\w\s]', '', sent[j].lower())
                if word in prondict:
                    syl = prondict[word]
                    pho = syl[-1][num_of_phonemes:]
                    location = j
                    phrase = sent[location - 3:location + 1]
                    # if pho == ph_list then it's definitely longer than 1, so we don't need to check that
                    if pho == ph_list and len(word) > 3 and len(phrase) > 0:
                        # print('pho: ', pho)
                        # print('phrase: ', phrase)
                        output.append(phrase)
        return output

    def phonemeList_ngram(num_of_phonemes, ph_list, sentence, ngrm) -> list:

        # def phoneme_list(self, num_of_phonemes, ph_list, sentence) ->list:
        '''return the a list of phonemes you are interested in'''
        output = []
        for i in sentence:
            sent = i.split()
            for j in range(len(sent)):
                word = re.sub(r'[^\w\s]', '', sent[j].lower())
                if word in prondict:
                    syl = prondict[word]
                    pho = syl[-1][num_of_phonemes:]
                    location = j
                    phrase = sent[location - ngrm:location + 1]
                    # if pho == ph_list then it's definitely longer than 1, so we don't need to check that
                    if pho == ph_list and len(word) > 3 and len(phrase) > 0:
                        # print('pho: ', pho)
                        # print('phrase: ', phrase)
                        output.append(phrase)
        return output


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


# print(type(Find_Phoneme))
# g = FP.phonemeList(-2, ['AH0', 'N'], sentence)
z = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, 5)
ph = FP.phonemeList_ngram(-2, ['AH0', 'N'], sentence, 3)

# for i in range(5):
#     print(find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i))

#AD sept. 12th refactoring the refactored find phonemes
def rph(num, ph_list, sentences):
    list_output, string_output = [], []
    for i in sentences:
        sent = i.split()
        for j in range(len(sent)):
            if sent[j] in prondict:
                syl = prondict[sent[j]]
                pho = syl[-1][num:]
                phrase = sent[j-3:j+1]
                if pho == ph_list and len(sent[j])>3 and len(phrase)>0:
                    phrase = r_punct_list(phrase)
                    list_output.append(phrase)
                    phrase_string = list_to_str(phrase)
                    string_output.append(phrase_string)


    return list_output, string_output

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

def ph_ngram_list_punct(num, ph_list, sentences, ngram):
    list_output = []
    for i in sentences:
        sent = i.split()
        for j in range(len(sent)):
            if sent[j] in prondict:
                syl = prondict[sent[j]]
                pho = syl[-1][num:]
                phrase = sent[j-ngram:j+1]
                if pho == ph_list and len(sent[j])>3 and len(phrase)>0:
                    phrase = r_punct_list(phrase)
                    list_output.append(phrase)
                    # phrase_string = list_to_str(phrase)
                    # string_output.append(phrase_string)


    return list_output

def ph_ngram_str_punct(num, ph_list, sentences, ngram):
    string_output, list_output = [], []
    for i in sentences:
        sent = i.split()
        for j in range(len(sent)):
            if sent[j] in prondict:
                syl = prondict[sent[j]]
                pho = syl[-1][num:]
                phrase = sent[j-ngram:j+1]
                if pho == ph_list and len(sent[j])>3 and len(phrase)>0:
                    phrase = r_punct_list(phrase)
                    list_output.append(phrase)
                    phrase_string = list_to_str(phrase)
                    string_output.append(phrase_string)


    return string_output

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
    print('w is ', w)
    phrase = r_punct_list(w)
        # print('the phrase is ', phrase)
        # phrase_list.append(phrase)
    phrase_string = list_to_str_nospace(phrase)
    return phrase_string


my_sentences = ["I'm on The mission to mars and beyond.", "It is clear the viewer's require hospitalization after view my work."]
my_list = [["this", "is", "Deliberately", "I'm", "mis-ing"],["I'm", "on", "a", "very", "involved", "mission"]]
my_sentences2 = ["I'm on The mission to mars and beyond.", "It is clear the viewer's require hospitalization after view my work."]

# this = rph(-2,phonemes,my_sentences)
# print(this)
#
# this_thing = ret_no_punct_string(my_sentences2[0])
# print(this_thing)

# my_string = ph_ngram_str_punct(-2, phonemes, my_sentences, 3)
# list_nopunct = ph_ngram_list_punct(-2, phonemes, my_sentences, 3)
# print(my_string)
# print(list_nopunct)
