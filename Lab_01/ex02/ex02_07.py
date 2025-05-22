print("Nhập các dòng văn bản (nhập 'done' để két thúc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\n Các dòng đã nhập sau khi cuyển thành chũ in hoa: ")
for line in lines:
    print(line.upper())