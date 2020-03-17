def solve(word_one, word_two):
    if len(word_one) is not len(word_two):
        return False

    if word_one == word_two:
        return False

    new_word_two = list(word_two)
    for letter in word_one:
        position = new_word_two.__contains__(letter)
        if position:
            del new_word_two[new_word_two.index(letter)]
        else:
            return False

    return True
            
