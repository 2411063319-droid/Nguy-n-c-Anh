# ==========================================
# HOAT DONG 3: NUMBER
# ==========================================

# Bai tap 3.1 - Cac kieu so va chuyen doi
print("===== BAI 3.1 =====")

so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j

print(type(so_nguyen), type(so_thuc), type(so_phuc))

print(float(so_nguyen))   # ep int -> float
print(int(so_thuc))       # ep float -> int, cat phan thap phan


# Bai tap 3.2 - Ham built-in xu ly so
print("\n===== BAI 3.2 =====")

a = -7
b = 2.6789
c, d = 17, 5

print(abs(a))          # gia tri tuyet doi
print(round(b))        # lam tron
print(round(b, 2))     # lam tron 2 chu so thap phan
print(pow(c, 2))       # c mu 2
print(divmod(c, d))    # tra ve (thuong, du)

# So sanh pow() va **
print("pow(c, 2) =", pow(c, 2))
print("c ** 2 =", c ** 2)


# Bai tap 3.3 - Phuong trinh bac hai
print("\n===== BAI 3.3 =====")

import math

a, b, c = 1, -3, 2

delta = b ** 2 - 4 * a * c

x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")


# ==========================================
# HOAT DONG 4: STRING
# ==========================================

# Bai tap 4.1 - Indexing va slicing
print("\n===== BAI 4.1 =====")

cau = "Lap trinh Python rat thu vi"

print(cau[0])       # ky tu dau tien
print(cau[-1])      # ky tu cuoi cung
print(cau[4:10])
print(cau[:8])
print(cau[11:])
print(cau[::-1])    # dao nguoc chuoi

# Kiem tra palindrome
print("Chuoi dao nguoc:", cau[::-1])
print("Co phai palindrome khong?", cau == cau[::-1])


# Bai tap 4.2 - Tinh bat bien cua String
print("\n===== BAI 4.2 =====")

ten = "Nam"

# Dong nay neu bo dau # se gay loi TypeError
# ten[0] = "T"

ten_moi = "T" + ten[1:]

print("Ten ban dau:", ten)
print("Ten moi:", ten_moi)


# Bai tap 4.3 - Cac phuong thuc xu ly chuoi
print("\n===== BAI 4.3 =====")

cau = " Toi dang HOC Python rat vui "

print(cau.strip())
print(cau.strip().upper())
print(cau.strip().lower())
print(cau.strip().replace("HOC", "hoc"))
print(cau.strip().split())
print(len(cau.strip().split()))
print(cau.count("o"))
print(cau.find("Python"))
print(cau.strip().startswith("Toi"))
print(cau.strip().endswith("vui"))
print("-".join(["Python", "that", "thu", "vi"]))


# Bai tap 4.4 - Chuan hoa ho ten
print("\n===== BAI 4.4 =====")

ho_ten_tho = " nguyen van an "

ho_ten_sach = " ".join(ho_ten_tho.split()).title()

print("Ho ten ban dau:", ho_ten_tho)
print("Ho ten sau khi chuan hoa:", ho_ten_sach)