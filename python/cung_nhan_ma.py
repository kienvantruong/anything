def chay_la(ngay,thang):
    print("vui long nhap so hop le!")
    ngay=int(input("Nhap ngay sinh:"))
    thang=int(input("nhap thang sinh:"))
    if 1<= thang <=12 and 1<= ngay <= 31:
        print(kiem_tra_nhan_ma(ngay, thang))
    else:
        print ("ngay thang khong hop le !")
        print("tự chạy lại")

def kiem_tra_nhan_ma(ngay, thang):
    if(thang==11 and ngay >=15) or (thang==12 and ngay <=25):
        return "ban thuoc cung Nhan Ma"
    else:
        return "ban khong thuoc cung Nhan Ma."
try: 
    ngay=int(input("Nhap ngay sinh:"))
    thang=int(input("nhap thang sinh:"))
    if 1<= thang <=12 and 1<= ngay <= 31:
        print(kiem_tra_nhan_ma(ngay, thang))
    else:
        print ("ngay thang khong hop le !")
        print(chay_la(ngay,thang))
except ValueError:
    print("nhap lai")
