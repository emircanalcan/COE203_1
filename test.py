import time  # Zaman gecikmesi için gerekli modül

print("=== Smart File Download Manager Automation ===")  # Program başlığı

# İndirilecek dosyalar (isim, boyut MB)
files = [("game.zip", 200), ("movie.mp4", 350), ("document.pdf", 40), ("music.mp3", 90)]
speed = 5  # Her saniyede indirilen MB miktarı

print("\nAutomation system initialized...")  # Otomasyon başlatıldığında bilgi ver
time.sleep(1)  # Gerçekçi gecikme efekti

# Klasör yapısı (dosya uzantısına göre)
folders = {
    "zip": "Archives",
    "mp4": "Videos",
    "mp3": "Music",
    "pdf": "Documents"
}

# İndirilen dosyaların saklandığı sanal klasör listesi
downloaded_files = {
    "Videos": [],
    "Documents": [],
    "Music": [],
    "Archives": []
}

# Her dosya için indirme işlemi başlat
for file_name, file_size in files:
    downloaded = 0  # Başlangıçta indirilen miktar sıfır
    print(f"\n{file_name} download starting ({file_size} MB)...")
    time.sleep(1)

    # Adım sayısını hesapla
    steps = file_size // speed
    if file_size % speed != 0:
        steps += 1

    # Adım adım indirme süreci
    for second in range(1, steps + 1):
        downloaded = second * speed
        if downloaded > file_size:
            downloaded = file_size

        percent = (downloaded / file_size) * 100
        print(f"Auto-downloading {file_name}: {downloaded}/{file_size} MB ({percent:.1f}%)")
        time.sleep(1)

    print(f"{file_name} download completed successfully!")
    time.sleep(1)

    # Dosyanın türünü (uzantısını) bul
    extension = file_name.split(".")[-1]  # Örneğin "movie.mp4" -> "mp4"
    
    # Klasör türünü belirle
    folder_name = folders.get(extension, "Other")  # Eşleşmeyen türler "Other" klasörüne gider

    # Dosyayı ilgili klasöre taşı (simülasyon)
    downloaded_files[folder_name].append(file_name)
    print(f"Automation: {file_name} moved to '{folder_name}' folder.")

time.sleep(1)
print("\nAll downloads completed and organized by file type:\n")

# Klasörlerin son durumunu ekrana yaz
for folder, items in downloaded_files.items():
    print(f"[{folder}] -> {items}")

time.sleep(2)
print("\nSystem shutting down automatically...")
time.sleep(1)
print("Automation complete.")
