import keyboard
x1 = ["o","o","o","o","o","o","o","o","o","o"]
x2 = ["o","o","o","o","o","o","o","o","o","o"]
x3 = ["o","o","o","o","o","o","o","o","o","o"]
x4 = ["o","o","o","o","o","o","o","o","o","o"]
x5 = ["o","o","o","o","o","o","o","o","o","o"]
x6 = ["o","o","o","o","o","o","o","o","o","o"]
x7 = ["o","o","o","o","o","o","o","o","o","o"]
x8 = ["o","o","o","o","o","o","o","o","o","o"]
x9 = ["o","o","o","o","o","o","o","o","o","o"]
x10 = ["o","o","o","o","o","o","o","o","o","o"]
map = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
a = len(map)
for i in range(a):
    for j in range(a):
        print(map[i][j], end=" ")
    print()

