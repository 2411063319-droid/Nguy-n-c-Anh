def nhap_so_nguyen(loi_nhac):
    while True:
        try:
            so = int(input(loi_nhac))
            return so
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap mot so nguyen.")


def nhap_diem():
    while True:
        try:
            diem = float(input("Nhap diem: "))

            if 0 <= diem <= 10:
                return diem

            print("-> Diem phai nam trong khoang tu 0 den 10.")

        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap mot so.")


danh_sach_sinh_vien = [
    {
        "ma_sv": "2411063319 ",
        "ho_ten": "Nguyen Duc Anh",
        "tuoi": 20,
        "diem": 8.5
    },
    {
        "ma_sv": "2411063319 ",
        "ho_ten": "Tran Thi Binh",
        "tuoi": 19,
        "diem": 7.5
    },
    {
        "ma_sv": "2411063319 ",
        "ho_ten": "Le Van Cuong",
        "tuoi": 21,
        "diem": 9.0
    }
]


def tim_sinh_vien_theo_ma(ma_sv):
    for sinh_vien in danh_sach_sinh_vien:
        if sinh_vien["ma_sv"] == ma_sv:
            return sinh_vien
    return None


def hien_thi_danh_sach():
    if len(danh_sach_sinh_vien) == 0:
        print("-> Danh sach sinh vien dang rong.")
        return

    print("\n" + "=" * 70)
    print(
        f"{'Ma SV':<10}"
        f"{'Ho ten':<25}"
        f"{'Tuoi':<10}"
        f"{'Diem':<10}"
        f"{'Xep loai':<15}"
    )
    print("-" * 70)

    for sinh_vien in danh_sach_sinh_vien:
        diem = sinh_vien["diem"]

        if diem >= 8:
            xep_loai = "Gioi"
        elif diem >= 6.5:
            xep_loai = "Kha"
        elif diem >= 5:
            xep_loai = "Trung binh"
        else:
            xep_loai = "Yeu"

        print(
            f"{sinh_vien['ma_sv']:<10}"
            f"{sinh_vien['ho_ten']:<25}"
            f"{sinh_vien['tuoi']:<10}"
            f"{diem:<10.1f}"
            f"{xep_loai:<15}"
        )

    print("=" * 70)


def them_sinh_vien():
    print("\n--- THEM SINH VIEN ---")

    ma_sv = input("Nhap ma sinh vien: ").strip()

    if tim_sinh_vien_theo_ma(ma_sv) is not None:
        print("-> Ma sinh vien da ton tai, khong the them.")
        return

    ho_ten = input("Nhap ho ten: ").strip()

    while ho_ten == "":
        print("-> Ho ten khong duoc de trong.")
        ho_ten = input("Nhap ho ten: ").strip()

    tuoi = nhap_so_nguyen("Nhap tuoi: ")

    while tuoi <= 0:
        print("-> Tuoi phai lon hon 0.")
        tuoi = nhap_so_nguyen("Nhap tuoi: ")

    diem = nhap_diem()

    sinh_vien_moi = {
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "tuoi": tuoi,
        "diem": diem
    }

    danh_sach_sinh_vien.append(sinh_vien_moi)

    print("-> Them sinh vien thanh cong.")


def tim_kiem_sinh_vien():
    print("\n--- TIM KIEM SINH VIEN ---")

    ma_sv = input("Nhap ma sinh vien can tim: ").strip()

    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    if sinh_vien is None:
        print("-> Khong tim thay sinh vien.")
        return

    print("\nThong tin sinh vien:")
    print("Ma sinh vien:", sinh_vien["ma_sv"])
    print("Ho ten:", sinh_vien["ho_ten"])
    print("Tuoi:", sinh_vien["tuoi"])
    print("Diem:", sinh_vien["diem"])


def sua_sinh_vien():
    print("\n--- SUA THONG TIN SINH VIEN ---")

    ma_sv = input("Nhap ma sinh vien can sua: ").strip()

    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    if sinh_vien is None:
        print("-> Khong tim thay sinh vien.")
        return

    print("Thong tin hien tai:")
    print("Ho ten:", sinh_vien["ho_ten"])
    print("Tuoi:", sinh_vien["tuoi"])
    print("Diem:", sinh_vien["diem"])

    ho_ten_moi = input("Nhap ho ten moi: ").strip()

    while ho_ten_moi == "":
        print("-> Ho ten khong duoc de trong.")
        ho_ten_moi = input("Nhap ho ten moi: ").strip()

    tuoi_moi = nhap_so_nguyen("Nhap tuoi moi: ")

    while tuoi_moi <= 0:
        print("-> Tuoi phai lon hon 0.")
        tuoi_moi = nhap_so_nguyen("Nhap tuoi moi: ")

    diem_moi = nhap_diem()

    sinh_vien["ho_ten"] = ho_ten_moi
    sinh_vien["tuoi"] = tuoi_moi
    sinh_vien["diem"] = diem_moi

    print("-> Cap nhat thong tin thanh cong.")


def xoa_sinh_vien():
    print("\n--- XOA SINH VIEN ---")

    ma_sv = input("Nhap ma sinh vien can xoa: ").strip()

    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    if sinh_vien is None:
        print("-> Khong tim thay sinh vien.")
        return

    danh_sach_sinh_vien.remove(sinh_vien)

    print("-> Xoa sinh vien thanh cong.")


def thong_ke_sinh_vien():
    print("\n--- THONG KE SINH VIEN ---")

    if len(danh_sach_sinh_vien) == 0:
        print("-> Chua co sinh vien nao.")
        return

    tong_so = len(danh_sach_sinh_vien)

    so_gioi = 0
    so_kha = 0
    so_trung_binh = 0
    so_yeu = 0
    tong_diem = 0

    for sinh_vien in danh_sach_sinh_vien:
        diem = sinh_vien["diem"]
        tong_diem += diem

        if diem >= 8:
            so_gioi += 1
        elif diem >= 6.5:
            so_kha += 1
        elif diem >= 5:
            so_trung_binh += 1
        else:
            so_yeu += 1

    diem_trung_binh = tong_diem / tong_so

    print("Tong so sinh vien:", tong_so)
    print("So sinh vien Gioi:", so_gioi)
    print("So sinh vien Kha:", so_kha)
    print("So sinh vien Trung binh:", so_trung_binh)
    print("So sinh vien Yeu:", so_yeu)
    print("Diem trung binh cua lop:", round(diem_trung_binh, 2))


def hien_thi_menu():
    print("\n")
    print("=" * 50)
    print("       CHUONG TRINH QUAN LY SINH VIEN")
    print("=" * 50)
    print("1. Hien thi danh sach sinh vien")
    print("2. Them sinh vien")
    print("3. Tim kiem sinh vien")
    print("4. Sua thong tin sinh vien")
    print("5. Xoa sinh vien")
    print("6. Thong ke sinh vien")
    print("0. Thoat chuong trinh")
    print("=" * 50)


def main():
    while True:
        hien_thi_menu()

        lua_chon = input("Nhap lua chon cua ban: ")

        if lua_chon == "1":
            hien_thi_danh_sach()

        elif lua_chon == "2":
            them_sinh_vien()

        elif lua_chon == "3":
            tim_kiem_sinh_vien()

        elif lua_chon == "4":
            sua_sinh_vien()

        elif lua_chon == "5":
            xoa_sinh_vien()

        elif lua_chon == "6":
            thong_ke_sinh_vien()

        elif lua_chon == "0":
            print("-> Cam on ban da su dung chuong trinh.")
            break

        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
    main()