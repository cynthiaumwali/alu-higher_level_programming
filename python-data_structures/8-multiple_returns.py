#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        print("Length: {:d} - First character: {}".format(0, None))
    else:
        length = len(sentence)
        first_char = sentence[0]
        print("Length: {:d} - First character: {}".format(length, first_char))
