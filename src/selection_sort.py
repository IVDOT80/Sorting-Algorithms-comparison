from typing import List


def selection_sort(list_numb: List[int]) -> List[int]:
    """Sorts a list using Selection Sort algorithm.

    Idea: Repeatedly find the smallest remaining element and put it at the front.

    :param list: The list to be sorted
    :type list: List[int]
    :return: The sorted list
    :rtype: List[int]
    """
    for i in range(len(list_numb)):
        for j in range(i + 1, len(list_numb)):
            if list_numb[i] > list_numb[j]:
                list_numb[i], list_numb[j] = list_numb[j], list_numb[i]
    return list_numb
