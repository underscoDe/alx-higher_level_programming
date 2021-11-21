#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list
    ...

    Parameters
    ----------
    my_list : list
        The list to remove item from
    idx : integer
        The given position

    Return:
        The same list if idx is negative
         the list without the deleted item
    """

    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
