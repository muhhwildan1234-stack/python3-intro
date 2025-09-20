import csv

print("============MATERI 10B============")
print("-----------------------------------")

# CARI POSISI FILE NOTE.TXT DENGAN RAW STRING (R)

file_path = r"\Users\LENOVO\Desktop\python\MINIPROJECT\materi_10_file\note.txt"

# OPEN()-> BUKA FILE TARGET
# MODE R -> READ ONLY (HANYA BACA)

file_catatan = open(file_path, "r")
# READ() -> BACA ISI FILE NOTE. TXT

catatan = file_catatan.read()
print(f"isi catatan: {catatan}")

# TUTUP FILE NOTE.TXT

print("=============OPEN CSV==========")
print("=================================")
anime_file_path = r"/Users\LENOVO\Desktop\python\MINIPROJECT\materi_10_file\anime.csv"
# with ... as -> agar file otomatis ter close
with open(anime_file_path, "r") as file_anime:

    # gunakan fungsi reader() dari module csv
    baca_file_anime = csv.reader(file_anime)

    # ubah object csv ke list agar bisa diolah
    list_anime = list(baca_file_anime)
    
    print(f"daftar anime: {list_anime}")
    print('>> proses baca file anime.csv selesai')
    print(f"anime baru: {anime_baru}")

    # keluarkan seluruh data dengan foor loop
    for anime in list_anime:
        print(anime)


        print("PROSES BACA FILE ANIME.CSV SUDAH SELESAI")
        print("============add csv====================")

        anime_baru = [6, "evan, "kaijuu no-8", 10.0]

        # mode 'a' (append) ->tambah data terakhir





























print