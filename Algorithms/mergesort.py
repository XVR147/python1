
# Insertion sort between 2 arrays

array = [2, 8, 9, 4, 3, 6, 12]


def sort(a1):
    if len(a1) > 1:

        middle = len(a1)//2
        half1 = a1[:middle]
        half2 = a1[middle:]

        sort(half1)
        sort(half2)

        i = 0
        j = 0
        k = 0

        while i < len(half1) and j < len(half2):
            if half1[i] < half2[j]:
                a1[k] = half1[i]
                i += 1
            else:
                a1[k] = half2[j]
                j += 1
            k += 1

        while i < len(half1):
            a1[k] = half1[i]
            i += 1
            k += 1

        while j < len(half2):
            a1[k] = half2[j]
            j += 1
            k += 1


sort(array)
print(array)
