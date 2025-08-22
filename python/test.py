import time

for i in range(10):
    i = (i+1)% 2
    time.sleep(1)
    print(i)
# % là tính số dư: VD:7 % 3 = 1 (7 chia 3 bằng 2 dư 1)
