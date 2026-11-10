# Konstanta bertipe Tuple
LOKASI = ("Kampung Anggur Plumbungan", -7.828, 110.378)
AMBANG_KRITIS = (35.0, 40.0)  

def hitung_tren(data_slice):
    """Menerima list of tuple (suhu, kelembapan),
    mengembalikan rata-rata suhu dan rata-rata kelembapan."""
    if len(data_slice) == 0:
        return 0, 0, 0

    total_suhu = 0
    total_lembab = 0
    for suhu, lembab in data_slice:
        total_suhu += suhu
        total_lembab += lembab

    rata_suhu =  total_suhu / len(data_slice)
    rata_lembab = total_lembab / len(data_slice)
    return rata_suhu, rata_lembab


def evaluasi_irigasi(rata_suhu, rata_lembab, tuple_kritis):
    """Mengembalikan status irigasi berdasarkan ambang kritis."""
    suhu_max, lembab_min = tuple_kritis

    if rata_suhu > suhu_max or rata_lembab < lembab_min:
        return "[KRITIS]: Nyalakan Pompa Irigasi!"
    else:
        return "[NORMAL]: Pompa Mati."