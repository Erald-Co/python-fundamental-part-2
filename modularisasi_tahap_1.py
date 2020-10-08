"""
Program menghitung luas segitiga
luas segitiga = alis * tinggi / 2
"""

# menghitung luas segitiga tanpa fungsi
alas = 10
tinggi = 6

luas_segitiga = alas * tinggi / 2

print("Segitiga dengan alas {} dan tinggi {} memiliki luas {}".format(alas, tinggi, str(int(luas_segitiga))))

# menghitung luas segitiga dengan fungsi

def luas_segitiga(alas, tinggi):
    return alas * tinggi / 2

print(luas_segitiga(2, 3))