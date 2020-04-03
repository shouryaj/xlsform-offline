: Make sure dependencies are installed
pip install PyInstaller wxpython pyxform

: Do some cleanup in case the directory has been built in before
rd /s /q build\xlsform-offline-win 
rd /s /q dist\win
del /s /q *.pyc

: Get some hashing from Git for the file name
git describe --tags --dirty --always > tmp.txt
SET /p BINARY_VERSION= < tmp.txt
DEL tmp.txt
SET EXE_NAME=ODK XLSForm Offline-%BINARY_VERSION%.exe
echo %EXE_NAME% > tmp.txt

: Build the file
python -m PyInstaller pkg\xlsform-offline-win.spec --distpath dist\win --onefile --windowed --noconfirm --clean
DEL tmp.txt