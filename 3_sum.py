def threeSum(nums):

    res = []
    nums.sort()
    n = len(nums)
    
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        
        l = i+1
        r = n-1
        while l < r:

            ts = a + nums[l] + nums[r]
            if ts < 0:
                l += 1
            elif ts > 0:
                r -= 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res
