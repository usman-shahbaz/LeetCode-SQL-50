def trap(height):
    if not height:
        return 0

    left_max = [0] * len(height)
    right_max = [0] * len(height)
    water_trapped = 0
    
    # Calculate the maximum height of bars to the left of each bar
    left_max[0] = height[0]
    for i in range(1, len(height)):
        left_max[i] = max(left_max[i - 1], height[i])
    
    # Calculate the maximum height of bars to the right of each bar
    right_max[-1] = height[-1]
    for i in range(len(height) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])
    
    # Calculate the amount of water trapped at each bar
    for i in range(len(height)):
        water_trapped += min(left_max[i], right_max[i]) - height[i]
    
    return water_trapped
        
