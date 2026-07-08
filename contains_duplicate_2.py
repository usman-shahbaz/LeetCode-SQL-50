def containsNearbyDuplicate(nums, k):
    
    n = len(nums)
    i = 0
    f = {}

    for i, num in enumerate(nums):
        if num in f and i - f[num] <= k:
                return True
        f[num] = i
    return False
