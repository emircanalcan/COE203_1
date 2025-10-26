import time  # Zaman gecikmesi için gerekli modül

print("=== Smart File Download Manager Automation ===")  # Program başlığı

# Otomasyon sistemi tarafından indirilecek dosyalar listesi (isim, boyut MB)
files = [("game.zip", 200), ("movie.mp4", 350), ("document.pdf", 40)]
speed = 5  # Her saniyede indirilen MB miktarı (5 MB/s)

print("\nAutomation system initialized...")  # Otomasyon başlatıldığında bilgi ver
time.sleep(1)  # Gerçekçi gecikme efekti

# Her dosya için indirme işlemi başlat
for file_name, file_size in files:
    downloaded = 0  # Başlangıçta indirilen miktar sıfır
    print(f"\n{file_name} download starting ({file_size} MB)...")  # Dosya indirme başlangıcı
    time.sleep(1)  # Küçük bekleme süresi

    # Kaç saniyede biteceğini hesapla
    steps = file_size // speed
    if file_size % speed != 0:
        steps += 1  # Tam bölünmezse bir adım daha ekle

    # Adım adım indirme süreci
    for second in range(1, steps + 1):
        downloaded = second * speed  # Her saniye 5 MB indiriliyor
        if downloaded > file_size:
            downloaded = file_size  # Son adımda dosya boyutunu aşma kontrolü

        percent = (downloaded / file_size) * 100  # Yüzdelik oranı hesapla
        print(f"Auto-downloading {file_name}: {downloaded}/{file_size} MB ({percent:.1f}%)")

        time.sleep(1)  # 1 saniyelik gerçek zamanlı bekleme

    print(f"{file_name} download completed successfully!")  # Dosya bittiğinde bilgi ver
    time.sleep(1)  # Sonraki dosyaya geçmeden önce küçük bekleme

print("\nAll downloads completed. Automation shutting down...")  # Tüm dosyalar tamamlandı
time.sleep(2)
print("System powered off automatically.")  # Otomasyon kapatılıyor