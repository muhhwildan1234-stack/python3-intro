print("==========FUNCTION DASAR=========")
print("==================================")

# struktur fungsi dasar tanpa parameter
def halo_lc() :
    print("hello ganteng")
    print("halo ganteng")
# cara akses function, sertakam namanya dan() -nya
halo_lc()

# fungsi dengan parameter (variabel d fungsi)
def sapa_sapa_gan(nama):
    print("hallo",nama, "selamat makan di hsi projo")

sapa_sapa_gan("mas boy")
sapa_sapa_gan("king ruckie")

def rumus_luas_segi_tiga(alas, tinggi):
    print("Alas", alas)
    print("tinggi:", tinggi)
    rumusan = 1/2 *(alas*tinggi)
    print("hasil:", rumusan)

rumus_luas_segi_tiga(10, 30)
rumus_luas_segi_tiga(50, 100)
