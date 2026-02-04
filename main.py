import os

# --- KONFIGURASI ---
NAMA_FILE = "data_belajar.txt"
catatan = []

def muat_data():
    """Mengambil data dari file txt saat aplikasi dibuka"""
    if os.path.exists(NAMA_FILE):
        try:
            with open(NAMA_FILE, "r") as file:
                for baris in file:
                    if "|" in baris:
                        m, t, d = baris.strip().split("|")
                        catatan.append({"mapel": m, "topik": t, "durasi": int(d)})
        except Exception as e:
            print(f"⚠️ Gagal memuat data: {e}")

def simpan_ke_file():
    """Menyimpan seluruh list catatan ke file txt"""
    try:
        with open(NAMA_FILE, "w") as file:
            for c in catatan:
                file.write(f"{c['mapel']}|{c['topik']}|{c['durasi']}\n")
    except Exception as e:
        print(f"⚠️ Gagal menyimpan data: {e}")

# --- FUNGSI UTAMA ---

def tambah_catatan():
    print("\n[ TAMBAH CATATAN ]")
    mapel = input("Mata Pelajaran : ")
    topik = input("Topik Belajar  : ")
    try:
        durasi = int(input("Durasi (menit) : "))
        catatan.append({"mapel": mapel, "topik": topik, "durasi": durasi})
        simpan_ke_file()
        print("✅ Data tersimpan!")
    except ValueError:
        print("❌ Error: Durasi harus berupa angka!")

def lihat_catatan():
    print("\n[ SEMUA CATATAN BELAJAR ]")
    if not catatan:
        print("Papan skor masih kosong. Yuk, belajar!")
    else:
        print(f"{'No':<4} {'Mapel':<15} {'Topik':<20} {'Durasi'}")
        print("-" * 50)
        for i, c in enumerate(catatan, 1):
            print(f"{i:<4} {c['mapel']:<15} {c['topik']:<20} {c['durasi']} mnt")

def total_waktu():
    print("\n[ RINGKASAN WAKTU ]")
    total = sum(c['durasi'] for c in catatan)
    jam = total // 60
    menit = total % 60
    print(f"Total: {total} menit ({jam} jam {menit} menit)")

# --- FITUR PENGEMBANGAN: FILTER ---
def filter_mapel():
    print("\n[ FILTER PER MAPEL ]")
    cari = input("Masukkan nama mapel: ").lower()
    print("-" * 30)
    ditemukan = [c for c in catatan if cari in c['mapel'].lower()]
    
    if ditemukan:
        for c in ditemukan:
            print(f"• {c['mapel']} - {c['topik']} ({c['durasi']} mnt)")
    else:
        print("Data tidak ditemukan.")

def menu():
    print("\n" + "="*25)
    print("   STUDY LOG APP")
    print("="*25)
    print("1. Tambah Catatan")
    print("2. Lihat Semua Catatan")
    print("3. Total Waktu")
    print("4. Filter Mapel")
    print("5. Keluar")

# --- MAIN LOOP ---
if __name__ == "__main__":
    muat_data()
    while True:
        menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_catatan()
        elif pilihan == "2":
            lihat_catatan()
        elif pilihan == "3":
            total_waktu()
        elif pilihan == "4":
            filter_mapel()
        elif pilihan == "5":
            print("Keep grinding! Sampai jumpa.")
            break
        else:
            print("Pilihan salah, coba lagi.")