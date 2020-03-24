pip install PyInstaller wxpython pyxform
rd /s /q build\xlsform-offline-win 
rd /s /q dist\win
del /s /q *.pyc
python -m PyInstaller main.spec --distpath dist\win --onefile --windowed --noconfirm --clean