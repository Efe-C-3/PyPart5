import math
from typing import List
from math import ceil


def get_item_at_position(list_in: List, pos: int) -> List:
    """
    Returns the item at pos.

    :param list_in: Input list
    :param pos: Position of desired item in list_in
    :return: Item in pos
    """

    result = list_in[pos]
    return result


def print_list_items(list_in: List) -> None:
    """
    Given a list, this function iterates through it and prints each element.

    :param list_in: Input list
    :return: None
    """
    for item in list_in:
        print(item)


def sort_by_commit_count(list_in: List) -> List:
    """
    Given a list of entries, return a new list sorted based on the commit count.

    :param list_in: A list where each entry is a list containing a name and the commit count corresponding to a user
    :return: The same list sorted in ascending order based on the commit count
    """
    result = sorted(list_in, key=lambda x: x[1])
    return result

def gen_list_of_nums(n: int) -> List[int]:
    """
    Given a number (N), this function returns a list of integers from 0 to N (exclusive).

    :param n: The number of items the result should contain
    :return: A list of integers
    """
    List = []
    for i in range(0, n):
        List.append(i)
    return List


def half_list(list_in: List, half: int) -> List:
    """
    Given a list, this function will return a new list that contains half of the items in the list_in parameter.

    :param list_in: The list which will be used to generate the return value
    :param half: 1 will use the first half of the input list. 2 will use the second half of the input list.
    If the length of list_in is an odd number, round the half value up (hint: math.ceil()).
    :return: A list.
    """
    length = len(list_in)
    if half == 1:
        if length % 2 == 0:
            half_even = length // 2
            return list_in[:half_even]
        else:
            half_odd = math.ceil(length // 2 + 1)
            return list_in[:half_odd]
    elif half ==2:
        if length % 2 == 0:
            half_even = length // 2
            return list_in[half_even:]
        else:
            half_odd = math.ceil(length // 2)
            return list_in[half_odd:]
    else:
        return "invalid"






def remove_odds(list_in: List[int]) -> None:
    """
    Given a list of integers, this function removes the odd numbers from the same list.

    :return: None
    """
    for i in list_in[:]:
        if i % 2 != 0:
            list_in.remove(i)
    return list_in


def remove_evens(list_in: List[int]) -> None:
    """
    Given a list of integers, this function removes the even numbers from the same list.

    :return: None
    """
    for i in list_in:
        if i % 2 == 0:
            list_in.remove(i)
    return list_in


def concatenate_lists(list_a: List, list_b: List) -> List:
    """
    Given two lists, this function combines them and returns the result as a new list.

    :param list_a: A list
    :param list_b: Another list
    :return: A list containing all elements from list_a and list_b
    """
    result = list_a + list_b
    return result


def multiply_list(list_in: List, scalar: int) -> List:
    """
    Given a list and an integer, this function will return a new list which is the result of multiplying
    the input list by the value of the scalar.

    :param list_in: A list
    :param scalar: An integer
    :return: A list
    """
    result = list_in * scalar
    return result
