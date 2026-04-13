# Laporan Hasil Praktikum Jaringan Komputer Modul 4

## Soal Bagian 1
1. Jalankan nslookup untuk mendapatkan alamat IP dari server web di Asia. Berapa alamat IP 
server tersebut? 
<img src="../assets/4-1-1.png">

2. Jalankan nslookup agar dapat mengetahui server DNS otoritatif untuk universitas di Eropa.
<img src="../assets/4-1-2.png">

3. Jalankan nslookup untuk mencari tahu informasi mengenai server email dari Yahoo! Mail 
melalui salah satu server yang didapatkan di pertanyaan nomor 2. Apa alamat IP-nya? 
<img src="../assets/4-1-3.png">

## Soal Bagian 2
1. Cari pesan permintaan DNS dan balasannya. Apakah pesan tersebut dikirimkan melalui UDP 
atau TCP? 
<img src="../assets/4-2-1-1.png">
<img src="../assets/4-2-1-2.png">

2. Apa port tujuan pada pesan permintaan DNS? Apa port sumber pada pesan balasannya? 
<img src="../assets/4-2-2-1.png">
<img src="../assets/4-2-2-2.png">

3. Pada pesan permintaan DNS, apa alamat IP tujuannya? Apa alamat IP server DNS lokal anda 
(gunakan ipconfig untuk mencari tahu)? Apakah kedua alamat IP tersebut sama? 
<img src="../assets/4-2-3-1.png">
<img src="../assets/4-2-3-2.png">

4. Periksa pesan permintaan DNS. Apa “jenis” atau ”type” dari pesan tersebut? Apakah pesan 
permintaan tersebut mengandung ”jawaban” atau ”answers”? 
<img src="../assets/4-2-4-1.png">

5. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau ”answers” yang terdapat di 
dalamnya? Apa saja isi yang terkandung dalam setiap jawaban tersebut? 
<img src="../assets/4-2-5-1.png">

6. Perhatikan paket TCP SYN yang selanjutnya dikirimkan oleh host Anda. Apakah alamat IP 
pada paket tersebut sesuai dengan alamat IP yang tertera pada pesan balasan DNS? 
<img src="../assets/4-2-6-1.png">

7. Halaman web yang sebelumnya anda akses (http://www.ietf.org) memuat beberapa 
gambar. Apakah host Anda perlu mengirimkan pesan permintaan DNS baru setiap kali ingin 
mengakses suatu gambar?
Tidak, host tidak perlu mengirimkan permintaan DNS baru setiap kali mengakses gambar dalam halaman web yang sama. Hal ini karena hasil resolusi DNS disimpan dalam cache dan dapat digunakan kembali selama nilai TTL belum habis. Namun, jika gambar berasal dari domain yang berbeda, maka diperlukan permintaan DNS baru.

## Soal Bagian 3
1. Apa port tujuan pada pesan permintaan DNS? Apa port sumber pada pesan balasan DNS?
<img src="../assets/4-3-1-1.png">
<img src="../assets/4-3-1-2.png">

2. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut 
merupakan default alamat IP server DNS lokal Anda? 
<img src="../assets/4-3-2-1.png">
<img src="../assets/4-3-2-2.png">

3. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan 
tersebut mengandung ”jawaban” atau ”answers”? 
<img src="../assets/4-3-3-1.png">

4. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau “answers” yang terdapat di 
dalamnya. Apa saja isi yang terkandung dalam setiap jawaban tersebut?
<img src="../assets/4-3-4-1.png">

## Soal Bagian 4
1. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut 
merupakan default alamat IP server DNS lokal Anda? 
<img src="../assets/4-4-1-1.png">
<img src="../assets/4-4-1-2.png">

2. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan 
tersebut mengandung ”jawaban” atau ”answers”? 
<img src="../assets/4-4-2-1.png">

3. Periksa pesan balasan DNS. Apa nama server MIT yang diberikan oleh pesan balasan? 
Apakah pesan balasan ini juga memberikan alamat IP untuk server MIT tersebut? 
<img src="../assets/4-4-3-1.png">

## Soal Bagian 5
1. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut 
merupakan default alamat IP server DNS lokal Anda? 
<img src="../assets/4-5-1-1.png">
<img src="../assets/4-5-1-2.png">

2. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan 
tersebut mengandung ”jawaban” atau ”answers”? 
<img src="../assets/4-5-2-1.png">

3. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau “answers” yang terdapat di 
dalamnya. Apa saja isi yang terkandung dalam setiap jawaban tersebut? 
<img src="../assets/4-5-3-1.png">
