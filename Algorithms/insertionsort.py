# Insertion sort in python

unsortedArray = [2, 8, 9, 4, 3, 6, 12]
print(unsortedArray)

def swap(pos):
    tmp = unsortedArray[pos]
    unsortedArray[pos] = unsortedArray[pos+1]
    unsortedArray[pos+1] = tmp

for i in range(1,len(unsortedArray)-1):
    print("Ciclo ")
    j = i
    while j>0 and unsortedArray[j] < unsortedArray[j-1]:
        swap(j-1)
        j = j-1

print(unsortedArray)
