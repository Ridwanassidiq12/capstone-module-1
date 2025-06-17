from tabulate import tabulate
from datetime import datetime
import re
import pandas as pd

data_karyawan = [
        {
        "nama": "ANDI SANTOSO",
        "nik": "1234567890123456",
        "tempat lahir": "JAKARTA",
        "tanggal lahir": "10-05-1985",
        "jenis kelamin": "LAKI-LAKI",
        "alamat": "JAKARTA SELATAN MANGGAERAI DIEPONOGORO RT.01/RW.01",
        "no telp": "081234567890",
        "email": "ANDI.SANTOSO@EMAIL.COM",
        "status pernikahan": "MENIKAH",
        "pendidikan terakhir": "S1",
        "jabatan": "MANAGER",
        "manajemen": "PRODUKSI",
        "tanggal masuk": "01-03-2010",
        "status karyawan": "TETAP",
        "gaji pokok": 7000000,
        "tunjangan": 2000000,
        "total gaji": 9000000
    },
    {
        "nama": "SITI AMINAH",
        "nik": "2345678901234567",
        "tempat lahir": "BANDUNG",
        "tanggal lahir": "15-07-1990",
        "jenis kelamin": "PEREMPUAN",
        "alamat": "BANDUNG TENGAH MANGGAERAI DIEPONOGORO RT.02/RW.03",
        "no telp": "082345678901",
        "email": "SITI.AMINAH@EMAIL.COM",
        "status pernikahan": "LAJANG",
        "pendidikan terakhir": "S2",
        "jabatan": "KARYAWAN",
        "manajemen": "KEUANGAN",
        "tanggal masuk": "20-06-2015",
        "status karyawan": "TETAP",
        "gaji pokok": 5500000,
        "tunjangan": 1500000,
        "total gaji": 7000000
    },
    {
        "nama": "BUDI WIJAYA",
        "nik": "3456789012345678",
        "tempat lahir": "SURABAYA",
        "tanggal lahir": "05-12-1988",
        "jenis kelamin": "LAKI-LAKI",
        "alamat": "SURABAYA BARAT MANGGAERAI DIEPONOGORO RT.03/RW.02",
        "no telp": "083456789012",
        "email": "BUDI.WIJAYA@EMAIL.COM",
        "status pernikahan": "MENIKAH",
        "pendidikan terakhir": "S1",
        "jabatan": "KARYAWAN",
        "manajemen": "MARKETING",
        "tanggal masuk": "10-11-2012",
        "status karyawan": "TETAP",
        "gaji pokok": 6000000,
        "tunjangan": 1200000,
        "total gaji": 7200000
    },
    {
        "nama": "DEWI LESTARI",
        "nik": "4567890123456789",
        "tempat lahir": "YOGYAKARTA",
        "tanggal lahir": "25-08-1992",
        "jenis kelamin": "PEREMPUAN",
        "alamat": "YOGYAKARTA SELATAN MANGGAERAI DIEPONOGORO RT.04/RW.05",
        "no telp": "084567890123",
        "email": "DEWI.LESTARI@EMAIL.COM",
        "status pernikahan": "LAJANG",
        "pendidikan terakhir": "S1",
        "jabatan": "KARYAWAN",
        "manajemen": "IT",
        "tanggal masuk": "15-02-2018",
        "status karyawan": "KONTRAK",
        "gaji pokok": 5000000,
        "tunjangan": 1000000,
        "total gaji": 6000000
    },
    {
        "nama": "EKO PRASETYO",
        "nik": "5678901234567890",
        "tempat lahir": "SEMARANG",
        "tanggal lahir": "30-04-1987",
        "jenis kelamin": "LAKI-LAKI",
        "alamat": "SEMARANG TENGAH MANGGAERAI DIEPONOGORO RT.05/RW.01",
        "no telp": "085678901234",
        "email": "EKO.PRASETYO@EMAIL.COM",
        "status pernikahan": "MENIKAH",
        "pendidikan terakhir": "S2",
        "jabatan": "MANAGER",
        "manajemen": "KEUANGAN",
        "tanggal masuk": "05-07-2011",
        "status karyawan": "TETAP",
        "gaji pokok": 7500000,
        "tunjangan": 2500000,
        "total gaji": 10000000
    },
    {
        "nama": "FIONA AMELIA",
        "nik": "6789012345678901",
        "tempat lahir": "MEDAN",
        "tanggal lahir": "12-09-1991",
        "jenis kelamin": "PEREMPUAN",
        "alamat": "MEDAN UTARA MANGGAERAI DIEPONOGORO RT.06/RW.02",
        "no telp": "086789012345",
        "email": "FIONA.AMELIA@EMAIL.COM",
        "status pernikahan": "LAJANG",
        "pendidikan terakhir": "S1",
        "jabatan": "MANAGER",
        "manajemen": "MARKETING",
        "tanggal masuk": "22-08-2017",
        "status karyawan": "MAGANG",
        "gaji pokok": 4000000,
        "tunjangan": 800000,
        "total gaji": 4800000
    },
    {
        "nama": "GUNTUR SANTOSO",
        "nik": "7890123456789012",
        "tempat lahir": "MAKASSAR",
        "tanggal lahir": "18-01-1984",
        "jenis kelamin": "LAKI-LAKI",
        "alamat": "MAKASSAR BARAT MANGGAERAI DIEPONOGORO RT.07/RW.04",
        "no telp": "087890123456",
        "email": "GUNTUR.SANTOSO@EMAIL.COM",
        "status pernikahan": "MENIKAH",
        "pendidikan terakhir": "S3",
        "jabatan": "DIREKTUR",
        "manajemen": "PRODUKSI",
        "tanggal masuk": "01-01-2009",
        "status karyawan": "TETAP",
        "gaji pokok": 12000000,
        "tunjangan": 4000000,
        "total gaji": 16000000
    },
    {
        "nama": "HANNA NURAINI",
        "nik": "8901234567890123",
        "tempat lahir": "BALIKPAPAN",
        "tanggal lahir": "03-03-1993",
        "jenis kelamin": "PEREMPUAN",
        "alamat": "BALIKPAPAN TIMUR MANGGAERAI DIEPONOGORO RT.08/RW.05",
        "no telp": "088901234567",
        "email": "HANNA.NURAINI@EMAIL.COM",
        "status pernikahan": "LAJANG",
        "pendidikan terakhir": "S1",
        "jabatan": "MANAGER",
        "manajemen": "IT",
        "tanggal masuk": "10-10-2019",
        "status karyawan": "KONTRAK",
        "gaji pokok": 5200000,
        "tunjangan": 1000000,
        "total gaji": 6200000
    },
    {
        "nama": "IWAN SETIAWAN",
        "nik": "9012345678901234",
        "tempat lahir": "MALANG",
        "tanggal lahir": "28-11-1986",
        "jenis kelamin": "LAKI-LAKI",
        "alamat": "MALANG SELATAN MANGGAERAI DIEPONOGORO RT.09/RW.02",
        "no telp": "089012345678",
        "email": "IWAN.SETIAWAN@EMAIL.COM",
        "status pernikahan": "MENIKAH",
        "pendidikan terakhir": "S2",
        "jabatan": "KARYAWAN",
        "manajemen": "MARKETING",
        "tanggal masuk": "05-05-2013",
        "status karyawan": "TETAP",
        "gaji pokok": 6500000,
        "tunjangan": 1500000,
        "total gaji": 8000000
    },
    {
        "nama": "JOKO WIDODO",
        "nik": "0123456789012345",
        "tempat lahir": "SOLO",
        "tanggal lahir": "21-06-1982",
        "jenis kelamin": "LAKI-LAKI",
        "alamat": "SOLO TENGAH MANGGAERAI DIEPONOGORO RT.10/RW.01",
        "no telp": "081234567899",
        "email": "JOKO.WIDODO@EMAIL.COM",
        "status pernikahan": "MENIKAH",
        "pendidikan terakhir": "S1",
        "jabatan": "CEO",
        "manajemen": "EKSEKUTIF",
        "tanggal masuk": "15-01-2007",
        "status karyawan": "TETAP",
        "gaji pokok": 15000000,
        "tunjangan": 5000000,
        "total gaji": 20000000
    }
    
    ]

