#!/usr/bin/python3
# Function to return a list of booleans indicating divisibility by 2
def divisible_by_2(my_list=[]):
    return [num % 2 == 0 for num in my_list]
