import os


files_path = r"E:\python fcc\code with harry\clear_clutter_program\text_files"
files = os.listdir(files_path)


for no, file in enumerate(files, start=1):
    old_path = os.path.join(files_path, file)
    new_path = os.path.join(files_path, f"fileno{no}" + os.path.splitext(file)[1])  # keep original extension
    print(f"Renaming '{file}' to 'fileno{no}{os.path.splitext(file)[1]}'")
    os.rename(old_path, new_path)
print(files)