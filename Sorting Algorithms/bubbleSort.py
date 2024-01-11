# BubbleSort
def BubbleSort(A):
    n=len(A)
    # for pass=n-1 ,pass >=0,pass--
    for passes in range(n-1,0,-1):
        for i in range(passes):
            if A[i]>A[i+1]:
                temp=A[i]
                A[i]=A[i+1]
                A[i+1]=temp

input_str=input('Enter the element of array: ')
my_array=input_str.split()
my_array=[int(x) for x in my_array]
BubbleSort(my_array)
print('After my array sort: ',my_array)
