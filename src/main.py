from textnode import TextNode, TextType
import os
import shutil

def copy_files_recursive(source_path, dest_path):
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    for filename in os.listdir(source_path):
        file_from = os.path.join(source_path, filename)
        file_too = os.path.join(dest_path, filename)
        print(f"[{file_from}] move to: [{file_too}]")
        if os.path.isfile(file_from):
            shutil.copy(file_from, dest_path)
        else:
            copy_files_recursive(file_from, file_too)

def main():
    print('deleting public folder')
    if os.path.exists('./public'):
        shutil.rmtree('./public')

    copy_files_recursive('./static', './public')

if __name__ == "__main__":
    main()