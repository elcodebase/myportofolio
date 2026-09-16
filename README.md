Nama: Jehezkiel Jefferson I Latupeirissa
NPM: 2506611156
Kelas: PBP F

Halo

Jawaban Pertanyaan Reflektif Tugas 1
1a. Pertanyaan: Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti section, article, atau aside? Iya, saya menggunakannya.

1b. Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Elemen section digunakan untuk memisahkan area utama seperti About, Projects, dan Skills. Elemen article membungkus setiap kartu proyek agar menjadi komponen independen, sedangkan aside memuat informasi pelengkap seperti tautan media sosial dan kontak samping.

2a. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Tantangannya ada dua. Pertama, saya harus melakukan penyesuaian galeri proyek berbasis grid agar tidak menyebabkan horizontal overflow pada layar sempit. Kedua, saya harus memastikan agar  transformasi navigasi desktop tidak menjadi tata letak bertumpuk pada tampilan mobile

2b. Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile? Biasanya, informasi krusial diprioritaskan berada di posisi paling atas pada layar mobile, sedangkan elemen pelengkap dipindahkan ke posisi bawah.

3a. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Saya merasakan dua hal. Pertama, setiap pembaruan karya atau riwayat harus dilakukan dengan mengedit kode HTML secara manual. Selain itu, formulir kontak tidak dapat memproses atau menyimpan pesan dari pengunjung tanpa bantuan layanan eksternal.

3b. Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?Saya ingin mengembangkan logika backend untuk menangkap masukan pesan, menyimpannya ke database, dan mengirimkan notifikasi email otomatis.


AI Disclosure
Pada bagian section Skills, AI digunakan untuk membantu memberikan struktur dan komentar awal pada kode. Setelah itu, dilakukan perbaikan secara manual pada kode, seperti merapikan indentation, memastikan setiap skill-card memiliki elemen h3 dan p yang sesuai, serta memeriksa kembali struktur pembuka dan penutup setiap elemen div agar tidak terjadi kesalahan nesting.

###Tugas 2

1. Ketika pengguna membuka halaman portofolio baru, browser akan mengirimkan sebuah HTTP Request ke server web Django. Permintaan ini pertama kali diterima oleh berkas urls.py pada tingkat proyek yang bertugas melakukan routing awal. urls.py proyek mencocokkan pola URL awal, lalu meneruskannya ke urls.py tingkat aplikasi. Selanjutnya, urls.py aplikasi mencocokkan jalur spesifik halaman portofolio dan memanggil fungsi atau kelas view yang bertindak sebagai pemroses utama. View kemudian berinteraksi dengan model untuk mengambil data portofolio dari basis data. Setelah model mengembalikan data tersebut, view menyisipkannya ke dalam template HTML. Template engine mengolah gabungan antara struktur HTML dan data dinamis tersebut menjadi tampilan akhir, lalu view mengembalikannya sebagai HTTP Response berupa dokumen HTML utuh untuk ditampilkan pada browser pengguna.

2. Menyimpan data portofolio pada model alih-alih menuliskannya secara langsung pada template menerapkan prinsip pemisahan peran, yaitu memisahkan pengelolaan data dari antarmuka pengguna. Dampaknya terhadap pemeliharaan aplikasi sangat besar, contohnya ketika ada perubahan atau penambahan data portofolio, pengembang dapat langsung memperbaruinya melalui basis data atau panel admin Django tanpa perlu mengubah berkas kode HTML secara manual. 

3. Perintah makemigrations dan migrate pada Django merupakan dua tahapan berurutan dalam mengelola perubahan struktur basis data. Perintah makemigrations bertugas untuk memeriksa berkas models.py, mendeteksi perubahan skema data yang dilakukan, dan membukukan perubahan tersebut menjadi berkas skrip migrasi baru di folder migrations/ tanpa mengubah basis data secara langsung. Sementara itu, perintah migrate bertugas untuk mengeksekusi berkas skrip migrasi tersebut dan menerapkan perubahan skema secara nyata ke dalam tabel-tabel basis data. Sebagai contoh, jika kita menambahkan bidang baru pada kelas model portofolio di models.py, kita harus menjalankan python manage.py makemigrations terlebih dahulu untuk mendokumentasikan penambahan kolom tersebut ke dalam berkas migrasi, kemudian menjalankan python manage.py migrate agar kolom description benar-benar dibuat pada tabel basis data.