def frequencySort(s):

    f = Counter(s)
    res = []

    c = sorted(f.items(), key=lambda x:x[1], reverse=True)

    for ch, fr in c:
        res.append(ch * fr)

    return ''.join(res)
