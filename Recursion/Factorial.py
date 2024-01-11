#Hàm giai thừa viết bằng đệ quy
def Factorial_res(n):
    if n==0 or n==1:
        return 1
    else:
        return Factorial_res(n-1)*n

n=input('Enter number: ')
num=int(n)
print(Factorial_res(num))