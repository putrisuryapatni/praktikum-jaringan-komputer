PRAKTIKUM MODUL 3


A. Basic HTTP GET/response interaction  
1. Jalankan browser web Anda. 
2. Jalankan packet sniffer Wireshark. Masukkan "http" (hanya huruf, bukan tanda kutip, dan 
dalam huruf kecil) di display-filter-specification window (textfield filter paket di bagian atas 
daftar paket), sehingga hanya pesan HTTP yang diambil yang akan ditampilkan nanti di 
jendela daftar paket.  
3. Tunggu sedikit lebih dari satu menit, dan kemudian mulai pengambilan paket Wireshark. 
4. Masukkan berikut ini ke browser Anda http://gaia.cs.umass.edu/wireshark-labs/HTTP
wireshark-file1.html, Browser Anda akan menampilkan file HTML satu baris yang sangat 
sederhana. 
5. Hentikan pengambilan paket Wireshark.

<img src="../assets/32.png">

B. HTTP CONDITIONAL GET/response interaction
1. Jalankan browser web Anda, dan pastikan cache browser Anda dibersihkan (jika belum, 
hapus terlebih dahulu cache dan history browser anda), seperti yang dibahas di atas. 
2. Mulai tangkap paket dengan Wireshark. 
3. Masukkan URL berikut ke browser Anda http://gaia.cs.umass.edu/wireshark-labs/HTTP
wireshark-file2.html Browser Anda akan menampilkan file HTML lima baris yang sangat 
sederhana. 
4. Masukkan kembali URL yang sama ke browser Anda dengan cepat (atau cukup tekan tombol 
refresh di browser Anda). 
5. Hentikan pengambilan paket Wireshark, dan masukkan “http” di jendela spesifikasi filter 
tampilan, sehingga hanya pesan HTTP yang diambil yang akan ditampilkan nanti di jendela 
daftar paket.

<img src="../assets/321.png">

C. Retrieving Long Documents  
1. Jalankan browser web Anda, dan pastikan cache browser Anda dibersihkan (jika belum, hapus 
terlebih dahulu cache dan history browser anda).
2. Mulai tangkap paket dengan Wireshark 
3. Masukkan URL berikut ke browser Anda http://gaia.cs.umass.edu/wireshark-labs/HTTP
wireshark-file3.html Browser Anda seharusnya menampilkan Bill of Rights AS yang agak 
panjang. 
4. Hentikan pengambilan paket Wireshark, dan masukkan “http” di jendela tampilan-filter
spesifikasi, sehingga hanya pesan HTTP yang diambil yang akan ditampilkan.

<img src="../assets/33.png">

D. HTML Documents dengan Embedded Objects 
1. Jalankan browser web Anda, dan pastikan cache browser Anda dibersihkan (jika belum, 
hapus terlebih dahulu cache dan history browser anda), seperti yang dibahas di atas. 
2.Mulai tangkap paket dengan Wireshark. 
3. Masukkan URL berikut ke browser Anda http://gaia.cs.umass.edu/wireshark-labs/HTTP
wireshark-file4.html 
4. Browser Anda harus menampilkan file HTML pendek dengan dua gambar. Kedua gambar ini 
direferensikan dalam file HTML dasar. Artinya, gambar itu sendiri tidak terdapat dalam HTML; 
alih-alih hanya terdapat URL kedua gambar pada file HTML tersebut. Browser Anda harus 
mengambil logo ini dari URL situs web yang disematkan pada file HTML. Logo penerbit kita 
diambil dari situs web gaia.cs.umass.edu. 
5. Hentikan pengambilan paket Wireshark, dan masukkan “http” di jendela tampilan-filter
spesifikasi, sehingga hanya pesan HTTP yang diambil yang akan ditampilkan. 

<img src="../assets/34.png">

E. HTTP Authentication 
1. Jalankan browser web Anda, dan pastikan cache browser Anda dibersihkan (jika belum, hapus 
terlebih dahulu cache dan history browser anda), seperti yang dibahas di atas. 
2. Mulai tangkap paket dengan Wireshark. 
3. Masukkan URL berikut ke browser Anda http://gaia.cs.umass.edu/wireshark
labs/protected_pages/HTTP-wireshark-file5.html Ketik username dan password yang diminta 
ke dalam kotak pop up (username dan password terdapat pada paragraf diatas). 
4. Hentikan pengambilan paket Wireshark, dan masukkan “http” di jendela spesifikasi filter 
tampilan, sehingga hanya pesan HTTP yang diambil yang akan ditampilkan nanti di jendela 
daftar paket.

<img src="../assets/sign-in.png">
<img src="../assets/35.png">
