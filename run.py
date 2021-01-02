# from helpers.this_helper import gen_random_number
from helpers.rhymes import refactored_find_phonemes, find_phonemes, find_alliteration, gen_rando

import random, textwrap
import nltk
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
from textblob import TextBlob, Word
thisSound = [['AA0'], ['AA1'], ['AA2'], ['AE0'], ['AE1'], ['AE2'], ['AH0'], ['AH1'], ['AH2'], ['AO0'], ['AO1'], ['AO2'],
             ['AW0'], ['AW1'], ['AW2'], ['AX0'], ['AX1'], ['AX2'], ['AXR'], ['AY0'], ['AY1'], ['AY2'], ['EH0'], ['EH1'],
             ['EH2'], ['ER0'], ['ER1'],['ER2'], ['EY0'], ['EY1'], ['EY2'], ['IH0'], ['IH1'], ['IH2'], ['IX0'], ['IX1'],
             ['IX2'], ['IY0'], ['IY1'], ['IY2'], ['OW0'], ['OW1'], ['OW2'], ['OY0'], ['OY1'], ['OY2'], ['UH0'], ['UH1'],
             ['UH2'], ['UW0'], ['UW1'], ['UW2'], ['UX0'], ['UX1'], ['UX2']]
z = nltk.corpus.gutenberg.fileids()
f = open('artistStatements.txt')
raw = f.read()
f.close()
artBlob = TextBlob(raw)
sentences = artBlob.sentences
my_list = []

sentence = sent_tokenize(raw)
phoneNum = -2
phonemes = ['AH0', 'N']
a = find_phonemes(phoneNum, phonemes, sentence, [])
b = refactored_find_phonemes(phoneNum, phonemes, sentence)

# print(gen_rando())
find_alliteration(sentences,my_list)

# print('this is the function ', find_alliteration(sentences,my_list))
# print(my_list)
print('old phonemes: ', a)
print('new phonemes: ', b)
#the function returns a list of tuples and it needs to be a string to use with the server app
# for i in range(len(my_list)):
#     print(' '.join(my_list[i]))


# print(gen_random_number())
# from my_helper import my_function
#
# print(my_function())



#choose a pair and convert it from a tuple to string
# my_tuple = gen_rhyme_pair()
# my1 = ' '.join(my_tuple[0])
# my2 = ' '.join(my_tuple[1])
# print(my1)
# print(my2)
