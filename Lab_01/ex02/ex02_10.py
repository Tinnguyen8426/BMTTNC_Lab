def dao_ngược_chuoi(chuoi):
    return chuoi[::-1]

input_string = input("Mời nhập chuỗi cần đảo ngược: ")
print("Chuỗi đảo ngược là:", dao_ngược_chuoi(input_string))