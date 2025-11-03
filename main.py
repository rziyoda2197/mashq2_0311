class Hayvon:
    def __init__(self, turi, ovoz):
        self.turi = turi
        self.ovoz = ovoz

    def malumot(self):
        info = (
            "==============================\n"
            f"🐾 Hayvon ma’lumotlari\n"
            "==============================\n"
            f"Turi : {self.turi}\n"
            f"Ovoz : {self.ovoz}\n"
            "=============================="
        )
        return info

    def ovoz_chiqar(self):
        print(f"{self.turi} ovoz chiqaryapti: {self.ovoz}!")


class Kuchuk(Hayvon):
    def __init__(self, nomi):
        super().__init__("Kuchuk", "Hov-hov")
        self.nomi = nomi

    def malumot(self):
        info = (
            "==============================\n"
            f"🐶 Kuchuk ma’lumotlari\n"
            "==============================\n"
            f"Nomi : {self.nomi}\n"
            f"Turi : {self.turi}\n"
            f"Ovoz : {self.ovoz}\n"
            "=============================="
        )
        return info

    def ovoz_chiqar(self):
        print(f"{self.nomi} hovlayapti: {self.ovoz}!")


class Mushuk(Hayvon):
    def __init__(self, nomi):
        super().__init__("Mushuk", "Miyov")
        self.nomi = nomi

    def malumot(self):
        info = (
            "==============================\n"
            f"🐱 Mushuk ma’lumotlari\n"
            "==============================\n"
            f"Nomi : {self.nomi}\n"
            f"Turi : {self.turi}\n"
            f"Ovoz : {self.ovoz}\n"
            "=============================="
        )
        return info

    def ovoz_chiqar(self):
        print(f"{self.nomi} miyovlayapti: {self.ovoz}!")


if __name__ == "__main__":
    hayvon1 = Hayvon("Ot", "Ig‘g‘iyo")
    kuchuk1 = Kuchuk("Rex")
    mushuk1 = Mushuk("Mimi")

    print(hayvon1.malumot())
    print(kuchuk1.malumot())
    print(mushuk1.malumot())

    print("\n=== Ovozlar ===")
    hayvon1.ovoz_chiqar()
    kuchuk1.ovoz_chiqar()
    mushuk1.ovoz_chiqar()

    print("\n=== Qo‘shimcha hayvonlar ===")
    kuchuk2 = Kuchuk("Sharik")
    mushuk2 = Mushuk("Kitti")
    print(kuchuk2.malumot())
    print(mushuk2.malumot())
    kuchuk2.ovoz_chiqar()
    mushuk2.ovoz_chiqar()
