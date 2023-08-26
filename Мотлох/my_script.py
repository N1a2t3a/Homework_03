import os
import shutil
import concurrent.futures


def process_directory(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    extension = entry.name.split('.')[-1]
                    extension_folder = os.path.join(path, extension)
                    os.makedirs(extension_folder, exist_ok=True)
                    shutil.move(entry.path, os.path.join(extension_folder, entry.name))
                elif entry.is_dir():
                    process_directory(entry.path)
    except Exception as e:
        print(f"Error processing {path}: {e}")


if __name__ == "__main__":
    root_folder = "Мотлох"

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(process_directory, root_folder)
    
    print("Processing complete.")
