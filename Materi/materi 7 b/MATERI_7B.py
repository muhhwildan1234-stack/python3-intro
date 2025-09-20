print("MATERI 7B - PYTHON DATA STRUCTURE")
print("==================================")

# set --> [] -> tidak berurutan, berubah,  tidak duplikat
game_azka = {"valorant", "dark soul"}
game_epan = {"genshin", "mlbb"}
print("azka games: ", game_azka)
print("epan games: ", game_epan)

#. add () --> menambahkan item baru
game_azka.add("elden ring")
game_azka.add("valorant")

#. REMOVE () --> MENAMBAH ITEM
game_epan.remove("genshin")

#. LEN() MENGHITUNG JMLAH ITEM
print("azka ada ", len(game_azka)," games: ", game_azka)
print("epan ada ", len(game_epan)," games: ", game_epan)


#. UNION() --> MENGGABUNG DUA SET YANG BERBEDA
game_berdua = game_azka.union(game_epan)
total_game = len(game_berdua)
print("semua game ada ",total_game," games: ", game_berdua)

#. INTERSECTION() -->MENCARI ITEM YG KEMBAR
#. DIFERENCE() --> MENCARI ITEM YANG BERBEDA

game_kembar = game_azka.intersection(game_epan)
game_beda = game_azka.difference(game_epan)

total_game_kembar = len(game_kembar)
total_game_beda = len(game_beda)
print("game yang kembar ", total_game_kembar," games: ", game_kembar)
print("game yang beda ", total_game_beda," games: ", game_beda)

# DICT (DICTIONARY) --> {KEY:VALUE} /{KUNCI:ISINYA}
# BERURUTAN BERDASARKAN KEY, BERUBAH,
# KEY TIDAK BOLEH DUPLIKAT

koleksi_anime = {
    "re_zero":"subaru",
    "one_piece":"usop",
    "waifu": {
        "re_zero": "rem_chan", # tidak masalah key sama klo struktur beda
        "demon_slayer": "nezuko"
    }
} 
print("koleksi_anime: ", koleksi_anime)
print("mc one_piece: ", koleksi_anime["one_piece"])


# OPERATOR DICTIONARY

data_dict = {
    "cup":"ucup surucup",
    "tong":"otong sorotong",
    "dung":"dudung surudung"
}

# PANJANG DICTIONARY
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# MENGECEK KEY EXIST ATAU TIDAK
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data dict: {CHECKKEY}")

# MENGAKSES VALUE (READ) DENGAN GET
print(data_dict.get("cup"))
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan"))

# MENGUPDATE DATA
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
