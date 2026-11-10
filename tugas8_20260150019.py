import modul_sensor as ms 

# 1. Struktur data utama
log_kebun = []


# 2. Fungsi validasi input
def input_sensor():
    """Mengembalikan tuple (suhu, kelembapan) secara aman."""
    while True:
        try:
            suhu = float(input("Masukkan suhu udara (C) [0-100]: "))
            lembab = float(input("Masukkan kelembapan tanah (%) [0-100]: "))

            if 0 <= suhu <= 100 and 0 <= lembab <= 100:
                return (suhu, lembab)
            else:
                print("Input di luar rentang! Suhu dan kelembapan harus 0-100.\n")
        except ValueError:
            print("Input tidak valid! Masukkan angka, bukan huruf.\n")


# 3. Menu interaktif
def main():
    print("=====================================")
    print(f"    Sistem Monitoring Presisi IoT    ")
    print("=====================================")
    
    while True:
        print("\n--- MENU ---")
        print("[1] Rekam Data")
        print("[2] Analisis Tren (3 Terakhir)")
        print("[3] Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            data = input_sensor()
            log_kebun.append(data)
            print("Data berhasil direkam!")

        elif pilihan == "2":
            if len(log_kebun) == 0:
                print("Belum ada data. Rekam data terlebih dahulu (menu 1).")
            else:
                # Slicing: maksimal 3 data terakhir
                data_slice = log_kebun[-3:]

                print("\nData terakhir yang dianalisis:")
                for i, (suhu, lembab) in enumerate(data_slice, start=1):
                    print(f"{i}. Suhu: {suhu} C | Kelembapan: {lembab} %")

                rata_suhu, rata_lembab = ms.hitung_tren(data_slice)
                status = ms.evaluasi_irigasi(rata_suhu, rata_lembab, ms.AMBANG_KRITIS)

                print(f"\nRata-rata suhu      : {rata_suhu:.2f} C")
                print(f"Rata-rata kelembapan: {rata_lembab:.2f} %")
                print(f"Status              : {status}")

        elif pilihan == "3":
            print("Terima kasih. Program selesai.")
            break

        else:
            print("Pilihan tidak valid! Pilih 1, 2, atau 3.")


main()