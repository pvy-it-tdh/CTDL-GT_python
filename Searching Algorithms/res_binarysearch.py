def binarySearch_res(A,key,l,r):
    if l>r:
        return -1
    else:
        m=(l+r)//2
        if key==A[m]:
            return  m
        elif(key>A[m]):
            return binarySearch_res(A,key,m+1,r)
        else:
            return binarySearch_res(A,key,l,m-1)

input_str=input("Enter the element of array: ")
my_array=input_str.split()
my_array=[int(x) for x in my_array]
my_array.sort()
key=input('Enter key: ')
print(binarySearch_res(my_array,int(key),0,len(my_array)-1))