#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary
    ...

    Parameters
    ----------
    a_dictionary : dictionary
        the given dictionary to delete value from

    Return:
        the new dictionary
    """

    while value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break

    return (a_dictionary)
