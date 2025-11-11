import sys
import time
from typing import Callable, List


def measure_time(func: Callable,/, list: List[int]) -> float:
    """
    Measures time complexity of a function

    :param func: The function to test
    :type func: Callable
    :param list: The list to pass to the function
    :type list: List[int]
    :return: The time taken by the function
    :rtype: float
    """ 
    start_time = time.perf_counter()
    func(list)
    end_time = time.perf_counter()
    return end_time - start_time

def measure_space(func: Callable,/, list: List[int]) -> int:
    """
    Measures space complexity of a function

    :param func: The function to test
    :type func: Callable
    :param list: The list to pass to the function
    :type list: List[int]
    :return: The memory used by the list
    :rtype: int
    """ 
    start_memory = sys.getsizeof(list)
    func(list)
    end_memory = sys.getsizeof(list)
    return end_memory - start_memory
