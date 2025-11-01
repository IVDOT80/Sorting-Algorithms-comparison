from src.bubble_sort import bubble_sort
from src.insertion_sort import insertion_sort
from src.merge_sort import merge_sort
from src.quick_sort import quick_sort
from src.selection_sort import selection_sort


def test_sort(func):
    test_cases = [
        ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([42], [42]),
        ([2, 2, 2, 2], [2, 2, 2, 2]),
        ([], []),
        ([10, -5, 0, 3, -2], [-5, -2, 0, 3, 10]),
        ([-2, 0, -5, 3, 1] ,[-5, -2, 0, 1, 3])
    ]

    print(f'Here we have the testing results for "{func.__name__}": \n')

    for i, (nums, expected) in enumerate(test_cases, start=1):
        result = func(nums.copy())
        if result == expected:
            print(f"Test {i} passed")
        else:
            print(f"Test {i} failed: got {result}, expected {expected}")
    
    print('---'*10, '\n')

# Run tests
if __name__ == '__main__':
    test_sort(merge_sort)
    test_sort(bubble_sort)
    test_sort(insertion_sort)
    test_sort(selection_sort)
    test_sort(quick_sort)
