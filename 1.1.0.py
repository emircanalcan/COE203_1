import os
import shutil

def move_files_by_type(Dosyalar, Hedef):
    """
    Belirli uzantılardaki dosyaları, her biri için tanımlanmış farklı klasörlere taşır.
    Taşındıktan sonra kaynak klasörden silinir.
    
    destinations: bir sözlük (dict) olmalı. Örnek:
    {".txt": "C:/Backup/TextFiles", ".jpg": "C:/Backup/Images"}
    """
    files = os.listdir(Dosyalar)

    if not files:
        print("No files found in the source folder.")
        return

    for file_name in files:
        source_path = os.path.join(Dosyalar, file_name)

        # Sadece dosyaları taşı
        if os.path.isfile(source_path):
            extension = os.path.splitext(file_name)[1].lower()

            # Eğer bu uzantı için hedef klasör tanımlıysa
            if extension in Hedef:
                destination_folder = Hedef[extension]

                # Hedef klasör yoksa oluştur
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                    print(f"Created folder: {destination_folder}")

                destination_path = os.path.join(destination_folder, file_name)

                # Dosyayı taşı
                shutil.move(source_path, destination_path)
                print(f"Moved '{file_name}' to '{destination_folder}'")

            else:
                print(f"Skipped '{file_name}' (no destination set for this type)")

    print("\n✅ All files moved to their specific folders!")

# 🔧 Örnek kullanım
source = "C:/Users/Erol/Desktop/python/Dosyalar"

# Uzantılara göre hedef klasörleri tanımla
destinations = {
    ".txt": "C:/Users/Erol/Desktop/python/Metinler",
    ".jpg": "C:/Users/Erol/Desktop/python/Resimler"
}

move_files_by_type(source, destinations)
