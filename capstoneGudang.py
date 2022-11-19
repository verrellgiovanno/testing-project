# CAPSTONE PROJECT GUDANG - DATA STOK

listBarang = [
    {
        'kode': 'BH-APEL',
        'nama': 'Apel',
        'kategori': 'Buah',
        'stok': 20,
        'status': 'In stock'
    }, 
    {
        'kode': 'BH-JMBU',
        'nama': 'Jambu', 
        'kategori': 'Buah',
        'stok': 0,
        'status': 'Out stock'
    },
    {
        'kode': 'SY-SAWI',
        'nama': 'Sawi', 
        'kategori': 'Sayur',
        'stok': 15,
        'status': 'In stock'
    }
]

def notifPilihanSalah() :
    print('Pilihan yang Anda masukkan salah')

def notifNoData():
    print('Tidak ada data')

def notifAdaData():
    print('Data sudah ada')

def notifSimpanData():
    print('Data tersimpan')

def notifUpdateData():
    print('Data terupdate')

def notifDeleteData():
    print('Data deleted')

def tampilListBarang() :
    print('\nDaftar Barang\nKode\t| Nama   \t| Kategori\t| Stok\t| Status')
    for i in range(len(listBarang)) :
        print(f"{listBarang[i]['kode']}\t| {listBarang[i]['nama']}   \t| {listBarang[i]['kategori']}   \t| {listBarang[i]['stok']}\t| {listBarang[i]['status']}")

def tampilIndexBarang(index) :
    print('\nDaftar Barang\nKode\t| Nama   \t| Kategori\t| Stok\t| Status')
    print(f"{listBarang[index]['kode']}\t| {listBarang[index]['nama']}   \t| {listBarang[index]['kategori']}   \t| {listBarang[index]['stok']}\t| {listBarang[index]['status']}")

def menampilkanData() :
    while True :
        menuBaca = input('''
List Menu Menampilkan Data Barang :
1. Menampilkan Semua Data Barang
2. Menampilkan Data Barang Berdasarkan Kode yang Dicari
3. Kembali ke Menu Utama
Masukkan angka Menu yang ingin dijalankan : ''')
        if menuBaca == '1' :
            if len(listBarang) == 0 :
                notifNoData()
            else :
                tampilListBarang()
        elif menuBaca == '2' :
            cariKode = input('Kode barang yang dicari: ').upper()
            for i in range(len(listBarang)) :
                if listBarang[i]['kode'] == cariKode :
                    tampilIndexBarang(i)
                    break
            else :
                notifNoData()
        elif menuBaca == '3' :
            break
        else :
            notifPilihanSalah()

def menambahData() :
    while True :
        menuTambah = input('''
List Menu Menambahkan Data Barang :
1. Menambahkan Data Barang
2. Kembali ke Menu Utama
Masukkan angka Menu yang ingin dijalankan : ''')
        if menuTambah == '1' :
            cariKode = input('Kode barang yang ingin ditambah: ').upper()
            for i in range(len(listBarang)) :
                if listBarang[i]['kode'] == cariKode :
                    notifAdaData()
                    break
            else :
                tambahKode = cariKode
                tambahNama = input('Nama barang yang ingin ditambah: ').lower().capitalize()
                tambahKategori = input('Kategori barang yang ingin ditambah: ').lower().capitalize()
                while True :
                    tambahStok = int(input('Stok barang yang ingin ditambah: '))
                    if tambahStok < 0 :
                        print('Stok barang tidak boleh kurang dari 0')
                    elif tambahStok == 0 :
                        tambahStatus = 'Out stock'
                        break
                    else :
                        tambahStatus = 'In stock'
                        break
                print(f' Kode   \t: {tambahKode}\n Nama   \t: {tambahNama}\n Kategori\t: {tambahKategori}\n Stok   \t: {tambahStok}')
                while True :
                    opsiSimpan = input('''Apakah Anda yakin ingin menyimpan data berikut?
1. Ya
2. Tidak
Masukkan angka opsi yang ingin dijalankan : ''')
                    if opsiSimpan == '1' :
                        dict = {}
                        dict['kode'] = tambahKode
                        dict['nama'] = tambahNama
                        dict['kategori'] = tambahKategori
                        dict['stok'] = tambahStok
                        dict['status'] = tambahStatus
                        listBarang.append(dict)
                        notifSimpanData()
                        break
                    elif opsiSimpan == '2' :
                        break
                    else :
                        notifPilihanSalah()
        elif menuTambah == '2' :
            break
        else:
            notifPilihanSalah()

