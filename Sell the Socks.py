def kk_tidak_ada_pasangan_test():
    expected = "H : "
    result = kk()

def to_warna_dan_jumlah(kaus_kaki):
    kaus_kaki.sort()
    jumlah_warna = [kaus_kaki.count(a) for a in kaus_kaki]
    warna_dan_jumlah = zip(kaus_kaki, jumlah_warna)
    list_warna_dan_jumlah = list(set(warna_dan_jumlah))
    return list_warna_dan_jumlah

def to_dict_warna_jumlah(warna_jumlah):
    dict_warna_dan_jumlah = {}
    for a in warna_jumlah:
        string = ""
        dict_warna_dan_jumlah[a[0]] = a[1] // 2
        for b in range(0, dict_warna_dan_jumlah[a[0]]):
            string = string + "#"
        dict_warna_dan_jumlah[a[0]] = string
    return  dict_warna_dan_jumlah

def kk(pasang_kaus_kaki):
    list_warna_dan_jumlah = to_warna_dan_jumlah(pasang_kaus_kaki)

    dict_warna_dan_jumlah = to_dict_warna_jumlah( list_warna_dan_jumlah)

    temp = ""
    for x in dict_warna_dan_jumlah.keys():
        temp = str(temp + x + " : " + dict_warna_dan_jumlah[x]) + "\n"
    return temp

def main():
    jenis_warna_kaus_kaki = input("masukkan warna : ")
    jenis_warna_kaus_kaki = jenis_warna_kaus_kaki.upper()
    jenis_warna_kaus_kaki = jenis_warna_kaus_kaki.split(",")
    a = kk(jenis_warna_kaus_kaki)
    print(a)

main()