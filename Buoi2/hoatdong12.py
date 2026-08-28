# ==========================================
# HOAT DONG 1: NHAP/XUAT VA DINH DANG CHUOI
# ==========================================

# Bai tap 1.1 - input() va ep kieu
ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))

print("\n--- Bai 1.1 ---")
print("Ho ten:", ho_ten)
print("Nam sinh:", nam_sinh)
print("Diem trung binh:", diem_tb)


# Bai tap 1.2 - print() voi sep/end
print("\n--- Bai 1.2 ---")

print("Python", "la", "ngon", "ngu", "lap trinh", sep="-")
print("Python", "la", "ngon", "ngu", "lap trinh", sep=", ")
print("Python", "la", "ngon", "ngu", "lap trinh", sep="\n")

print("Dong 1", end=" | ")
print("Dong 2")


# Bai tap 1.3 - 3 cach dinh dang chuoi
print("\n--- Bai 1.3 ---")

# Cach 1: f-string
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")

# Cach 2: str.format()
print("Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(
    ho_ten, nam_sinh, diem_tb
))

# Cach 3: toan tu %
print("Ho ten: %s - Nam sinh: %d - DTB: %.2f"
      % (ho_ten, nam_sinh, diem_tb))


# ==========================================
# HOAT DONG 2: CHU THICH VA TRICH DAN
# ==========================================

print("\n--- Bai 2.1 ---")

# Chu thich mot dong: khai bao thong tin sinh vien

"""
Chu thich/docstring nhieu dong:
Chuong trinh quan ly diem sinh vien - Buoi 2
"""

ho_ten_sv = "Tran Thi B"  # bien luu ho ten
print(ho_ten_sv)


# Bai tap 2.2 - Cac kieu trich dan va escape
print("\n--- Bai 2.2 ---")

s1 = 'Xin chao'
s2 = "Ban co khoe khong?"
s3 = '''Day la
mot chuoi
nhieu dong'''

s4 = "Duong dan: C:\\Python\\data"
s5 = r"Duong dan raw: C:\Python\data"
s6 = "Toi ten la \"Nam\", con ban ten gi?"

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)