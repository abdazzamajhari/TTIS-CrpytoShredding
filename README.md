# TTIS-CrpytoShredding
## Proses Kerja Program
1. Impor modul yang diperlukan:
- tkinter digunakan untuk membuat antarmuka grafis.
- filedialog dari tkinter digunakan untuk memilih file dan folder dari sistem.
- messagebox dari tkinter digunakan untuk menampilkan pesan dialog.
- Cipher, algorithms, modes, PBKDF2HMAC, hashes, dan default_backend dari cryptography.hazmat.primitives digunakan untuk enkripsi dan dekripsi menggunakan AES.
- os digunakan untuk operasi file dan direktori.
- shutil digunakan untuk menghapus folder dan isinya.
2. Fungsi shred_file(file_path, key):
- Membaca isi file asli menggunakan open(file_path, 'rb').
- Mengenkripsi data file menggunakan AES-GCM dengan menghasilkan kunci key dan nonce yang dihasilkan secara acak.
- Menulis data terenkripsi ke file asli menggunakan open(file_path, 'wb').
- Menghapus file asli menggunakan os.remove(abs_file_path).
3. Fungsi shred_folder(folder_path, key):
- Menggunakan os.walk untuk mengiterasi melalui semua file dalam folder dan subfolder.
- Memanggil fungsi shred_file untuk setiap file yang ditemukan.
- Menghapus folder dan isinya menggunakan shutil.rmtree.
4. Fungsi select_item():
- Memilih file atau folder menggunakan filedialog.askopenfilename() atau filedialog.askdirectory() berdasarkan opsi yang dipilih oleh pengguna.
- Membaca password dari input pengguna.
- Membangun kunci AES menggunakan PBKDF2HMAC dengan salt yang dihasilkan secara acak dan iterasi sebanyak 100000.
- Menampilkan kotak dialog konfirmasi menggunakan messagebox.askquestion.
- Jika pengguna menyetujui, memanggil fungsi shred_file atau shred_folder berdasarkan opsi yang dipilih oleh pengguna.
- Menampilkan pesan informasi atau peringatan menggunakan messagebox.showinfo atau messagebox.showwarning.
5. Membuat jendela GUI menggunakan tkinter.Tk().
- Menambahkan elemen-elemen GUI seperti label, input, tombol, dan radio button.
- Mengatur event handler untuk tombol menggunakan command.
- Menampilkan jendela GUI menggunakan window.mainloop().

## Contoh Enkripsi
1. Buat file teks dengan konten berikut dan simpan dengan nama "example.txt":
- Ini adalah contoh teks yang akan dienkripsi.
2. Jalankan program "Crypto Shredding" dan ikuti langkah-langkah berikut:
- Pilih opsi "Pilih File".
- Klik tombol "Pilih Item" dan pilih file "example.txt".
- Masukkan password yang akan digunakan untuk enkripsi.
- Klik tombol "OK" pada kotak dialog konfirmasi.
- Akan muncul kotak dialog informasi yang menunjukkan proses selesai.

## Manual Kriptografi
Misalkan kita memiliki file dengan isi sebagai berikut:<br>
File: example.txt<br>
Isi: "Ini adalah contoh teks yang akan dienkripsi."<br>
Kunci yang digunakan adalah "mysecretpassword".<br><br>

Langkah-langkah perhitungan manual:<br>
1. Menghasilkan kunci AES dari password menggunakan PBKDF2HMAC:
- Panjang kunci AES adalah 32 byte (256 bit).
- Salt yang digunakan adalah nilai acak dengan panjang 16 byte.
- Iterasi PBKDF2HMAC adalah 100000.<br>
Hasil perhitungan kunci:<br>
Salt: 0x3a0b31738bdcf94ed8f8ebc1ccfd1ec5<br>
Kunci: 0x6a1c3f5f77f3ce3e8e8494eb35f7e4a295663a30a42f5f7490ea15e9c070b60e<br>

2. Mengenkripsi file menggunakan kunci AES:
- Menggunakan mode AES-GCM dengan nonce yang dihasilkan secara acak.
- Membaca isi file "example.txt" menjadi byte array.
- Mengenkripsi byte array menggunakan kunci dan nonce.
Hasil enkripsi:<br>
Isi terenkripsi (dalam bentuk byte array): 0xe0a95828b2e7a2833044f3a02c5f183fe5735037aa6a8b733ed2d60ddbe4<br>

3. Mengupdate file asli dengan isi terenkripsi:
- Menulis byte array terenkripsi ke file "example.txt".
- Setelah proses tersebut, file "example.txt" telah terenkripsi dengan menggunakan algoritma AES dan kunci yang diberikan.
