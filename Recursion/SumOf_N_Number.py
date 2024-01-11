def sum_rec(n):
    if n==0:
        return 0
    else:
        return sum_rec(n-1)+n


num=input('Enter number: ')
# Do hàm input trả về một chuỗi nên mình phải ép kiểu cho num
n=int(num)
# Hoặc chúng ta cũng có thể code vậy print(sum_rec(int(num))
print(sum_rec(n))