def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    value = "".join(value.split()).lower()
    if len(value) <= 1:
        return True
    if value[0] != value[-1]:
        return False
    return is_palindrome(value[1:-1])

