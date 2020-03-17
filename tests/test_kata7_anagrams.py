from katas import kata7_anagrams as anagrams
import os

# return the two word anagrams from the list of the input
def test_solve_three_unique_letters():
    assert anagrams.solve('aye', 'yea') == True

def test_solve_three_unique_letters_fail():
    assert anagrams.solve('ear', 'yea') == False

def test_solve_three_nonunique_letters():
    assert anagrams.solve('eye', 'yee') == True

def test_solve_three_nonunique_letters_fail():
    assert anagrams.solve('eye', 'ye') == False
    assert anagrams.solve('eye', 'yae') == False

def test_solve_same_word():
    assert anagrams.solve('eye', 'eye') == False

def test_solve_longer_word():
    assert anagrams.solve('kinship', 'pinkish') == True

def test_solve_list():
    test_list = ['inlets', 'listen', 'silent', 'boats', 'silteb']
    output = ['enlist']
    for item in test_list:
        if anagrams.solve('enlist', item):
            output.append(item)

    assert output == ['enlist', 'inlets', 'listen', 'silent'] 

def test_solve_list_multi():
    wordlist = []
    with open(f'{os.getcwd()}\\tests\\kata7_wordlist.txt', 'r') as f:
        for line in f:
            wordlist.append(line)

    newlist = []
    for textline in wordlist[1:]:
        newlist.extend(textline.split())

    matches = []
    #for word in newlist:
    for comparison in newlist:
        if anagrams.solve(comparison, 'animal'):
            matches.append(("animal", comparison))

    assert matches == [('animal', 'manila')]

def test_solve_whole_file():
    wordlist = []
    with open(f'{os.getcwd()}\\tests\\kata7_wordlist.txt', 'r') as f:
        for line in f:
            wordlist.append(line)

    newlist = []
    for textline in wordlist[1:]:
        newlist.extend(textline.split())

    matches = []
    for word in newlist:
        for comparison in newlist:
            if anagrams.solve(comparison, word):
                matches.append((word, comparison))

    assert len(matches) == 50

# Speed Racer time, goal @ 1.8s
def test_solve_whole_file_large():
    wordlist = []
    with open(f'{os.getcwd()}\\tests\\kata7_full_wordlist.txt', 'r') as f:
        for line in f:
            wordlist.append(line)

    newlist = []
    for textline in wordlist[1:]:
        newlist.extend(textline.split())

    matches = []
    for word in newlist:
        for comparison in newlist:
            if anagrams.solve(comparison, word):
                matches.append((word, comparison))

    assert len(matches) == 20683