def memperbaruiData() :
    while True :
        menuUpdate = input('''
List Menu Memperbarui Data Barang :
1. Memperbarui Data Barang
2. Kembali ke Menu Utama
Masukkan angka Menu yang ingin dijalankan : ''')              
        if menuUpdate == '1' :
            cariKode = input('Kode barang yang ingin diperbarui: ').upper()
            for i in range(len(listBarang)) :
                if listBarang[i]['kode'] == cariKode :
                    tampilIndexBarang(i)
                    while True :
                        opsiUpdate = input('''Apakah Anda ingin memperbarui data berikut?
1. Ya
2. Tidak
Masukkan angka opsi yang ingin dijalankan : ''')
                        if opsiUpdate == '1' :
                            while True :
                                kolomUpdate = input('''List kolom yang ingin diperbarui :
1. Kode
2. Nama
3. Kategori
4. Stok
Masukkan angka kolom yang ingin diubah : ''')
                                if kolomUpdate == '1' or kolomUpdate == '2' or kolomUpdate == '3' or kolomUpdate == '4' :
                                    if kolomUpdate == '1' :
                                        kolomUpdate = 'kode'
                                        valueUpdate = input(f'Masukkan value {kolomUpdate} yang baru : ').upper()
                                    elif kolomUpdate == '2' :
                                        kolomUpdate = 'nama'
                                        valueUpdate = input(f'Masukkan value {kolomUpdate} yang baru : ').lower().capitalize()
                                    elif kolomUpdate == '3' :
                                        kolomUpdate = 'kategori'
                                        valueUpdate = input(f'Masukkan value {kolomUpdate} yang baru : ').loswer().capitalize()
                                    else :
                                        kolomUpdate = 'stok'
                                        while True :
                                            valueUpdate = int(input(f'Masukkan value {kolomUpdate} yang baru : '))
                                            if valueUpdate < 0 :
                                                print('Stok barang tidak boleh kurang dari 0')
                                            elif valueUpdate == 0 :
                                                statusUpdate = 'Out stock'
                                                break
                                            else :
                                                statusUpdate = 'In stock'
                                                break
                                    while True :
                                        opsiSimpan = input(f'''Anda yakin ingin memperbarui {kolomUpdate} barang menjadi {valueUpdate}?
1. Ya
2. Tidak
Masukkan angka opsi yang ingin dijalankan : ''')
                                        if opsiSimpan == '1' :
                                            if kolomUpdate == 'stok' :
                                                listBarang[i][kolomUpdate] = valueUpdate
                                                listBarang[i]['status'] = statusUpdate
                                                notifUpdateData()
                                                break
                                            else :
                                                listBarang[i][kolomUpdate] = valueUpdate
                                                notifUpdateData()
                                                break
                                        elif opsiSimpan == '2' :
                                            break
                                        else :
                                            notifPilihanSalah()
                                    break
                                else :
                                    notifPilihanSalah()
                            break
                        elif opsiUpdate == '2' :
                            break
                        else :
                            notifPilihanSalah()
                    break
            else :
                notifNoData()
        elif menuUpdate == '2' :
            break
        else :
            notifPilihanSalah()

def menghapusData() :
    while True :
        menuHapus = input('''
List Menu Menghapus Data Barang :
1. Menghapus Data Barang
2. Kembali ke Menu Utama
Masukkan angka Menu yang ingin dijalankan : ''')
        if menuHapus == '1' :
            cariKode = input('Kode barang yang ingin dihapus: ').upper()
            for i in range(len(listBarang)) :
                if listBarang[i]['kode'] == cariKode :
                    tampilIndexBarang(i)
                    while True :
                        opsiHapus = input('''Apakah Anda ingin menghapus data berikut?
1. Ya
2. Tidak
Masukkan angka opsi yang ingin dijalankan : ''')
                        if opsiHapus == '1' :
                            del listBarang[i]
                            notifDeleteData()
                            break
                        elif opsiHapus == '2' :
                            break
                        else :
                            notifPilihanSalah()
                    break
            else :
                notifNoData()
        elif menuHapus == '2' :
            break
        else :
            notifPilihanSalah()

while True :
    menuUtama = input('''
Selamat Datang di Gudang
List Menu Utama :
1. Menampilkan Data Barang
2. Menambahkan Data Barang
3. Memperbarui Data Barang
4. Menghapus Data Barang
5. Exit Program
Masukkan angka Menu yang ingin dijalankan : ''')
    if menuUtama == '1' :
        menampilkanData()
    elif menuUtama == '2' :
        menambahData()
    elif menuUtama == '3' :
        memperbaruiData()
    elif menuUtama == '4' :
        menghapusData()
    elif menuUtama == '5' :
        break
    else :
        notifPilihanSalah()