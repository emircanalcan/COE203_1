import os
import shutil

def move_files_by_type():
    """
    Programın bulunduğu dizindeki .txt ve .jpg dosyalarını
    otomatik olarak kendi alt klasörlerine taşır.
    """
    # 🔧 Çalıştırılan klasörü bul (her durumda güvenli)
    base_folder = os.getcwd()  

    # 📁 Hedef klasörleri belirle
    text_folder = os.path.join(base_folder, "TextFiles")
    image_folder = os.path.join(base_folder, "ImageFiles")

    # 📂 Klasörleri oluştur (varsa hata vermez)
    os.makedirs(text_folder, exist_ok=True)
    os.makedirs(image_folder, exist_ok=True)

    # 🔍 Dizindeki dosyaları tara
    for file_name in os.listdir(base_folder):
        source_path = os.path.join(base_folder, file_name)

        if not os.path.isfile(source_path):
            continue

        ext = os.path.splitext(file_name)[1].lower()

        if ext == ".txt":
            destination = text_folder
        elif ext == ".jpg":
            destination = image_folder
        else:
            continue

        destination_path = os.path.join(destination, file_name)
        shutil.move(source_path, destination_path)
        print(f"✅ {file_name} -> {destination} klasörüne taşındı")

    print("\n🎉 Tüm uygun dosyalar taşındı!")

if __name__ == "__main__":
    move_files_by_type()
