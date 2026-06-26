def topKFrequent(words, k):
        
        f = Counter(words)
        h = []

        for w, c in f.items():
            heapq.heappush(h, (c, w))

            if len(h) > k:
                heapq.heappop(h)

        return [ h[1] for h in h ][::-1]
