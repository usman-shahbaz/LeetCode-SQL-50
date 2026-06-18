def productExceptSelf(nums):

    n = len(nums)
    ls = [1] * n
    rs = [1] * n
    res = [1] * n

    for i in range(1, n):
        ls[i] = nums[i-1] * ls[i-1]

    for i in range(n-2, -1, -1):
        rs[i] = nums[i+1] * rs[i+1]

    for i in range(n):
        res[i] = ls[i] * rs[i]
    
    return res
