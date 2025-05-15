def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

so_kiem_tra = int(input("Nhập vào số cần kiểm tra: "))
if kiem_tra_so_nguyen_to(so_kiem_tra):
    print(so_kiem_tra, "là số nguyên tố.")
else:
    print(so_kiem_tra, "không phải là số nguyên tố.")