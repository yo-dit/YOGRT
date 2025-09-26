#Buatlah aplikasi sederhana untuk sistem penilaian Ujian Siswa SMKN 21 Jakarta dengan 
#ketentuan sebagai berikut: 
#1. Program meminta input: - Nama lengkap siswa (diisi dengan nama Anda masing-masing) - Tentukan nilai KKM nya dan munculkan di output aplikasi Anda - Range Nilai UTS (0–100) - Range Nilai UAS (0–100) 
#2. Program melakukan perhitungan Nilai Akhir Semester: - Nilai akhir = (40% × UTS) + (60% × UAS) - Gunakan operator aritmatika dalam proses perhitungan. 
#3. Program menentukan status kelulusan dengan syarat: - Lulus jika nilai akhir semester ≥ 60 DAN tidak ada nilai (UTS atau UAS) < 40. - Gagal jika nilai akhir semester < 60 ATAU ada nilai < 40. - Gunakan operator pembanding (>=, <) dan operator logika (and, or). 
#4. Program menampilkan hasil: - Nama lengkap Siswa - Nilai UTS Siswa - Nilai UAS Siswa - Status (LULUS atau GAGAL) 
#5. Gunakan operator penugasan (misalnya =, +=, *=) di dalam program. 
#6. Silahkan buat akun github sesuai dengan nama masing-masing! Link  
#https://github.com/  
#7. Silahkan buatkan tutorial pembuatan projek Anda yang di jelaskan secara detail di 
#dalam dokumen Microsoft Word sejelas-jelasnya menurut Anda. Termasuk membuat 
#Akun github.  

#1.input
print("~~~~~~INPUT~~~~~~")
namaL= input("Masukkan nama lengkap: ")
kkm= int(input("KKM nilai: "))
uts= int(input("Nilai UTS(0-100): "))
uas= int(input("Nilai UTS(0-100): "))

#2.nilai akhir
print("~~~~~~Nilai Akhir~~~~~~")
nAkhir = 0#deklarasi
nAkhir += (0.4 * uts)#penugasan += : nAkhir + 40% dari uts
nAkhir += (0.6 * uas)#penugasan += ; nAkhir(sudah ditambah 40% dari uts) + 60% dari uas 

#3.persyaratan lulus
if (nAkhir >= 60 and uts >=40 and uas >=40):
    status= "Anda LULUS!"
else:
    status= "Anda GAGAL!😔🥀"

#4.hasil
print("~~~~~~Surat Kelulusan~~~~~~")
print("Nama Lengkap: ", namaL)
print("Nilai UTS: ", uts)
print("Nilai UAS: ", uas)
print("Status Kelulusan: ", status)