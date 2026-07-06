#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        new_tuple = (None, 0)
        return new_tuple
    else:
        words = sentence.split()
        first_word = words[0]
        length = len(sentence)
        new_tuple = (first_word, length)
        return new_tuple
