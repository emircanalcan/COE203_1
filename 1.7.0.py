import os
import shutil

def auto_sort_files():
    """
    'source' klasöründeki tüm dosyaları uzantılarına göre alt klasörlere taşır.
    Dosya adında birden fazla nokta olsa bile, sadece son noktadan sonrası uzantı olarak kabul edilir.
    """

    base_folder = os.path.dirname(os.path.abspath(__file__))
    source_folder = os.path.join(base_folder, "downloads")
    os.makedirs(source_folder, exist_ok=True)

    files = os.listdir(source_folder)
    if not files:
        print("Kaynak klasör boş. Lütfen 'source' klasörüne dosya ekle.")
        return

    for file_name in files:
        source_path = os.path.join(source_folder, file_name)

        if os.path.isfile(source_path):
            # Sadece son noktadan sonraki kısmı uzantı olarak al
            if '.' in file_name:
                ext = file_name.split('.')[-1].lower()  # son nokta sonrası
            else:
                ext = ""

            if ext == "":
                folder_name = "Bilinmeyen"
            else:
                folder_name = ext.upper()

            destination_folder = os.path.join(base_folder, folder_name)
            os.makedirs(destination_folder, exist_ok=True)

            shutil.move(source_path, os.path.join(destination_folder, file_name))
            print(f"{file_name} -> {folder_name} klasörüne taşındı.")

    print("\n✅ Tüm dosyalar uzantılarına göre taşındı!")

# 🚀 Çalıştır
auto_sort_files()
