#Thuật toán tìm kiếm nhị phân

def Binarysearch(A,key):

    l=0
    r=len(A)-1
    while l<=r :
        m=(l+r)//2 # toán tử chia làm tròn xuống
        if key==A[m]:
            return m
        elif(key>A[m]):
            l+=1
        else:
            r-=1
    return -1

input_str=input("Enter the element of array:")
my_array=input_str.split()
my_array=[int(x) for x in my_array]
key=input("Enter key: ")
# trước khi thực hiện Binary Search phải sắp xếp lại mảng
my_array.sort()
print(Binarysearch(my_array,int(key)))

