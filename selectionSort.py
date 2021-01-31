def selsort(x):
    for i in range(len(x) - 1):
        min_pos = i
        for j in range(i + 1, len(x)):
            if x[j] < x[min_pos]:
                min_pos = j
        x[i], x[min_pos] = x[min_pos], x[i]
    print(x)


lst = [35, 2354, 234345, 23432, 45345, 234, 23, 4, 243, 67, 45, 5, 2234, 2]
selsort(lst)
# This is done with simple scripting.
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
