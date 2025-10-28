from src.merge_sort import merge_sort


def test_merge_sort():
    test_cases = [
        ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([42], [42]),
        ([2, 2, 2, 2], [2, 2, 2, 2]),
        ([], []),
        ([10, -5, 0, 3, -2], [-5, -2, 0, 3, 10])
    ]

    for i, (nums, expected) in enumerate(test_cases, start=1):
        result = merge_sort(nums.copy())
        if result == expected:
            print(f"Test {i} passed")
        else:
            print(f"Test {i} failed: got {result}, expected {expected}")

# Run tests
if __name__ == '__main__':
    test_merge_sort()
