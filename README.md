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

### Tugas 3
1. Django menyediakan ModelForm supaya struktur form otomatis mengikuti struktur model (field, tipe input, validasi tipe data, hingga batas panjang karakter) tanpa saya harus menuliskan ulang setiap elemen input secara manual dan menjaga konsistensinya setiap kali model berubah. Selain lebih ringkas, ModelForm juga otomatis menjalankan validasi bawaan Django sebelum data disimpan ke database. {% csrf_token %} wajib ditambahkan karena Django mewajibkan setiap request POST menyertakan token rahasia unik yang dibuat server. Tanpa token ini, permintaan akan ditolak sebagai perlindungan dari serangan Cross-Site Request Forgery.

2. JSON lebih disukai dibanding XML pada pengembangan web modern karena strukturnya lebih ringkas sehingga ukuran data yang dikirim lebih kecil dan lebih cepat diproses. JSON juga native terhadap JavaScript karena bentuknya identik dengan object literal JavaScript sehingga di sisi frontend data JSON bisa langsung dipakai tanpa parsing tambahan yang rumit. 

3. Alurnya dimulai saat client mengakses endpoint. View mengambil data dari database melalui Django ORM (Project.objects.all() / Certification.objects.all()), lalu memanggil serializers.serialize("json", queryset) untuk mengubah objek model Python menjadi teks berformat JSON, dan mengembalikannya sebagai HttpResponse dengan content_type="application/json". Proses serialization diperlukan karena objek model Django adalah instance Python  sehingga perlu dikonversi dulu ke format JSON yang bisa dibaca oleh sistem lain di luar Python/Django.

### Tugas 5

1. Debouncing adalah teknik untuk menunda eksekusi fungsi sampai pengguna berhenti melakukan aksi selama waktu tertentu. Pada pencarian AJAX, tanpa debouncing setiap ketikan langsung mengirim request ke server, padahal yang dibutuhkan hanya hasil dari kata terakhir. Di halaman Certifications, saya memasang timer 300 ms yang di-reset setiap kali pengguna mengetik, sehingga request baru dikirim setelah pengguna berhenti mengetik. Dengan begitu, beban server berkurang dan hasil pencarian tidak tertimpa respons request lama.

2. Fetch bersifat asinkron dan mengembalikan Promise, bukan langsung datanya. Await membuat kode menunggu sampai Promise selesai, sehingga kita mendapatkan respons dari server dan bisa memprosesnya, misalnya mengubahnya menjadi JSON. Kalau tidak memakai await, yang didapat masih berupa Promise yang belum selesai, sehingga status respons tidak bisa dicek dan proses pengolahan data akan error karena datanya belum tersedia.

3. XSS adalah serangan ketika penyerang menyisipkan script berbahaya ke dalam data yang nantinya dijalankan di browser pengguna lain, misalnya tag gambar yang menjalankan alert saat halaman dibuka. Template Django lebih aman karena otomatis melakukan escaping pada setiap variabel yang ditampilkan. Sementara itu, data dari AJAX yang dimasukkan langsung ke HTML lewat JavaScript tidak di-escape otomatis, jadi browser bisa membacanya sebagai HTML asli. Karena itu, saya melakukan escaping pada setiap teks di JavaScript dan membersihkan tag HTML di sisi server pada form sertifikasi.

### AI Disclosure Tugas 5

Saya menggunakan Claude untuk memeriksa apakah kode saya sudah memenuhi checklist Tugas 5.

Keterbatasan AI
1. AI tidak bisa melihat tampilan di browser, jadi modal, toast, dan pengujian XSS saya cek sendiri di browser untuk setiap peran. 
2. AI hanya membaca kode yang saya kirim, bukan repo saya langsung, sehingga hasilnya tetap saya cocokkan dengan kode terbaru.

Contoh perbaikan manual yang saya lakukan: 
Mengganti response = self.client.get('/api/projects/') dari esponse = self.client.get('/projects/') pada main/test.py

AI membantu mempercepat pengecekan, tetapi hasilnya tetap perlu saya verifikasi.