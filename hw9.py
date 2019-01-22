import random

verbs_1=[]
verbs_2=[]
clitics=[]
sg_nouns=[]
pl_nouns=[]

def get_words():
    with open('words.txt', encoding='utf-8') as f:
        text = f.read()
        words = text.split()
        for word in words:
            if word=='и':
                clitics.append(word)
            elif word=='но':
                clitics.append(word)
            elif word.endswith('ет'):
                verbs_1.append(word)
            elif word.endswith('ут'):
                verbs_2.append(word)
            elif word.endswith('ют'):
                verbs_2.append(word)
            elif word.endswith('и'):
                pl_nouns.append(word)
            elif word.endswith('ы'):
                pl_nouns.append(word)
            elif word.endswith('a'):
                if word=='a':
                    clitics.append(word)
                else:
                    sg_nouns.append(word)
            else:
                sg_nouns.append(word)

def verb_1():
    return random.choice(verbs_1)

def verb_2():
    return random.choice(verbs_2)

def punctuation():
    punct = ['.', '?', '!', '...']
    return random.choice(punct)

def clitic():
    return random.choice(clitics)

def noun(number):
    if number=='s':
        return random.choice(sg_nouns)
    elif number=='pl':
        return random.choice(pl_nouns)


def sentence_1():
    return noun('s')+' '+verb_1()+' '+noun('s')+' '+','+' '+clitic()+' '+verb_1()+punctuation()

def sentence_2():
    return noun('s')+' '+verb_1()+' '+noun('s')+','+' '+'хотя'+' '+noun('s')+' '+verb_1()+punctuation()

def sentence_3():
    return noun('pl')+' '+verb_2()+' '+noun('s')+','+' '+clitic()+' '+verb_2()+' '+noun('s')+punctuation()

def sentence_4():
    return noun('pl')+' '+verb_2()+' '+noun('s')+','+' '+'хотя'+' '+noun('s')+' '+verb_1()+punctuation()

def sentence_5():
    return noun('s')+' '+verb_1()+' '+noun('s')+','+' '+'хотя'+' '+noun('pl')+' '+verb_2()+' '+noun('s')+punctuation()


def __main__():
    get_words()
    a1=sentence_1()
    a2=sentence_2()
    a3=sentence_3()
    a4=sentence_4()
    a5=sentence_5()
    print(a1, a2, a3, a4, a5)


__main__()



