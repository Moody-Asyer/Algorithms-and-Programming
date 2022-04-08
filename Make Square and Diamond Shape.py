# P1 (20%) :
# Panjang = 6
# Lebar = 3
#
# * * * * * *
# * * * * * *
# * * * * * *

# p2 (80%)
# # diagonal = 1    diagonal = 2      diagonal = 3
#                                         *
#  *                    *                * *
#                      * *              * * *
#                       *                * *
#                                         *


def persegi_panjang():
    panjang = int(input("Masukkan Panjang : "))
    lebar = int(input("Masukkan Lebar : "))
    count = 1
    while count <= lebar:
        for x in range(panjang):
            print("*",end="   ")
        count += 1
        print(" ")

def belah_ketupat():
    diagonal = int(input("Masukkan Diagonal: "))
    D = diagonal
    count = 2
    while D >= count:
        for x in range (D):
            print("", end=" ")
        print(" *","* "*abs(diagonal-D))
        D -=1
    while D <= diagonal:
        for x in range (D):
            print("", end=" ")
        print(" *","* "*abs(D-diagonal))
        D +=1
if __name__ == "__main__":

    # metode (en: method) dibawah ini bisa kalian uncomment untuk menjalankannya.
    persegi_panjang()
    belah_ketupat()

    # belahketupat()
