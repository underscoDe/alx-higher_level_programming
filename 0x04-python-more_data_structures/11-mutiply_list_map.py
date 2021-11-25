#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    """
    Returns a list with all values
     multiplied by a number without using any loops
    ...

    Parameters
    ----------
    my_list : list
        the list of values
    number : integer

    Return:
        a new list:
         Same length as my_list
         Each value should be multiplied by number
    """

    return (list(map(lambda x: x*number, my_list)))
