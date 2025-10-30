import os
import shutil

def move_files_by_type():
    """
    Programın bulunduğu dizindeki .txt ve .jpg dosyalarını
    otomatik olarak kendi alt klasörlerine taşır.
    """
    # 🏠 Programın bulunduğu klasörü bul
    base_folder = os.path.dirname(os.path.abspath(__file__))

    # 📁 Hedef klasörleri belirle
    text_folder = os.path.join(base_folder, "TextFiles")
    image_folder = os.path.join(base_folder, "ImageFiles")

    # 📂 Klasörler yoksa oluştur
    os.makedirs(text_folder, exist_ok=True)
    os.makedirs(image_folder, exist_ok=True)

    # 🔍 Dizindeki tüm dosyaları tara
    for file_name in os.listdir(base_folder):
        source_path = os.path.join(base_folder, file_name)

        # Klasörleri atla
        if not os.path.isfile(source_path):
            continue

        # Dosya uzantısını bul
        ext = os.path.splitext(file_name)[1].lower()

        # Hedefi belirle
        if ext == ".txt":
            destination = text_folder
        elif ext == ".jpg":
            destination = image_folder
        else:
            continue  # diğer dosyaları atla

        # Hedef dosya yolu
        destination_path = os.path.join(destination, file_name)

        # 🪄 Dosyayı taşı (kaynakta silinir)
        shutil.move(source_path, destination_path)
        print(f"✅ {file_name} -> {destination} klasörüne taşındı")

    print("\n🎉 Tüm uygun dosyalar taşındı!")

# 🚀 Programı çalıştır
if __name__ == "__main__":
    move_files_by_type()