# function replace dan isalpha
def func_re_pha(value_re_pha):
    while True:
        func_re_pha_in = input(value_re_pha)
        if func_re_pha_in.replace(" ", "").isalpha():
            return func_re_pha_in
        else :
            print("hanya boleh memasukan huruf!")

# function isnumeric
def func_num(value_num):
    while True:
        func_num_in = input(value_num)
        if func_num_in.isnumeric():          
            return func_num_in
        
        if func_num_in == "x":
            return None

        else :
            print("hanya boleh memasukan angka!")

# function nik
def func_nik(value_nik):
    while True:
        func_nik_in = input(value_nik)
        if any(str(data_nik["nik"]) == func_nik_in for data_nik in data_karyawan):
            print(f"Data dengan NIK {func_nik_in} sudah ada!")
            continue
        if re.match(r"\b[\d]{10,20}\b", func_nik_in): 
            return func_nik_in
        else :
            print("masukan NIK dengan benar! 'minimal 10 angka' ")

# function alamat
def func_alamat(value_alamat):
    while True:
        func_alamat_in = input(value_alamat)
        if re.match(r"^(?:[a-z]{4,20}|[a-z]{2,5}\s[a-z]{4,30})\s[a-z]{4,30}\s[a-z]{4,30}\s[a-z]{4,30}\srt\.\d{1,3}/rw\.\d{1,3}$", func_alamat_in):
            return func_alamat_in
        else:
            print("masukan alamat yg sesuai ( cth : provinsi kota/kabupaten kecamatan desa rt.01/rw.01 )")

