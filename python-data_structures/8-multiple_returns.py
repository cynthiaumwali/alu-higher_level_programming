#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        print("Length: {:d} - First character: {}".format(0, None))
    else:
        first_char = sentence[0]
        length = len(sentence)
        print("Length: {:d} - First character: {}".format(length, first_char))
