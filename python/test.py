def date(ngay,thang):
    if (thang == 11 and ngay >= 15) or (thang == 12 and ngay <= 15):
        return print("bạn là cung nhân mã")
    else:
        return print("bạn không phải là cung nhân mã")
try:
    ngay = int(input("ngày sinh của bạn là:"))
    thang = int(input("tháng sinh của bạn là:"))    
    if 1 <= thang <= 12 and 1 <= ngay <= 31:
        print(date(ngay,thang))
    else:
        print("ngày tháng không hộp lệ")
except ValueError:
    print("😑 vui làng nhập lại")
