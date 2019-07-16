# CBZMaker
Program to convert directories (folders) into readable comic books for ComicRack.

Program works with multiple levels of folders so only ones that need to be turned into books are converted 
while folders used for storage of books are not converted into books themselves.


To turn into executable file:

(1) Download python script

(2) Make sure pyinstaller in installed with command: pip install pyinstaller

(3) Navigate using cmd line to directory containing python script

(4) Run command in same directory as script file: pyinstaller --onefile <your_script_name>.py
  (4a) To customize icon, add before <your_script_name>.py: --icon=<icon_name_here>.ico

(5) Executable will be inside dist folder

