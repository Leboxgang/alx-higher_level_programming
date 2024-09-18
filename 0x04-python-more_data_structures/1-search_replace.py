#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Replace all occurrences of 'search' with 'replace' in the list
    return [replace if search == n else n for n in my_list]
