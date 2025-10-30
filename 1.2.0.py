import os
import shutil

def auto_sort_files():
    """
    Programın bulunduğu klasördeki 'source' klasöründen
    dosyaları uzantılarına göre otomatik olarak alt klasörlere taşır.
    Örnek:
      *.txt -> TXT klasörü
      *.jpg -> JPG klasörü
      *.pdf -> PDF klasörü
    """

    # 📁 Programın bulunduğu klasörü bul
    base_folder = os.path.dirname(os.path.abspath(__file__))

    # 📂 Kaynak klasör (burada dosyalar olacak)
    source_folder = os.path.join(base_folder, "downloads")

    # 📂 Klasör yoksa oluştur
    os.makedirs(source_folder, exist_ok=True)

    # 📄 Dosya listesi al
    files = os.listdir(source_folder)
    if not files:
        print("Kaynak klasör boş. Lütfen 'downloads' klasörüne dosya ekle.")
        return

    for file_name in files:
        source_path = os.path.join(source_folder, file_name)

        if os.path.isfile(source_path):
            # Uzantıyı al (örn: '.txt' -> 'TXT')
            ext = os.path.splitext(file_name)[1].lower().replace('.', '')

            if ext == "":
                folder_name = "Bilinmeyen"
            else:
                folder_name = ext.upper()

            # Hedef klasör
            destination_folder = os.path.join(base_folder, folder_name)
            os.makedirs(destination_folder, exist_ok=True)

            # Taşıma işlemi
            destination_path = os.path.join(destination_folder, file_name)
            shutil.move(source_path, destination_path)
            print(f"{file_name} -> {folder_name} klasörüne taşındı.")

    print("\n✅ Tüm dosyalar uzantılarına göre taşındı!")

# 🚀 Programı çalıştır
auto_sort_files()
