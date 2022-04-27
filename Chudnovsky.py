from decimal import Decimal, getcontext
from math import ceil, factorial

def pi(hassasiyet: int) -> str:
    if not isinstance(hassasiyet, int): #precision 
        raise TypeError("Tamsayı olmayanları için tanımsız / Undefined for non-integers")
    elif hassasiyet < 1:
        raise ValueError("Doğal olmayan sayılar için tanımsız / Undefined for non-natural numbers")

    getcontext().prec = hassasiyet 
    interasyon_say = ceil(hassasiyet/14) #number of iteration
    kalan = 426880 * Decimal(10005).sqrt() #constant term
    ustel_terim = 1 #exponential term
    lineer_terim = 13591409 #linear term
    parcali_toplam = Decimal(lineer_terim) #partial sum
    for k in range(1, interasyon_say):
        multinominal_terim = factorial(6 * k) // (factorial(3 * k) * factorial(k) **3)
        lineer_terim += 545140134
        ustel_terim *= -262537412640768000
        formul(ustel_terim, lineer_terim, parcali_toplam, multinominal_terim)
    return str(kalan / parcali_toplam)[:-1]

def formul(ustel_terim, lineer_terim, parcali_toplam, multinominal_terim):
    parcali_toplam += Decimal(multinominal_terim * lineer_terim) / ustel_terim

if __name__ == "__main__":
    n=50 ## Kaç basamak hesaplamak istediğinizi yazın - Write here how many digit you want to calculate.
    print(f"Pi sayısının ilk {n} basamağı: {pi(n)}") 
