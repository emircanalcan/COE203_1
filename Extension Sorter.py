import os, shutil, sys
# define
def auto_sort_files():
    # find source file
    if getattr(sys, 'frozen', False):
        base_folder = os.path.dirname(sys.executable)
    else:
        base_folder = os.path.dirname(os.path.abspath(__file__))
    # assign source file
    source_folder = os.path.join(base_folder, "Downloads")
    # add file if it does not exist
    os.makedirs(source_folder, exist_ok=True)
    # get file list
    files = os.listdir(source_folder)
    if not files:
        # return if downloads is empty
        return
    for file_name in files:
        source_path = os.path.join(source_folder, file_name)
        if os.path.isfile(source_path):
            # taking the "." at the far right
            if '.' in file_name:
                ext = file_name.split('.')[-1].lower()
            else:
                ext = ""
            # "Extensionless" file for extensionless files
            if ext == "":
                folder_name = "Extensionless"
            else:
                folder_name = ext.upper()
            # target file
            destination_folder = os.path.join(base_folder, folder_name)
            os.makedirs(destination_folder, exist_ok=True)
            # file movement
            shutil.move(source_path, os.path.join(destination_folder, file_name))
            print(f"{file_name} moved to {folder_name}.")
    print("\nAll files are moved according to their extensions.")
# run
auto_sort_files()