# function tanggal dd-mm-yyyy
def func_date(value_date):
    while True:
        func_date_in = input(value_date)
        if re.match(r"^(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-(19\d{2}|20\d{2})$", func_date_in):
            return func_date_in
        else:
            print("masukan tanggal yg sesuai (cth : 01-01-2000)")

# function no tlpn
def func_no_tlpn(value_no_tlpn):
    while True:
        func_no_tlpn_in = input(value_no_tlpn)
        if re.match(r"^(?:\+62|0)8[1-9]\d{6,10}$", func_no_tlpn_in): # tanda ?: itu berfungsi agar grouping() tidak di baca ## tanda grouping () dan ?: untuk mengeluarkan grouping
            return func_no_tlpn_in
        else:
            print("masukan no tlpn yang sesuai (cth : 08xxxxxxxx / +628xxxxxxxxx)")

# function email
def func_email(value_email):
    while True:
        func_email_in = input(value_email)
        if re.match(r"^[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}$", func_email_in):
            return func_email_in
        else:
            print("masukan email yang sesuai (cth : xxxxx@gmail.com)")

# function gender
def func_gender(value_gender):
    while True:
        list_gender = ["laki-laki", "perempuan"]
        func_gender_in = input(value_gender)
        if func_gender_in in list_gender:
            return func_gender_in
        else :
            print("pilih isi yang sesuai (laki-laki / perempuan) 'penulisan harus laki-laki'")

# function status perkawinan
def func_sta_per(value_sta_per):
    while True:
        list_sta_per = ["lajang", "menikah", "cerai"]
        func_sta_per_in = input(value_sta_per)
        if func_sta_per_in in list_sta_per:
            return func_sta_per_in
        else :
            print("pilih isi yang sesuai ( lajang / menikah / cerai)")

