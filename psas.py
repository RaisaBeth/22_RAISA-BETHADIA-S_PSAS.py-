import tkinter as tk
from tkinter import ttk

jendela = tk.Tk()
jendela.title('Aplikasi Kas Kelas')
jendela.geometry("700x450")
jendela.config(bg="#747BAB")

data_kas = []  # tempat menyimpan data kas

# ====================================================
# Fungsi Umum
# ====================================================
def tampilan(frame):
    frame.tkraise()

# ====================================================
# Simpan Data Kas
# ====================================================
def simpandata():
    nama = entry_nama.get()
    tanggal = entry_tanggal.get()
    jumlah = entry_jumlah.get().replace(".", "")  # hapus titik jika user input
    keterangan = entry_keterangan.get()
    kategori = var_kategori.get()
    status_lunas = "Lunas" if cek_status.get() == 1 else "Belum Lunas"

    if not nama or not tanggal or not jumlah:
        label_hasil.config(text="Semua data wajib diisi!", fg="red")
        return
    
    try:
        jumlah = float(jumlah)
        data_kas.append((nama, tanggal, jumlah, keterangan, kategori, status_lunas))
        label_hasil.config(text="Data berhasil disimpan!", fg="green")

        entry_nama.delete(0, tk.END)
        entry_tanggal.delete(0, tk.END)
        entry_jumlah.delete(0, tk.END)
        entry_keterangan.delete(0, tk.END)
        var_kategori.set("Kas")
        cek_status.set(0)

    except:
        label_hasil.config(text="Jumlah harus angka!", fg="red")

# ====================================================
# Tampilkan Data
# ====================================================
def tampilkandata():
    for i in tabel.get_children():
        tabel.delete(i)
    for d in data_kas:
        nama, tanggal, jumlah, keterangan, kategori, status = d
        jumlah_str = f"Rp {jumlah:,.0f}".replace(",", ".")
        tabel.insert("", tk.END, values=(nama, tanggal, jumlah_str, kategori, status, keterangan))

# ====================================================
# Cari Data
# ====================================================
def caridata():
    nama_dicari = entry_cari.get().lower()
    for i in tree_cari.get_children():
        tree_cari.delete(i)

    if not nama_dicari:
        tree_cari.insert("", tk.END, values=("Masukkan nama!", "", "", "", "", ""))
        return

    ketemu = False
    for d in data_kas:
        if nama_dicari in d[0].lower():
            nama, tanggal, jumlah, keterangan, kategori, status = d
            jumlah_str = f"Rp {jumlah:,.0f}".replace(",", ".")
            tree_cari.insert("", tk.END, values=(nama, tanggal, jumlah_str, kategori, status, keterangan))
            ketemu = True
    
    if not ketemu:
        tree_cari.insert("", tk.END, values=("Data tidak ditemukan", "", "", "", "", ""))

# ====================================================
# Hitung Total Kas
# ====================================================
def totalkas():
    total = sum(d[2] for d in data_kas)
    total_str = f"Rp {total:,.0f}".replace(",", ".")
    label_total_kas.config(text=f"Total Uang Kas: {total_str}")

# ====================================================
# HALAMAN 1 — MENU
# ====================================================
hal1 = tk.Frame(jendela, bg="#747BAB")
hal1.place(x=0, y=0, relwidth=1, relheight=1)

tk.Label(hal1, text="Aplikasi Kas Kelas", bg="#747BAB", font=("Times New Roman", 20, "bold")).pack(pady=30)
tk.Button(hal1, text="Tambah Data Kas", command=lambda: tampilan(hal2)).pack(pady=5)
tk.Button(hal1, text="Daftar Kas", command=lambda: tampilan(hal3)).pack(pady=5)
tk.Button(hal1, text="Cari Data Kas", command=lambda: tampilan(hal4)).pack(pady=5)
tk.Button(hal1, text="Total Kas", command=lambda: tampilan(hal5)).pack(pady=5)

# ====================================================
# HALAMAN 2 — INPUT DATA (5 FIELD BERBEDA)
# ====================================================
hal2 = tk.Frame(jendela, bg="#747BAB")
hal2.place(x=0, y=0, relwidth=1, relheight=1)

tk.Label(hal2, text="Tambah Data Kas", bg="#747BAB", font=("Times New Roman", 18)).pack(pady=10)

# String
tk.Label(hal2, text="Nama:", bg="#747BAB").pack()
entry_nama = tk.Entry(hal2)
entry_nama.pack()

