def combine(n, k):
    
    result = []
    current = []

    def backtrack(start):
        if len(current) == k:
            result.append(current[:])   # Add a copy of current combination
            return

        for i in range(start, n+1):
            
            current.append(i)

            backtrack(i+1)

            current.pop()

    backtrack(1)
    return result