# function pendidikan terakhir
def func_pe_ter(value_pe_ter):
    while True:
        list_pe_ter = ["sd", "smp", "sma", "s1", "s2", "s3"]
        func_pe_ter_in = input(value_pe_ter)
        if func_pe_ter_in in list_pe_ter:
            return func_pe_ter_in
        else :
            print("pilih isi yang sesuai (sd/ smp/ sma/ s1/ s2/ s3)")

# function jabatan
def func_jabatan(value_jabatan):
    while True:
        list_jabatan = ["ceo", "direktur", "manager", "karyawan"]
        func_jabatan_in = input(value_jabatan)
        if func_jabatan_in in list_jabatan:
            return func_jabatan_in
        else :
            print("pilih isi yang sesuai (ceo/ direktur/ manager/ karyawan)")

# function manajemen
def func_manajemen(value_manajemen):
    while True:
        list_manajemen = ["eksekutif", "keuangan", "marketing", "produksi", "it"]
                        
        func_manajemen_in = input(value_manajemen)
        if func_manajemen_in in list_manajemen:
            if func_manajemen_in.replace(" ", ""):
                return func_manajemen_in
        else :
            print("pilih isi yang sesuai (eksekutif/ keuangan/ marketing/ produksi/ it)")

# function status pekerja
def func_sta_ker(value_sta_ker):
    while True:
        list_sta_ker = ["tetap", "kontrak", "magang"]
                        
        func_sta_ker_in = input(value_sta_ker)
        if func_sta_ker_in in list_sta_ker:
            return func_sta_ker_in
        else :
            print("pilih isi yang sesuai ( tetap / kontrak / magang )")

# function update data
def func_up_da(value_up_da):
    while True:
        list_up_da = ["nama", "nik", "tempat lahir", "tanggal lahir", "jenis kelamin" , "alamat", "no telp", "email", "status pernikahan", "pendidikan terakhir", "jabatan", "manajemen", "tanggal masuk", "status karyawan", "gaji pokok", "tunjangan" , "total gaji", "x"]
                        
        func_up_da_in = input(value_up_da)
        if func_up_da_in in list_up_da:
            return func_up_da_in
        else :
            print("pilih isi yang sesuai!")

# function iya / tidak
def func_yes_no(value_yes_no):
    while True:
        list_yes_no = ["iya", "tidak"]
                        
        func_yes_no_in = input(value_yes_no)
        if func_yes_no_in in list_yes_no:
            return func_yes_no_in
        else :
            print("pilih isi yang sesuai! ( iya / tidak)")

# function validasi
def func_validasi(value_validasi):
    while True:
        list_validasi = [ "kembalikan", "hapus permanent" ]
                        
        func_validasi_in = input(value_validasi)
        if func_validasi_in in list_validasi:
            return func_validasi_in
        else :
            print("pilih isi yang sesuai! ( kembalikan / hapus permanent )")
################
# read simulasi pesangon
def read_simulasi():
    input_nik = func_num("\nMASUKAN NIK 'untuk mencari data yang ingin dilihat' ( x = exit ) : ")
    if input_nik is None:
        return
    
    for read_nik in data_karyawan:
        if read_nik["nik"] == input_nik:
            tanggal_masuk = datetime.strptime(read_nik["tanggal masuk"], "%d-%m-%Y")
            tahun_masuk = tanggal_masuk.year
            tahun_sekarang = datetime.now().year

            masa_kerja = tahun_sekarang - tahun_masuk - 1
            pesangon = read_nik["total gaji"] * masa_kerja
            read_nik["pesangon"] = pesangon
            data = [{
                "nama" : read_nik["nama"],
                "masa kerja" : masa_kerja,
                "total gaji" : read_nik["total gaji"],
                "pesangon" : pesangon
            }]

            print(tabulate(data, headers="keys" , tablefmt="fancy_grid", showindex=False ))
            return

    else :
        print(f"\nDATA DENGAN NIK : {input_nik} TIDAK ADA!! ")
        return
        

