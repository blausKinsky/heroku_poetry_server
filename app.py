from flask import Flask, render_template
import random
import nltk
# from helpers.rhymes import find_alliteration, find_phonemes, gen_rhyme_pair, gen_rando, gen_one_phone
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize, word_tokenize
from helpers.fp import find_phonemes_ngram
# z = nltk.corpus.gutenberg.fileids()
prondict = nltk.corpus.cmudict.dict()
f = open('artistStatements.txt')
raw2 = f.read()
sentence = sent_tokenize(raw2)
words = word_tokenize(raw2)
phoneNum = -2
phonemes = ['AH0', 'N']

app = Flask(__name__)

# def sep_fib(fib):
#     sep_fib.phrase = ''
#     for i in range(fib):

def ps_simple(fib):
    ps_simple.phrase = ''
    for i in range(fib):
        phrase = find_phonemes_ngram(-2, ['AH0', 'N'], sentence, i)
        rn = int(random.random()*len(phrase)-1)
        str_phrase = ' '.join(phrase[rn])
        ps_simple.phrase = ps_simple.phrase + str_phrase+" "+'<br/>'
        # print(ps.phrase)
        yield ps_simple.phrase
ps_simple.phrase = ''
# ps(5)

def run_simple():
    # print(run_simple.x)
    x = next(run_simple.x, 'end')
    if (x) == 'end':
        run_simple.x = ps_simple(5)
        return next(run_simple.x)
    else:
        return x

run_simple.x = ps_simple(5)

@app.route('/fibo_phone')
def fibo_phone():
    my_variable = run_simple()
    # return render_template("simple.html", words =my_variable)
    return render_template("index_archive.html", words=my_variable)


#ACROSTIC BEGIS HERE
def pick_word():
    my_choice = random.choice(words)
    return my_choice

def test_length(word):
    if len(word) >6:
        return word

def picker():
    for i in range(len(words)):
        v = pick_word()
        test = test_length(v)
        if test != None:
            return test

def broken_up(acrostic):
    letters = list(acrostic)
    return letters

def letter_word(l):
    temp_list = []
    for i in words:
        if i[:1] == l:
            temp_list.append(i)
    chosen_word = random.choice(temp_list)
    return chosen_word

def acrostic():
    acrostic = picker()
    lettre = broken_up(acrostic)
    word_is = ''
    for i in lettre[1:len(lettre)]:
        word_is = word_is + ' '+ letter_word(i)
    combo = acrostic + word_is
    collection = combo.split()
    # new_phrase = ' '.join(collection)
    return collection
    # for j in collection:
    #     ' '.join(j)

# acrostic()
@app.route('/art_acrostic')
def art_acrostic():
    my_variable = acrostic()
    # return render_template("simple.html", words =my_variable)
    return render_template("index.html", words=my_variable)


if __name__ == '__main__':
  app.run()

#to run this code, cd into the location where the file is and then goto your browser: localhost:5000/hello
