# -*- coding: utf-8 -*-
"""Dynamic_Programming_10101190154

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RLReOZJ_2tgcb5gPuypoXx7fjw3WIVjq
"""

# !!!code masih error!!! output yang keluar tidak sesuai yang diharapkan

# import numpy as np
# import time

# start = time.time() # penanda watu operasi dimulai

# building_file = open("Bangunan1.txt", "r").read() #membuka file bangunan, lalu membaca isinya
# rows = building_file.split("\n") #membagi isi file ke dalam list tiap barisnya

# #mengambil isi file pada baris pertama yang merupakan input ukuran dari baris, kolom, dan tinggi lantai bangunan
# input_size = tuple(map(int, rows[0].split(" "))) 

# rmax = input_size[0]-1 #mengambil nilai baris maksimal, ada -1 karena index mulai dari 0
# cmax = input_size[1]-1 #mengambil nilai kolom maksimal, ada -1 karena index mulai dari 0
# hmax = input_size[2]-1 #mengambil nilai tinggi lantai maksimal, ada -1 karena index mulai dari 0

# building_matrix = [] # bangunan awal berbentuk list kosong yang nantinya akan kita buat menjadi matrix

# def matrix(building_matrix, building_file_rows):
#     # Fungsi matrix untuk membentuk matrix bangunan yang berisi tiap nilai data pada baris, kolom, dan lantai masing-masing...
#     # dan di tiap baris dan kolom tiap lantainya ada data dari nilai harta karun yang dapat dikumpulkan

#     x = 1 #index nilai harta karun dimulai dari index 1 pada file (index 0 adalah input)
#     while x < len(building_file_rows) - 1:
#         lantai = [] # list yang berisi baris dan kolom dari suatu lantai
#         y = x + rmax + 1 
#         while x < y:
#             lantai.append(list(map(int, building_file_rows[x].split(" ")))) # menambah list berisi setiap nilai pada baris dan kolom suatu lantai
#             x += 1 
#         building_matrix.append(lantai) # menambah list yang berisi nilai dari baris dan kolom suatu lantai ke dalam list bangunan

# def dynamic(h, r, c, path):
#     # l merupakan nomor tingkatan dari lokasi cell yang sedang ditinjau.
#     # r merupakan nomor baris dari lokasi cell yang sedang ditinjau.
#     # c merupakan nomor kolom dari lokasi cell yang sedang ditinjau.
#     # direction merupakan arah gerak dari cell sebelumnya ke cell saat ini.
#     if memo[h][r][c] != None:
#         path += memo[h][r][c][1]
#         return memo[h][r][c][0], path
#     if (h == hmax - 1 and r == rmax - 1 and c == cmax - 1 ):
#         data = [building_matrix[h][r][c], ""]
#         memo[h][r][c] = data
#         return memo[h][r][c][0], path + memo[h][r][c][1]
#     elif (h < hmax - 1 and r < rmax - 1 and c < cmax - 1):
#             next_step = max(dynamic(h, r + 1, c, "S"), dynamic(h, r, c + 1, "T"), dynamic(h + 1, r, c, "A"))
#     elif (h == hmax - 1 and c < cmax - 1 and r < rmax - 1 ):
#             next_step = max(dynamic(h, r + 1, c, "S"), dynamic(h, r, c + 1, "T"))
#     elif (h < hmax - 1  and c < cmax - 1 and r == rmax - 1):
#             next_step = max(dynamic(h, r, c + 1, "T"), dynamic(h + 1, r, c, "A"))
#     elif (h < hmax - 1 and r < rmax - 1 and c == cmax - 1):
#             next_step = max(dynamic(h, r + 1, c, "S"), dynamic(h + 1, r, c, "A"))
#     elif (h == hmax - 1 and r == rmax - 1 and c < cmax - 1):
#             next_step = dynamic(h, r, c + 1, "T")
#     elif (h == hmax - 1 and c == cmax - 1 and r < rmax - 1 ):
#             next_step = dynamic(h, r + 1, c, "S")
#     elif (h < hmax - 1  - 1 and c == cmax - 1 and r == rmax):
#             next_step = dynamic(h + 1, r, c, "A")

#     data = [next_step[0] + building_matrix[h][r][c], next_step[1]]
#     memo[h][r][c] = data
#     return memo[h][r][c][0], path + memo[h][r][c][1]
    
# matrix(building_matrix, rows)    
# memo = np.full((hmax, rmax, cmax),None)
# result = dynamic(0, 0, 0, "")
# print(result[1])
# print(result[0])
# operation_time = (time.time()-start) #jumlah waktu operasi keseluruhan
# print(operation_time)