# read data
def read_data():
    while True:
        input_no = func_num("\n1. MELIHAT SEMUA DATA \n2. MELIHAT SIMULASI PESANGON \nSILAHKAN PILIH NO DIATAS ( x = exit ) ")
        if input_no is None:
            return
        if input_no == "1":
            print(tabulate(data_karyawan, headers="keys", tablefmt="fancy_grid", showindex=range(1, len(data_karyawan)+1)))
            return
        if input_no == "2":
            read_simulasi()
            return
        else:
            print("MASUKAN NO YANG SESUAI DIATAS")
            

# mencari data bedasarkan nik
def read_data_nik():
    input_nik = func_num("\nMASUKAN NIK 'untuk mencari data yang ingin dicari' ( x = exit ): ")
    if input_nik is None:
        return

    for read_nik in data_karyawan:
        if read_nik["nik"] == input_nik:
            print("Data ditemukan:")
            print(tabulate([read_nik], headers="keys", tablefmt="fancy_grid")) 
            return
            
    else:
        print(f"\nDATA DENGAN NIK : {input_nik}, TIDAK ADA!! ")
        return
        


# mencari data bedasarkan manajemen
def read_manajemen():
    manajemen_in = func_manajemen("\n1. eksekutif \n2. keuangan \n3. marketing \n4. produksi \n5. it  \nMASUKAN NAMA MANAGEMENT ( cth : maraketing ) : ").upper()
    hasil = []

    for manajemen in data_karyawan:
        if manajemen["manajemen"] == manajemen_in:
            hasil.append([manajemen["nama"], manajemen["manajemen"]])

    if hasil:
        print(tabulate(hasil, headers=["Nama", "Manajemen"], tablefmt="fancy_grid", showindex=range(1, len(hasil)+1)))
        return
    else:
        print(f"\nDATA MANAGEMENT {manajemen_in} TIDAK ADA!! ")


####################
# create data karyawan
def create_data(): 

    jumlah_data = int(func_num("berapa data yang ingin di tambahkan ? "))
            
    for jumlah_data_range in range(jumlah_data):
        print(f"\ndata ke-{jumlah_data_range + 1}")

        nama = func_re_pha("NAMA : ").upper()
        nik = func_nik("NIK : ")
        tempat_lahir = func_re_pha("TEMPAT LAHIR : ").upper()
        tanggal_lahir = func_date("TANGGAL LAHIR ( cth : dd-mm-yyyy ) : ")
        jenis_kelamin = func_gender("JENIS KELAMIN ( laki-laki / perempuan ) : ").upper()
        alamat = func_alamat("ALAMAT ( cth : provinsi kota/kabupaten kecamatan desa rt.01/rw.01 ) : ").upper()
        no_telp = func_no_tlpn("NO TELP ( cth : 08xxxxxxxx / +628xxxxxxxxx ) : ")
        email = func_email("EMAIL ( cth : xxxxx@gmail.com ) : ")
        status_pernikahan = func_sta_per("STATUS PERKAWINAN ( lajang / menikah / cerai ) : ").upper()
        pendidikan_terakhir = func_pe_ter("PENDIDIKAN TERAKHIR ( sd/ smp/ sma/ s1/ s2/ s3) : ").upper()
        jabatan = func_jabatan("JABATAN ( ceo/ direktur/ manager/ karyawan) : ").upper()
        manajemen = func_manajemen("MANAJEMEN ( eksekutif/ keuangan/ marketing/ produksi/ it) : ").upper()
        tanggal_masuk = func_date("TANGGAL MASUK ( cth : dd-mm-yyyy ) : ")
        status_karyawan = func_sta_ker("STATUS PEKERJA ( tetap / kontrak / magang ) : ").upper()
        gaji_pokok = int(func_num("GAJI POKOK : "))
        tunjangan = int(func_num("TUNJANGAN : "))
        total_gaji = gaji_pokok + tunjangan  
        data_karyawan.append({
           "nama": nama,
            "nik": nik,
            "tempat lahir" : tempat_lahir,
            "tanggal lahir" : tanggal_lahir,
            "jenis kelamin" : jenis_kelamin,
            "alamat" : alamat,
            "no telp" : no_telp,
            "email" : email,
            "status pernikahan" : status_pernikahan,
            "pendidikan terakhir" : pendidikan_terakhir,
            "jabatan" : jabatan,
            "manajemen" : manajemen,
            "tanggal masuk" : tanggal_masuk,
            "status karyawan" : status_karyawan,
            "gaji pokok" : gaji_pokok,
            "tunjangan" : tunjangan,
            "total gaji" :  total_gaji
            })
        
    print("data berhasil ditambah : \n",tabulate(data_karyawan, headers="keys", tablefmt="fancy_grid", showindex=range(1, len(data_karyawan)+1)))

    tanya_ulang = func_yes_no("\nAPAKAH INGIN MENYIMPAN DI DATA_KARYAWAN.CSV ( iya / tidak ) ? ")
    if tanya_ulang == "iya":
        create_da_kar = pd.DataFrame(data_karyawan)
        create_da_kar.to_csv("data_karyawan.csv", index=False)
    elif tanya_ulang == "tidak":
        return 



