nn = int(input("Enter the length: "))
lst = []
for ii in range(nn):
    inn = int(input("Enter list element: "))
    lst.append(inn)


def selsort(x):
    for i in range(len(x) - 1):
        min_pos = i
        for j in range(i + 1, len(x)):
            if x[j] < x[min_pos]:
                min_pos = j
        x[i], x[min_pos] = x[min_pos], x[i]
    print(x)


selsort(lst)
