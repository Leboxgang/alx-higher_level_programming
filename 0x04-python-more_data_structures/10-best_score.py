#!/usr/bin/python3
def best_score(my_dict):
    # Return the key with the largest value in the dictionary
    return max(my_dict, key=my_dict.get) if my_dict else None