#update data bedasarkan nik
def update_data():
    input_nik = func_num("silahkan masukan NIK yang datanya ingin anda ubah ( x = exit ) : ")
    if input_nik is None:
        return

    for list_data_update in data_karyawan:
        if list_data_update["nik"] == input_nik:
            print(tabulate([list_data_update], headers="keys", tablefmt="fancy_grid"))

            pilih_up_da = func_up_da("1.nama \n2.nik \n3.tempat lahir \n4.tanggal lahir \n5.jenis kelamin  \n6.alamat \n7.no telp \n8.email \n9.status pernikahan \n10.pendidikan terakhir \n11.jabatan \n12.manajemen \n13.tanggal masuk \n14.status karyawan \n15.gaji pokok \n116.tunjangan\n  \nMASUKAN NAMA DATA YANG INGIN UBAH ( cth : nama,alamat ) ( x = exit ) : ")
            
            if pilih_up_da in ["nama", "tempat lahir"]:
                value_baru = func_re_pha(f"\nMASUKAN {pilih_up_da.upper()} BARU : ").upper()
                print(f"{pilih_up_da.upper()} BERHASIL DI UBAH")
            
            elif pilih_up_da == "nik":
                value_baru = int( func_nik(f"\nMASUKAN {pilih_up_da.upper()} BARU : "))
                print(f"{pilih_up_da.upper()} BERHASIL DI UBAH!")

            elif pilih_up_da == "jenis kelamin":
                value_baru = func_gender(f"\nMASUKAN {pilih_up_da.upper()} BARU ( laki-laki / perempuan ) : ").upper()
                print(f"{pilih_up_da.upper()} BERHASIL DI UBAH!")

            elif pilih_up_da == "alamat":
                value_baru = func_alamat(f"\nMASUKAN {pilih_up_da.upper()} BARU ( cth : provinsi kota/kabupaten kecamatan desa rt.01/rw.01 ) : ").upper()
                print(f"{pilih_up_da.upper()} BERHASIL DI UBAH!")

            elif pilih_up_da in ["tanggal lahir", "tanggal masuk"]:
                value_baru = func_date(f"\nMASUKAN {pilih_up_da.upper()} BARU ( cth : dd-mm-yyyy ) : ")
                print(f"{pilih_up_da.upper()} BERHASIL DI UBAH!")

            elif pilih_up_da == "no telp":
                value_baru = func_no_tlpn(f"\nMASUKAN {pilih_up_da.upper()} BARU ( cth : 08xxxxxxxx / +628xxxxxxxxx ) : ")
                print(f"{pilih_up_da.upper()} BERHASIL DI UBAH!")

            elif pilih_up_da == "email":
                value_baru = func_email(f"\nMASUKAN {pilih_up_da.upper()} BARU ( cth : xxxxx@gmail.com ) : ")
                print(f"{pilih_up_da.upper()} BERHASIL DI UBAH!")

            elif pilih_up_da == "status pernikahan":
                value_baru = func_sta_per(f"\nMASUKAN {pilih_up_da.upper()} BARU ( lajang / menikah / cerai ) : ").upper()
                print(f"{pilih_up_da.upper()} BERHASIL DI UBAH!")

            elif pilih_up_da == "pendidikan terakhir":
                value_baru = func_pe_ter(f"\nMASUKAN {pilih_up_da.upper()} BARU ( sd/ smp/ sma/ s1/ s2/ s3) : ").upper()
                print(f"{pilih_up_da.upper()} BERHASIL DI UBAH!")

            elif pilih_up_da == "jabatan":
                value_baru = func_jabatan(f"\nMASUKAN {pilih_up_da.upper()} BARU ( ceo/ direktur/ manager/ karyawan) : ").upper()
                print(f"{pilih_up_da.upper()} BERHASIL DI UBAH!")

            elif pilih_up_da == "manajemen":
                value_baru = func_manajemen(f"\nMASUKAN {pilih_up_da.upper()} BARU ( eksekutif/ keuangan/ marketing/ produksi/ it) : ").upper()
                print(f"{pilih_up_da.upper()} BERHASIL DI UBAH!")

            elif pilih_up_da == "status karyawan":
                value_baru = func_sta_ker(f"\nMASUKAN {pilih_up_da.upper()} BARU ( tetap / kontrak / magang ) : ").upper()
                print(f"{pilih_up_da.upper()} BERHASIL DI UBAH!")

            elif pilih_up_da in [ "gaji pokok", "tunjangan"]:
                value_baru = int(func_num(f"\nMASUKAN {pilih_up_da.upper()} BARU : "))
                list_data_update[pilih_up_da] = value_baru
                list_data_update["total gaji"] = list_data_update["gaji pokok"] + list_data_update["tunjangan"]

            elif pilih_up_da == "x":
                return


            list_data_update[pilih_up_da] = value_baru
            print(tabulate([list_data_update], headers="keys" , tablefmt="fancy_grid"))
            return
                
    else :
        print(f"\nDATA DENGAN NIK : {input_nik}, TIDAK ADA!! ")
        return

