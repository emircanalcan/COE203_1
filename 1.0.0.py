import os
import shutil

# Ana klasördeki fotoğrafları düzenle
def organize_photos():
    # Tüm dosyaları listele
    files = os.listdir("images")
    
    # Her dosya için işlem yap
    for file in files:
        # Dosya yolunu oluştur
        file_path = f"images/{file}"
        
        # Sadece dosyaları işle (klasörleri değil)
        if os.path.isfile(file_path):
            # Dosya uzantısını al (.jpg, .png gibi)
            file_extension = file.split('.')[-1].lower()
            
            # Yeni klasör oluştur (jpeg, jpg, png gibi)
            new_folder = f"images/{file_extension}"
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
            
            # Dosyayı yeni klasöre kopyala
            shutil.copy(file_path, f"{new_folder}/{file}")
            print(f"{file} -> {file_extension} klasörüne kopyalandı")

# Oluşturulan klasörleri temizle
def clean_folders():
    files = os.listdir("images")
    
    for item in files:
        item_path = f"images/{item}"
        # Sadece klasörleri sil (dosyaları değil)
        if os.path.isdir(item_path) and item != "organized":
            shutil.rmtree(item_path)
            print(f"{item} klasörü silindi")

# Ana program
print("Fotoğraf Düzenleyici")
print("1 - Fotoğrafları Düzenle")
print("2 - Klasörleri Temizle")
print("3 - Çıkış")

while True:
    choice = input("Seçiminiz: ")
    
    if choice == "1":
        organize_photos()
        print("Düzenleme tamamlandı!")
    
    elif choice == "2":
        clean_folders()
        print("Temizlik tamamlandı!")
    
    elif choice == "3":
        print("Program kapatılıyor...")
        break
    
    else:
        print("Geçersiz seçim!")