# String
tk.Label(hal2, text="Tanggal (dd-mm-yyyy):", bg="#747BAB").pack()
entry_tanggal = tk.Entry(hal2)
entry_tanggal.pack()

# Float / Integer
tk.Label(hal2, text="Jumlah (10000 / 10.000):", bg="#747BAB").pack()
entry_jumlah = tk.Entry(hal2)
entry_jumlah.pack()

# OptionMenu
tk.Label(hal2, text="Kategori Pembayaran:", bg="#747BAB").pack()
var_kategori = tk.StringVar()
var_kategori.set("Kas")
option_kategori = tk.OptionMenu(hal2, var_kategori, "Kas", "Utang", "Donasi", "Denda",'Lainnya')
option_kategori.pack()

# Checkbox
tk.Label(hal2, text="Status Pembayaran:", bg="#747BAB").pack()
cek_status = tk.IntVar()
tk.Checkbutton(hal2, text="Sudah Lunas", variable=cek_status, bg="#747BAB").pack()

# String
tk.Label(hal2, text="Keterangan:", bg="#747BAB").pack()
entry_keterangan = tk.Entry(hal2)
entry_keterangan.pack()

label_hasil = tk.Label(hal2, text="", bg="#747BAB")
label_hasil.pack()

tk.Button(hal2, text="Simpan", command=simpandata).pack(pady=5)
tk.Button(hal2, text="Kembali", command=lambda: tampilan(hal1)).pack()

# ====================================================
# HALAMAN 3 — DAFTAR KAS
# ====================================================
hal3 = tk.Frame(jendela, bg="#747BAB")
hal3.place(x=0, y=0, relwidth=1, relheight=1)

tk.Label(hal3, text="Daftar Kas Kelas XI", bg="#747BAB", font=("Times New Roman", 18)).pack(pady=10)

kolom = ("Nama", "Tanggal", "Jumlah", "Kategori", "Status", "Keterangan")
tabel = ttk.Treeview(hal3, columns=kolom, show="headings")
for k in kolom:
    tabel.heading(k, text=k)
    tabel.column(k, width=120, anchor='center')
tabel.pack(fill="both", expand=True)

tk.Button(hal3, text="Tampilkan Data", command=tampilkandata).pack(pady=5)
tk.Button(hal3, text="Kembali", command=lambda: tampilan(hal1)).pack()

# ====================================================
# HALAMAN 4 — CARI DATA
# ====================================================
hal4 = tk.Frame(jendela, bg="#747BAB")
hal4.place(x=0, y=0, relwidth=1, relheight=1)

tk.Label(hal4, text="Cari Data Kas", bg="#747BAB", font=("Times New Roman", 18)).pack(pady=20)
tk.Label(hal4, text="Nama:", bg="#747BAB").pack()
entry_cari = tk.Entry(hal4)
entry_cari.pack()

kolom_cari = ("Nama", "Tanggal", "Jumlah", "Kategori", "Status", "Keterangan")
tree_cari = ttk.Treeview(hal4, columns=kolom_cari, show="headings", height=8)
for k in kolom_cari:
    tree_cari.heading(k, text=k)
tree_cari.pack(fill="x", padx=10, pady=10)

tk.Button(hal4, text="Cari", command=caridata).pack(pady=5)
tk.Button(hal4, text="Kembali", command=lambda: tampilan(hal1)).pack()

# ====================================================
# HALAMAN 5 — TOTAL KAS
# ====================================================
hal5 = tk.Frame(jendela, bg="#747BAB")
hal5.place(x=0, y=0, relwidth=1, relheight=1)

tk.Label(hal5, text="Total Kas Kelas XI", bg="#747BAB", font=("Times New Roman", 18)).pack(pady=20)

label_total_kas = tk.Label(hal5, text="Total Uang Kas: Rp 0", bg="#747BAB", font=("Arial", 14, "bold"))
label_total_kas.pack(pady=20)

tk.Button(hal5, text="Hitung Total Kas", command=totalkas).pack(pady=10)
tk.Button(hal5, text="Kembali", command=lambda: tampilan(hal1)).pack()

# ====================================================
# Jalankan Aplikasi
# ====================================================
for f in (hal1, hal2, hal3, hal4, hal5):
    f.place(x=0, y=0, relwidth=1, relheight=1)

tampilan(hal1)
jendela.mainloop()
