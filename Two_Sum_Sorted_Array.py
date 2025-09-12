
def twoSum(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            return [left + 1, right + 1]
        elif total > target:
            right -= 1
        else:
            left += 1


# Test case 1: numbers = [2, 7, 11, 15], target = 9
test_case_1 = [2, 7, 11, 15]
target_1 = 9
result_1 = twoSum(test_case_1, target_1)
print(f"Test case 1 result: {result_1}")


# Test case 2: numbers = [-1, 0, 3, 5, 9], target = 4
test_case_2 = [-1, 0, 3, 5, 9]
target_2 = 4
result_2 = twoSum(test_case_2, target_2)
print(f"Test case 2 result: {result_2}")
