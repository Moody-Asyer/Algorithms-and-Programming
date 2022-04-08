nomor = open("angkas.txt", "r")
angka = nomor.readline()
x = angka.split (",")
list = []
for i in x:
   list.append(int(i))

dicari = int(input("angka yang dicari =  "))
def binary_search(list, dicari):
    kiri = 0
    kanan = len(list) - 1
    found = False
    while kiri <= kanan and not found:
        mid = (kiri + kanan) // 2
        if dicari > list[kanan] or dicari < list[kiri]:
            return "tidak ada"
        if list[mid] == dicari:
            found = True
        else:
            if dicari < list[mid]:
                kanan = mid
            elif dicari > list[mid]:
                kiri = mid
    if found == True:
        return "angka yang dicari ada di index ke-%d" % mid
    else:
        return "tidak ada"

print(binary_search(list, dicari))
nomor.close()

#Menggunakan 3 test yaitu test untuk mencari angka dalam angkas.txt,membuktikan suatu angka diluar angkas.txt,dan test semua test apakah berjalan lancar atau ada kesalahan.

#Test untuk membuktikan suatu angka diluar angkas.txt
#misal dicari = 0
def test_0():
    result = binary_search(list, 0)
    expected = "tidak ada"
    assert result == expected,"gagal"
    if result == expected:
        print("test Berhasil")

#Test untuk membuktikan suatu angka didalam angkas.txt
#misal dicari = 20
def test_20():
    result = binary_search(list, 20)
    expected = "angka yang dicari ada di index ke-19"
    assert result == expected,"gagal"
    if result == expected:
        print("test Berhasil")

##Test untuk mengetest semua fungsi test sebelum program dimulai
def test_all():
    test_0()
    test_20()

test_all()

