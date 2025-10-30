import random
from typing import List

random.seed(80)


def quick_sort(lis: List[int]) -> List[int]:
    """
    Sorts a list using the quicksort algorithm with random pivot selection.
    
    This implementation randomly selects a pivot element to improve performance
    on already sorted or reverse-sorted input lists. The function recursively
    partitions the list into elements less than, equal to, and greater than
    the pivot, then combines the sorted partitions.
    
    :param lis: The list to be sorted. Can contain any comparable elements.
    :type lis: list
    :return: A new list containing all elements from the input list in ascending order.
    :rtype: list
    """
    if len(lis) == 0 or len(lis) == 1:  # Recursion stopping expression
        return lis

    pivot = lis.index(random.choice(lis))

    left_half = []
    right_half = []
    mid = []

    for i in range(len(lis)):
        if lis[i] < lis[pivot]:
            left_half.append(lis[i])
        elif lis[i] > lis[pivot]:
            right_half.append(lis[i])
        else:
            mid.append(lis[i])

    left_sort = quick_sort(left_half)
    right_sort = quick_sort(right_half)

    return left_sort + mid + right_sort
