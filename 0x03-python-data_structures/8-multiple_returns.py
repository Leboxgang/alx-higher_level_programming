#!/usr/bin/python3
# Function to return the length and first character of a string
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
