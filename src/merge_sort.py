from typing import List

def merge_sort(list_num: List[int], /) -> List[int]:
    """Sorts a list of numbers using the merge sort algorithm.

    This function is implemented recursively and uses a divide-and-conquer strategy
    to efficiently sort the list. It modifies the list in-place.

    :param list_num: The list of integers to be sorted.
    :type list_num: List[int]
    :return: The sorted list of integers.
    :rtype: List[int]
    """
    if len(list_num) <= 1:
        return list_num
    
    mid = len(list_num) // 2
    left_half = list_num[0: mid]
    right_half = list_num[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = j = k = 0   # i: index for left_half, j: index for right_half, k: index for list_num
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            list_num[k] = left_half[i]
            k += 1
            i += 1
        else:
            list_num[k] = right_half[j]
            k += 1
            j += 1

    while i < len(left_half):
        list_num[k] = left_half[i]
        k += 1
        i += 1

    while j < len(right_half):
        list_num[k] = right_half[j]
        k += 1
        j += 1

    return list_num
