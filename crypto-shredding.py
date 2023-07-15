# pip install cryptography

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os

# Fungsi untuk mengenkripsi dan menghapus berkas
def shred_file(file_path, key):
    abs_file_path = os.path.abspath(file_path)

    # Membaca isi file original
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Mengenkripsi file dengan AES-GCM
    nonce = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(file_data) + encryptor.finalize()

    # Mengupdate file asli dengan data terenkripsi
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

    print("Enkripsi berkas berhasil:", abs_file_path)

# Fungsi untuk mengenkripsi dan menghapus folder
def shred_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            shred_file(file_path, key)

    print("Enkripsi folder berhasil:", folder_path)

# Fungsi untuk memilih folder atau file yang akan dienkripsi dan dihapus
def select_item():
    item_path = filedialog.askopenfilename() if option.get() == 1 else filedialog.askdirectory()
    if item_path:
        password = entry_key.get().encode("utf-8")

        # Membangun kunci AES menggunakan PBKDF2HMAC
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # Panjang kunci AES adalah 32 byte (256 bit)
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(password)

        result = messagebox.askquestion("Konfirmasi", "Apakah Anda yakin ingin melanjutkan? Ini akan mengenkripsi dan menghapus item yang dipilih secara permanen.", icon='warning')
        if result == 'yes':
            if option.get() == 1:
                shred_file(item_path, key)
            else:
                shred_folder(item_path, key)
            messagebox.showinfo("Informasi", "Proses selesai!")
        else:
            messagebox.showwarning("Peringatan", "Operasi dibatalkan.")
    else:
        messagebox.showwarning("Peringatan", "Item tidak dipilih.")

# Membuat jendela GUI
window = tk.Tk()
window.title("@bgbedul Crypto Shredding")
window.geometry("300x200")

# Label dan input untuk memasukkan password
label_key = tk.Label(window, text="Masukkan Password:")
label_key.pack()

entry_key = tk.Entry(window, show="")
entry_key.pack()

# Opsi untuk memilih item (file atau folder)
option = tk.IntVar()
option.set(1)  # Default: Pilih file

radio_file = tk.Radiobutton(window, text="Pilih File", variable=option, value=1)
radio_file.pack()

radio_folder = tk.Radiobutton(window, text="Pilih Folder", variable=option, value=2)
radio_folder.pack()

# Tombol untuk memilih item
btn_select_item = tk.Button(window, text="Pilih Item", command=select_item)
btn_select_item.pack(pady=20)

# Menjalankan jendela GUI
window.mainloop()
