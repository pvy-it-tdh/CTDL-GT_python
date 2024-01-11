def linearsearch(A,key):
    index=0
    while index<len(A):
        if A[index]==key:
            return index
        index+=1
    return -1

# Nhập chuỗi tù nguời dùng
input_str=input('Enter the elements of the array :')
my_array=input_str.split()
# Chuyển dổi mỗi phần tử trong mảng thành số nguyên
my_array=[int(x) for x in my_array]
key=input('Enter key:')
print(linearsearch(my_array,int(key)))