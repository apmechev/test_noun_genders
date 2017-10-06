
def make_nouns_file(dictccfile,nounfile='nouns.txt'):
    nouns=[]
    with open(dictccfile,'rb') as full_file:
        for line in full_file:
            if '{m}' in line or '{f}' in line:
                nouns.append(line)
    print len(nouns)
    with open(nounfile,'wb') as noun_file:
        for i in nouns:
            noun_file.write(i)
