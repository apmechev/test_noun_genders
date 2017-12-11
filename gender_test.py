#!/bin/env python
import codecs
import random
import pickle
import os

class wordlist(list):
    def __init__(self,wordfile='nouns_from_wiki.txt'):
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
        return True
    else:
        print("\033[41mWrong!\033[0m "+word['word']+ ' is '+['\033[44mMasculine\033[0m','\033[45mFeminine\033[0m'][guess=='m'])
        return False

def run_n_tests(n,wordlist):
    run=0
    while run<n:
        run+=1
        guess_gender(get_random_word(wordlist))


class WordTest(object):
    def __init__(self,word_list=None,results_file='results'):
        if not word_list:
            self.wordlist=wordlist()
        elif type(word_list)==str and os.path.exists(word_list):
            self.wordlist=wordlist(wordfile=word_list)
        elif type(word_list) == wordlist:
            self.wordlist=wordlist
        self.results_file=results_file

        if os.path.exists(results_file):
            self.results=pickle.load(open(results_file,'rb'))
        else:
            self.results={'T':[],'F':[]} #dictionary holding the correct and false guesses

    def run_random_test(self,num_words=10):
        run=0
        while run<num_words:
            run+=1
            word=get_random_word(self.wordlist)
            if(guess_gender(word)):
                self.results['T'].append(word)
            else:
                self.results['F'].append(word)

    def run_percent_failed(self,perc_failed=0.5):
        """Samples the results and gives a sample 
        of failed previous words. Updates results
        """
        pass

    def store_results(self):
        pickle.dump(self.results,open(self.results_file,'wb'))