#
history_del = []

# menghapus data bedasarkan nik
def delete_data():
    input_nik = func_num("silahkan masukkan NIK yang datanya ingin Anda hapus ( x = exit ) : ")
    if input_nik is None:
        return
    
    for hapus, del_data in enumerate(data_karyawan):
        if del_data["nik"] == input_nik:
            print("Data ditemukan:")
            print(tabulate([del_data], headers="keys", tablefmt="fancy_grid"))
            while True:
                tanya_ulang = func_yes_no("\nAPAKAH YAKIN INGIN MENGHAPUS DATA INI ( iya / tidak ) ? ")
                if tanya_ulang == "iya":
                    history_del.append(del_data)
                    del data_karyawan[hapus]
                    print("Data berhasil dihapus!")
                    print(tabulate(data_karyawan, headers="keys" , tablefmt="fancy_grid", showindex=range(1, len(data_karyawan)+1)))
                    print("DATA YANG DIHAPUS DIKIRIM KE history del")
                    print(tabulate(history_del, headers="keys" , tablefmt="fancy_grid", showindex=range(1, len(history_del)+1)))
                    return
                elif tanya_ulang == "tidak":
                    print("Data tidak dihapus!")
                    return
                else:
                    print("pilih yang sesuai (iya / tidak).")
                
    else:
        print(f"\nDATA DENGAN NIK : {input_nik}, TIDAK ADA!! ")
        return

