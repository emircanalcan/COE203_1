import os
import shutil

def move_files_by_type():
    """
    Programın bulunduğu klasördeki dosyaları uzantısına göre alt klasörlere taşır.
    .txt -> TextFiles
    .jpg -> ImageFiles
    """

    # 📁 Programın bulunduğu klasörün yolunu bul
    base_folder = os.path.dirname(os.path.abspath(__file__))

    # 📂 Kaynak klasör: programın bulunduğu klasördeki "source" klasörü
    source_folder = os.path.join(base_folder, "source")

    # 📂 Hedef klasörler (otomatik olarak program dizininde oluşturulacak)
    text_folder = os.path.join(base_folder, "TextFiles")
    image_folder = os.path.join(base_folder, "ImageFiles")

    # 🧱 Eğer klasörler yoksa oluştur
    os.makedirs(source_folder, exist_ok=True)
    os.makedirs(text_folder, exist_ok=True)
    os.makedirs(image_folder, exist_ok=True)

    # 📄 Kaynak klasördeki dosyaları al
    files = os.listdir(source_folder)
    if not files:
        print("Kaynak klasör boş.")
        return

    for file_name in files:
        source_path = os.path.join(source_folder, file_name)

        # Sadece dosyaları al (klasörleri atla)
        if os.path.isfile(source_path):
            ext = os.path.splitext(file_name)[1].lower()

            if ext == ".txt":
                shutil.move(source_path, os.path.join(text_folder, file_name))
                print(f"{file_name} -> TextFiles klasörüne taşındı.")
            elif ext == ".jpg":
                shutil.move(source_path, os.path.join(image_folder, file_name))
                print(f"{file_name} -> ImageFiles klasörüne taşındı.")
            else:
                print(f"{file_name} atlandı (tanımlı uzantı değil).")

    print("\n✅ Tüm dosyalar başarıyla taşındı!")

# 🚀 Programı başlat
move_files_by_type()
