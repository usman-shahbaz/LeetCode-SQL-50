
def mySqrt(x: int) -> int:
    if x < 2:  # 0 and 1 cases
        return x
    
    left, right = 1, x // 2
    ans = 1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans


print(mySqrt(4))  # 2
print(mySqrt(8))  # 2
print(mySqrt(0))  # 0
print(mySqrt(1))  # 1
print(mySqrt(15)) # 3
