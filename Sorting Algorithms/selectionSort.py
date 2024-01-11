# Hàm sắp xếp chọn
def selectionSort(A):
    n=len(A)
    for i in range(n-1):
        position=i
        for j in range(i+1,n):
            if(A[j]<A[position]):
                position=j
        temp=A[i]
        A[i]=A[position]
        A[position]=temp

input_str=input("Enter the element of array: ")
my_array=input_str.split()
my_array= [int(x) for x in my_array]
selectionSort(my_array)
print('After array sorted: ',my_array)
