def removeDuplicates(nums):
    
    n = len(nums)
    f = Counter(nums)
    j = 0
    c = 1

    for i in range(1, n):
        if nums[i] == nums[j]:
            c += 1
        else:
            c = 1

        if c <= 2:
            j += 1
            nums[j] = nums[i]
    return j + 1
