import os
import shutil
from zipfile import ZipFile

'''
Written by GitHub account JamesH117
To turn into executable file,
(1) make sure pyinstaller in installed with command: pip install pyinstaller
(2) Run command in same directory as script file: pyinstaller --onefile <your_script_name>.py
(2a) To customize icon, add before <your_script_name>.py: --icon=<icon_name_here>.ico

'''

cwd = os.getcwd()
# List of files in top folder, with program, with their full file paths
items_inside_dir = [os.path.join(cwd, f) for f in os.listdir(cwd) if not (f.endswith(".py") or f.endswith(".cbz") or f.endswith(".exe"))]
book_extensions = ["cbz", "zip", "rar", "7zip", "cbr", "ini"]

def is_book(some_path):
    print("Looking at item: [{}]".format(some_path))
    if len(some_path) >= 259:
        with open(os.path.join(cwd, "long_file_names.txt"), "a") as f:
            f.write("{}\n".format(some_path))

    if any([some_path.endswith(x) for x in book_extensions]):
        return True

    if os.path.isdir(some_path):
        '''
        Not an already zipped book, now check if it is an unzipped book
        (directory with no folders inside)
        '''
        if os.path.getsize(some_path) == 0:
            return False

        items_inside = [os.path.join(some_path, f) for f in os.listdir(some_path)]

        for x in items_inside:
            if any([x.endswith(y) for y in book_extensions]) or os.path.isdir(x) or x.endswith(".exe"):
                # If any items inside the directory is a book, the directory is not a book
                # If any item inside the directory is also a directory, the top level directory is not a book
                return False

            # if all items inside are not folders, or books, treat some_path as an unzipped book
            return True
    # If unsure at all, treat the path given as not a book
    return False

def book_zipper(some_book_path):
    '''
    1. Zip 'some_book_path' (if unzipped)
    2. Rename extension to 'cbz'
    '''
    #print("Book zipper working on item: [{}]".format(some_book_path))
    if os.path.isdir(some_book_path):
        items_inside_book = [tf for tf in os.listdir(some_book_path)]

        new_book = '{}.cbz'.format(some_book_path)
        with ZipFile(new_book, 'w') as zip:
            for file in items_inside_book:
                zip.write(os.path.join(some_book_path, file), file)

        shutil.rmtree(some_book_path)
        return True
    else:
        if (not some_book_path.endswith("cbz")) and (not some_book_path.endswith("ini")):
            # Rename book to correct extension
            try:
                os.rename(some_book_path, some_book_path[:-3]+"cbz")
            except FileExistsError:
                new_book_name = some_book_path[:-4]+" (dupe).cbz"
                os.rename(some_book_path, new_book_name)
                with open(os.path.join(cwd, "duplicate_books.txt"), "a") as f:
                    f.write("{}\n".format(new_book_name))
            return True


for x in items_inside_dir:
    if x.endswith(".cbz") or x.endswith(".cbr") or x.endswith(".exe"):
        pass
    else:
        if is_book(x):
            book_zipper(x)
        else:
            # Add all inner directories to end of 'items_inside_dir'
            # to check for more books to create
            if os.path.isdir(x):
                items_inside_x = [f for f in os.listdir(x)]
                #print("Appending items: {}".format(items_inside_x))
                items_inside_dir += [os.path.join(x, y) for y in items_inside_x]
