#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        print("Length: {:d} - First character: {}".format(0, None))
    else:
        words = sentence.split()
        first_word = words[0]
        first_char = first_word[0]
        length = len(sentence)
        print("Length: {:d} - First character: {}".format(length, first_char))
