# Đệ quy đầu (Head Recursion)
def calculate_sum(x):
    if x == 1:
        return x
    else:
        return x + calculate_sum(x - 1)

# Đệ quy đuôi (Tail Recursion)
def calculate_sum1(x, running_total=0):
    if x == 0:
        return running_total
    else:
        return calculate_sum1(x - 1, running_total + x)

# Đệ quy Tree (Tree Recursion)
def calculate_sum2(x):
    if x > 0:
        return x + calculate_sum2(x - 1)
    else:
        return x

# Thử nghiệm hàm calculate_sum1
b = calculate_sum1(10, 0)
print(b)

# Thử nghiệm hàm calculate_sum2
c = calculate_sum2(10)
print(c)
