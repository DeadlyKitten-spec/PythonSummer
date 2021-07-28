def sort_array(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                temp = a[j + 1]
                a[j + 1] = a[j]
                a[j] = temp
    return a, 1

a = input().split()
b = [0] * len(a)
for i in range(len(a)):
    b[i] = int(a[i])
print(b)
b, c = sort_array(b)
print(b, c)