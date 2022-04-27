#todo: açıklamalar eklenecek
from decimal import Decimal, getcontext
from math import ceil, factorial

def pi(hassasiyet: int) -> str:
    if not isinstance(hassasiyet, int):
        raise TypeError("Tamsayı olmayanları için tanımsız / Undefined for non-integers")
    elif hassasiyet < 1:
        raise ValueError("Doğal olmayan sayılar için tanımsız / Undefined for non-natural numbers")

    getcontext().prec = hassasiyet
    interasyon_say = ceil(hassasiyet/14)
    kalan = 426880 * Decimal(10005).sqrt()
    ustel_terim = 1
    lineer_terim = 13591409
    parcali_toplam = Decimal(lineer_terim)
    for k in range(1, interasyon_say):
        multinominal_terim = factorial(6 * k) // (factorial(3 * k) * factorial(k) **3)
        lineer_terim += 545140134
        ustel_terim *= -262537412640768000
        parcali_toplam += Decimal(multinominal_terim * lineer_terim) / ustel_terim
    return str(kalan / parcali_toplam)[:-1]

if __name__ == "__main__":
    n=50
    print(f"Pi sayısının ilk {n} basamağı: {pi(n)}")
