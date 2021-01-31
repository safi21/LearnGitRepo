l = [334, 34, 235, 234, 564, 7, 45]
for k in range(0, len(l) - 1):
    mp = k
    for n in range(k + 1, len(l)):
        if l[n] < l[mp]:
            mp = n
    temp = l[k]
    l[k] = l[mp]
    l[mp] = temp

    print(l)
