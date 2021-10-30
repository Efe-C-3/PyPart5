
def str_len(str_in: str) -> str:
    """
    Given a string parameter, this function should return the length of the parameter.
    """
    result = len(str_in)
    return result


def first_char(str_in: str) -> str:
    """
    Given a string parameter, this function should return the first letter of the parameter.
    """
    first_letter = str_in[0]
    return first_letter


def last_char(str_in: str) -> str:
    """
    Given a string parameter, this function should return the last letter of the parameter..
    """
    last_letter = str_in[-1]
    return last_letter


def input_has_substring(str_in: str, sub_str_in: str) -> bool:
    """
    This function determines if the substring exists within the string. Returns True or False.
    """
    def checking_substring():
        if sub_str_in in str_in:
            return True
        else:
            return False

    return checking_substring()


def substring(str_in: str, start: int, stop: int) -> str:
    """
    Returns the substring of a string.

    Keyword arguments:
    str_in -- the string in which to generate a substring from
    start -- starting position of the input parameter to start the substring (inclusive)
    stop -- stopping position of the input parameter to stop the substring (exclusive)
    """
    substring_of_string = str_in[start:stop]
    return substring_of_string


def opposite_case(str_in: str) -> str:
    """
    Given a string parameter, this function returns the same string back with each letter having the opposite case.
    Example: 
    When input = "Python" the function returns "pYTHON"
    """
    length = len(str_in)
    result = ""
    for i in range(length):
        if str_in[i] .islower():
            result += str_in[i].upper()
        elif str_in[i].isupper():
            result += str_in[i].lower()
        else:
            result += str_in
    return result
