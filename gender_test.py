#!/bin/env python
import codecs
import random

class wordlist(list):
    def __init__(self,wordfile='nouns.txt'):
        with codecs.open(wordfile,'rb') as wf:
            for line in wf:
                self.append(line)

    def append(self,item):
        if '{m}' in item:
            super(wordlist,self).append({'word':item.split()[0],
                                        'gender':'m',
                                        'definition':" ".join(item[2:-1].split())})
        if '{f}' in item:
            super(wordlist,self).append({'word':item.split()[0],
                                        'gender':'f',
                                        'definition':" ".join(item[2:-1].split())})


def get_random_word(wordlist):
    return(wordlist[int(random.random()*len(wordlist))])

def guess_gender(word):
    print(word['word'])
    guess=""
    while guess!='f' and guess !='m':
        guess=raw_input("is it m or f?").lower()
    if guess==word['gender']:
        print("\033[42mCorrect!\033[0m "+word['word']+ ' is '+['\033[44mMasculine\033[0m','\033[45mFeminine\033[0m'][guess=='f'])
    else:
        print("\033[41mWrong!\033[0m "+word['word']+ ' is '+['\033[44mMasculine\033[0m','\033[45mFeminine\033[0m'][guess=='m'])

def run_n_tests(n,wordlist):
    run=0
    while run<n:
        run+=1
        guess_gender(get_random_word(wordlist))
