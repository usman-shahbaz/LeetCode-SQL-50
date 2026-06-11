def dailyTemperatures(temperatures):
    
    n = len(temperatures)
    s = []
    r = [0] * n

    for i in range(n):

        while s and temperatures[i] > temperatures[s[-1]]:
            
            index = s.pop()
            r[index] = i - index

        s.append(i)

    return r
  
