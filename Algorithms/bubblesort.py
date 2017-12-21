# Bubblesort in python

unsortedArray = [2, 8, 9, 4, 3, 6, 12]
print(unsortedArray)


def swap(pos):
    tmp = unsortedArray[pos]
    unsortedArray[pos] = unsortedArray[pos+1]
    unsortedArray[pos+1] = tmp


for i in range(len(unsortedArray)-1, 1, -1):
    for j in range(0, i-1, 1):
        if unsortedArray[j] > unsortedArray[j+1]:
            swap(j)

print(unsortedArray)
