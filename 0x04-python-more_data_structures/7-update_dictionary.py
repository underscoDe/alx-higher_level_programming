#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary
    ...

    Parameters
    ----------
    a_dictionary : dictionary
        the given dictionary
    key : string
        argument will be always a string
    value : any type
        argument will be any type

    Return:
        the dictionary with the new inserted value
    """

    a_dictionary[key] = value
    return (a_dictionary)
