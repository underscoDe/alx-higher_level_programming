#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list
    ...

    Parameters
    ----------
    my_list : list
        Initial list of elements
    search : integer
        The element to replace in the list
    replace : integer
        The new element

    Return:
        a new list with the new elements
    """

    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
