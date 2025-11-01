from typing import List


def insertion_sort(list_numb: List[int]) -> List[int]:
    """
    Sorts a list using Insertion Sort algorithm.
    
    Idea: Build the sorted list one element at a time by inserting new elements in the correct spot.

    :param list: The list to be sorted
    :type list: List[int]
    :return: The sorted list
    :rtype: List[int]
    """
    for i in range(2,len(list_numb)+1):               
        for j in range(1,i):  
            if list_numb[i-1] < list_numb[j-1]:
                list_numb[i-1], list_numb[j-1] = list_numb[j-1], list_numb[i-1]
    return list_numb
