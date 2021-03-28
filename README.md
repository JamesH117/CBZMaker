# CBZMaker / CBZ Maker
Program to convert directories (folders) into readable comic books for ComicRack.

Program works with multiple levels of folders so only ones that need to be turned into books are converted 
while folders used for storage of books are not converted into books themselves.

## To run as python script:
(1) Make sure latest version of Python 3 is installed

(2) Download python script

(3) Navigate using cmd line to directory containing python script

(4) Type into cmd line: python cbzmaker.py

## To turn into executable file:

(1) Download python script

(2) Make sure pyinstaller is installed with command: pip install pyinstaller

(3) Navigate using cmd line to directory containing python script

(4) Run command in same directory as script file: pyinstaller --onefile cbzmaker.py

  (4a) To customize icon: pyinstaller --onefile --icon=<icon_name_here>.ico cbzmaker.py

(5) Executable will be inside dist folder

