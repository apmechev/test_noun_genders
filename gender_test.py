#!/bin/env python
import codecs
import random
import pickle
import os
import pdb

class wordlist(list):
    def __init__(self,wordfile='nouns_from_wiki.txt'):
        with codecs.open(wordfile,'rb') as wf:
            for line in wf:
#                pdb.set_trace()
                if line[0]!='#':
                    self.append(line.split('\t'))

    def append(self,item):
#        pdb.set_trace()
        result = {}
        result['word'] = item[1]
        result['frequency'] = float(item[17])
        result['gender'] = self.get_gender(item[3])
        result['invariant'] = self.get_invariant(item[3])
        result['notes'] = item[7]
        super(wordlist,self).append(result)

    @staticmethod
    def get_gender(item, gender_dict={'mas':'M', 'fem':"F"}):
        for key in list(gender_dict.keys()):
            if key in item:
                return gender_dict[key]

    @staticmethod
    def get_invariant(item):
        if 'inv' in item:
            return True
        return False



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

class RandomWordTest(WordTest):
    def __init__(self,word_list=None,results_file='results'):
         super(RandomWordTest, self).__init__(
                 word_list=word_list,
                 results_file=results_file)

    def __enter__(self):
        pass


    def __exit__(self,type, value, traceback):
        self.store_results()

class PercentWrongTest(WordTest):
    def __init__(self,word_list=None,results_file='results'):
        super(RandomWordTest, self).__init__(
                 word_list=word_list,
                 results_file=results_file)

    def run_random_test(self,num_words=10,percent_wrong=0.5):
        perc_wrong_wordlist=self.results['F']

