def insertionSort(A, n):
    for i in range(1, n):
        x = A[i]
        pos = i - 1
        while pos >= 0 and x < A[pos]:
            A[pos + 1] = A[pos]
            pos -= 1
        A[pos + 1] = x

input_str = input('Enter the elements of the array: ')
my_array = input_str.split()
my_array = [int(x) for x in my_array]
insertionSort(my_array, len(my_array))
print('After array sorted:', my_array)
