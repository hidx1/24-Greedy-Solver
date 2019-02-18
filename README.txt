24 Solver dengan Algoritma Greedy

Program ini digunakan untuk mencari kombinasi 4 angka untuk mendapat
hasil 24 terdekat dengan kombinasi operator yang menghasilkan jumlah
poin yang tinggi. Program ini dibuat dengan bahasa pemrograman Python
dengan implementasi algoritma Greedy.

Rumus total poin yang digunakan:
24 - hasil akhir + operator 1 + operator 2 + operator 3 - jumlah kurung

Nilai operator:
+ (5 poin)
- (4 poin)
* (3 poin)
/ (2 poin)
tanda kurung (-1 poin)

Terdapat 2 frontend dan 1 backend.
Frontend pertama berupa GUI yang memanggil 4 kartu random dari deck
Frontend kedua berupa program biasa yang akan membaca file dan memberikan 
output ke file juga

Perintah kompilasi dan run di Windows:
Untuk Frontend pertama: python GUI_Kelompok35.py
Untuk Frontend kedua: python Filereader_Kelompok35.py AA BB 
dengan AA sebagai file input dan BB sebagai file output. Keduanya berupa .txt

File input berisi 4 angka yang dipisahkan dengan whitespace
Contoh: 1 2 3 4

Penggunaan program:
Untuk Frontend pertama:
1. Masukkan perintah Frontend pertama ke command shell
2. Window GUI akan terbuka
3. Tekan tombol Randomize untuk mengambil 4 kartu secara acak
4. Jawaban dan poin yang didapat akan ditampilkan di bagian kiri bawah
5. Tekan tombol reset untuk membuat deck penuh kembali

Untuk Frontend kedua:
1. Buat input file dengan format .txt yang berisi 4 angka dipisah oleh whitespace
2. Masukkan perintah Frontend kedua ke command shell

Contoh Input Output:

Input.txt:
13 6 5 10

Output.txt: 
13+10+6-5 = 24
Point : 14

Versi Python yang digunakan:
Python 3.7.0

Versi kivy yang digunakan (sebagai GUI):
1.10.1