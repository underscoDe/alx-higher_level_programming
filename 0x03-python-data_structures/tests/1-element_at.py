#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves an element at a given index
    ...

    Parameters
    ----------
    my_list : list
        The list of integers
    idx : integer
        The given index

    Return:
        The element when found
        None if the index is negative
        None if the index is larger than the list length
    """

    if idx < 0 or idx > (len(my_list) - 1):
        return None
    else:
        return my_list[idx]
