import os
import shutil
from zipfile import ZipFile

"""
Written by James Hauser II
To turn into executable file,
(1) make sure pyinstaller in installed with command: pip install pyinstaller
(2) Run command in same directory as srcipt file: pyinstaller --onefile <your_script_name>.py
"""

cwd = os.getcwd()

path = cwd
files = [f for f in os.listdir(cwd) if not f.endswith(".py") and not f.endswith(".cbz")]

for f in files:
    print("Working on item: [{}]".format(f))
    if os.path.isdir(f):
        temp_path = os.path.join(cwd, f)
        temp_files = [tf for tf in os.listdir(temp_path)]

        new_zip_folder = '{}.zip'.format(f)
        # If new_zip_folder already exists, should never happen, delete zip folder
        # and use folder for new zip
        if new_zip_folder in files:
            files.remove(new_zip_folder)
            os.remove(os.path.join(cwd, new_zip_folder))

        with ZipFile(new_zip_folder,'w') as zip:
            for file in temp_files:
                zip.write(os.path.join(temp_path, file), file)

        shutil.rmtree(f)
        f = new_zip_folder

    if f.endswith(".zip") or f.endswith(".rar"):
        # If a cbz file copy does not exist, rename the zip file to cbz file
        if f[:-3]+"cbz" not in [f for f in os.listdir(cwd)]:
            print("Renaming zip folder to cbz: [{}]".format(f))
            os.rename(f, f[:-3]+"cbz")

        # If we try to rename a zip file to .cbz but a copy already exists,
        # just delete the zip file
        else:
            print("Deleting zip folder since cbz folder exists: [{}]".format(f[:-3]+"cbz"))
            os.remove(os.path.join(cwd, f))
