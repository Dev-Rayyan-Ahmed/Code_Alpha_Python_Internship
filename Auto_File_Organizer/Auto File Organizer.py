import os
import shutil

folder_path = input("Organize Files at: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "PDFs": [".pdf"],
    "Documents": [".doc", ".docx", ".txt", ".odt"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    # also Moves files of other Extensions to Misc. folder
}

def organize_files():
    if not os.path.exists(folder_path):
        print("The folder does not exist!")
        return

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        moved = False

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()

            for category, extensions in file_types.items():
                if file_ext in extensions:
                    category_folder = os.path.join(folder_path, category)

                    if not os.path.exists(category_folder):  # Create folder if not exists
                        os.makedirs(category_folder)

                    shutil.move(file_path, os.path.join(category_folder, file))
                    moved = True
                    print(f"Moved: {file} → {category}")

        if not moved:
            Misc_folder = os.path.join(folder_path, "Misc")
            if not os.path.exists(Misc_folder):
                os.makedirs(Misc_folder)

            shutil.move(file_path, os.path.join(Misc_folder, file))
            print(f"Moved: {file} → Misc.")

    print("✅ File organization completed!")



organize_files()
input("Press Enter to Exit. ... . . . ")