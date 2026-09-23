def sortPeserta(peserta):
    # Kerjakan di sini yaw
    if len(peserta) <= 1:
        return peserta
    mid = len(peserta) // 2
    kiri = peserta[:mid]
    kanan = peserta[mid:]
    kiri = sortPeserta(kiri)
    kanan = sortPeserta(kanan)
    return merge(kiri, kanan)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i]["total"] > right[j]["total"]:
            result.append(left[i])
            i += 1
        elif left[i]["total"] == right[j]["total"] and left[i]["penonton"] > right[j]["penonton"]:
            result.append(left[i])
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Program Utama - Jangan di Hapus
data_awal = [
    ("Frieren_Males_Gerak", 88, 90, 85),
    ("Gojo_Nah_Id_Win", 95, 80, 90),
    ("Jett_Rebibe_Me", 87, 90, 88),
    ("Sigma_Mewing_Chad", 80, 95, 75),
    ("Kafka_Stellaron", 92, 88, 95),
    ("Zhongli_Kagak_Punya_Mora", 98, 95, 85),
    ("Windah_Bocil_Kematian", 75, 90, 100),
    ("Anya_Waku_Waku", 95, 90, 85),
    ("Bocil_Epep_Jumpshoot", 70, 60, 99),
    ("Kobo_Pawang_Hujan", 85, 95, 90)
]

peserta = []
for data in data_awal:
    nama = data[0]
    kostum = data[1]
    karakter = data[2]
    penonton = data[3]
    total = kostum + karakter + penonton
    
    data_peserta = {
        "nama": nama,
        "kostum": kostum,
        "karakter": karakter,
        "penonton": penonton,
        "total": total
    }
    peserta.append(data_peserta)

hasil = sortPeserta(peserta)

print("===== HASIL COSWALK COMPETITION - REQUIEM: FEAST TO THE UNSEEN =====")

if hasil:
    for i, p in enumerate(hasil, start=1):
        print(f"Juara {i} : {p['nama']} (Total Skor: {p['total']} | Skor Penonton: {p['penonton']})")
else:
    print("Program belum selesai! Fungsi sortPeserta() belum mengembalikan nilai list yang terurut.")