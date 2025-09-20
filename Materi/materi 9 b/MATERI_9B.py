print("==========MATERI 9 - FUNCION STRUCTURE")
print("=======================================")

# fungsi biasa dengan nama

def hello_world(name):
    print('hello mr',name)
    print("how are you doing {name}?")

hello_world("wildan")
hello_world("adull")
hello_world("pawass")
print("---------->lambda<----------")

# FUNGSI ANONIM LAMBDA JIKA SATU BARIZZ
greeting =lambda name: print(f"hello, {name} with lambda")
greeting("hanif")
greeting("landa")
greeting("bilal")


print("=========KONVERSI TIPE DATA!!!==========")
# "" artinya string walupun dia isinya angka
nlai_string ="1000"# tipe datanya string
nilai_integer = int(nlai_string) # int (ubah jadi integer)
kalian_dua_salah = nilai_string * 2
kalian_dua_benar = nilai_integer * 2
print(kalian_dua_salah, kalian_dua_benar)

# MAP () UNTUK MENTRANSFORMASI DATA DARI LIST
# MAP ([FUNGSI _PERUBAHAN_DATA], [SUMBER_DATA])
nilai_mentah = [1.9, 0.2, 4.5, 8.9, 2.1, 0.95, 2.46]
nilai_kali_seratus = map(lambda nilai: nilai * 100, nilai_mentah) 
print(f"nilai_mentah")




daftar_siswa = [
    {"nama": "ali", "angka": 8},
    {"nama": "blanda", "angka": 24},
    {"nama": "bilal", "angka": 26},
]

print("daftar angka siswa", daftar_siswa)
daftar_siswa_terurut = sorted(daftar_siswa, key=lambda siswa:siswa["angka"])

# FOR LOOP -> MENGELUARKAN SELURUH ISI DAFTAR
for siswa in daftar_siswa_terurut:
    print(siswa)

# SORTING LIST
daftar_siswa_kelas_b = ["hanif", "wildan", "joko", "mazza"]
daftar_siswa_terurut = sorted(daftar_siswa_kelas_b)
daftar_siswa_terbalik = sorted(daftar_siswa_kelas_b, reverse=True)
for nama in daftar_siswa_terurut:
    print(nama)


print("----------------#############-------------")
for siswa in daftar_siswa_terbalik:
    print(nama)