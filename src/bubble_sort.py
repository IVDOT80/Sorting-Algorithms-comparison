from typing import List


def bubble_sort(list_numb: List[int],/) -> List[int]:
    """
    Sorts a list using Bubble Sort algorithm.

    Idea: Compare neighbors, swap if wrong order. After each pass, the biggest element moves to the end.

    :param list: The list to be sorted
    :type list: List[int]
    :return: The sorted list
    :rtype: List[int]
    """
    for _ in range(len(list_numb)-1):    
        for i in range(len(list_numb)-1):
            if list_numb[i] > list_numb[i+1]:
                list_numb[i+1],list_numb[i] = list_numb[i], list_numb[i+1]
    return list_numb