## restore data
def restore_data():
    input_nik = func_num("silahkan masukkan NIK yang datanya ingin Anda dikembalikan ( x = exit ) : ")
    if input_nik is None:
        return
    
    for restore, restore_data in enumerate(history_del):
        if restore_data["nik"] == input_nik:
            print("Data ditemukan:")
            print(tabulate([restore_data], headers="keys", tablefmt="fancy_grid")) 
            while True:
                tanya_ulang = func_validasi("\nAPAKAH BENAR DATA DI ATAS MAU DI ( kembalikan / hapus permanent ) ? ")
                if tanya_ulang == "kembalikan":
                    data_karyawan.append(restore_data)
                    del history_del[restore]
                    print("Data berhasil dikembalikan!")
                    print(tabulate(data_karyawan, headers="keys" , tablefmt="fancy_grid", showindex=range(1, len(data_karyawan)+1)))
                    print("DATA YANG ADA DI history del")
                    if history_del:
                        print(tabulate(history_del, headers="keys" , tablefmt="fancy_grid", showindex=range(1, len(history_del)+1)))
                        return
                    else:
                        print("data tidak ada!!")   
                        return 
                    
                elif tanya_ulang == "hapus permanent":
                    del history_del[restore]
                    print(tabulate(data_karyawan, headers="keys", tablefmt="fancy_grid", showindex=range(1, len(data_karyawan)+1)))
                    print("Data berhasil dihapus!")
                    return
                else:
                    print("pilih yang sesuai (iya / tidak).")
                
    else:
        print(f"\nDATA DENGAN NIK : {input_nik}, TIDAK ADA!! ")
        return



def menu_utama():
    print("\n### MENU UTAMA ###")
    print("\n1. CREATE DATA   \n2. READ DATA  \n3. UPDATE DATA KARYAWAN \n4. DELETE DATA \n5. RESTORE/MENGEMBALIKAN DATA \n6. MENCARI DATA BEDASARKAN NIK \n7. MENCARI DATA BEDASARKAN MANAJEMEN \n8.EXIT/KELUAR")
    while True :
        pilih_fungsi = func_num("SILAHKAN PILIH NO DIATAS : ")
        if pilih_fungsi == "1" :
            print(" \n## CREATE DATA KARYAWAN ## ")
            create_data()
            menu_utama()
            return
        
        elif pilih_fungsi == "2" :
            print(" \n## READ SEMUA DATA KARYAWAN ## ")
            read_data()
            menu_utama()
            return    
        
        elif pilih_fungsi == "3" :
            print(" \n## UPDATE DATA KARYAWAN ## ")
            update_data()
            menu_utama()
            return

        elif pilih_fungsi == "4" :
            print(" \n## DELETE DATA KARYAWAN ## ")
            delete_data()
            menu_utama()
            return

        elif pilih_fungsi == "5" :
            print(" \n## RESTORE/MENGEMBALIKAN DATA KARYAWAN ## ")
            restore_data()
            menu_utama()
            return

        elif pilih_fungsi == "6" :
            print(" \n## MENCARI DATA KARYAWAN BEDASARKAN NIK ## ")
            read_data_nik()
            menu_utama()
            return

        elif pilih_fungsi == "7" :
            print(" \n## MENCARI DATA KARYAWAN BEDASARKAN MANAJEMEN ## ")
            read_manajemen()
            menu_utama()
            return
        
        elif pilih_fungsi == "8" :
            print("### TERIMA KASIH ###")
            return 

        else :
            print("pilihan tidak ada, silahkan pilih nomor di atas, atau tekan x jika ingin keluar")

if __name__ == "__main__":  
    menu_utama()