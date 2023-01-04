x = open("input.txt", "r") #pembacaan dari file text
file = x.readlines() #pembacaan semua baris
x.close() # setelah file text nya diakses maka harus ditutup
pemain_golf = []
datas = []
perhitungan=[]
for i in file: 
    datas.append(i.split()) 


for i in range(len(datas)):
    pemain_golf.append(dict())
    for j in range(1,len(datas[i])+1): #perulangan untuk semua elemen di datas
        pemain_golf[i]["Nama"] = datas[i][0]  #hanya mengambil nama pemain dan dimasukkan kedalam list dg tipe data dictionary
        a = datas[i][j-1] #mengambil semua elemen di datas termasuk nama pemain dan simbol skornya
        PAR=5
        qd=4
        tp=3
        db=2
        bg=1
        par=0
        br=-1
        eg=-2
        al=-3
        cn=-4
        ace=1
        if a == datas[i][0]: #dilakukan pengecekan jika a adalah nama pemain maka tidak akan di proses
            continue
        elif a == "PAR":
            datas[i][j-1] = (PAR+par)
        elif a == "BR":
            datas[i][j-1] = (PAR+br)
        elif a == "EG":
            datas[i][j-1] = (PAR+eg)
        elif a == "AL":
            datas[i][j-1] = (PAR+al)
        elif a == "CN":
            datas[i][j-1] = (PAR+cn)
        elif a == "BG":
            datas[i][j-1] = (PAR+bg)
        elif a == "DB":
            datas[i][j-1] = (PAR+db)
        elif a == "TP":
            datas[i][j-1] = (PAR+tp)
        elif a == "QD":
            datas[i][j-1] = (PAR+qd)
        elif a == "ACE":
            datas[i][j-1] = ace
        pemain_golf[i]["hole"+str(j-1)] = datas[i][j-1] #menambahkan setiap hole dan skornya ke dalam dictionary

#perulangan ini untuk menjumlahkan skor dari 18 hole tersebut
for i in range(len(pemain_golf)):
    total = 0
    nama = datas[i][0] 
    for j in pemain_golf[i]:
        a = pemain_golf[i][j] #akan mengambil value-value dari dictionary
        if type(a) == int: #mengecek jika a adalah int maka akan dijumlahkan
            total += a
        else:
            continue
    perhitungan.append({nama:total}) #menambahkan dict kedalam list dg key nama pemain & value total skor

#fungsi ini untuk mengecek pemenangnya dimana pemenang memiliki skor terkecil
def pemenang(perhitungan):
    tinggi=perhitungan[0]["PRAS"] #penginisialisasian skor pras terbesar
    nama="PRAS" #penginisialisasian dg nama pras
    for i in perhitungan:
        for j in i:
            if i[j]<tinggi:
                tinggi=i[j] #tinggi nya di update jika i[j] lebih kecil dari tinggi
                nama=j
    return nama #mereturn nama pemain dengan skor terkecil

#fungsi ini digunakan untuk menghitung rata-rata dari skor semua pemain
def rerata(perhitungan):
    jumlah=0
    for i in perhitungan:
        for j in i:
            jumlah+=i[j]
    return jumlah/len(perhitungan) #mereturn rata-rata



#main program
for i in pemain_golf:
    print(i)
for i in perhitungan:
    print(i)
print("pemenangnya adalah",pemenang(perhitungan))
print("rata-rata keseluruhan adalah","{:.3f}".format(rerata(perhitungan)))