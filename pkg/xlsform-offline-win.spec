# -*- mode: python ; coding: utf-8 -*-
import site;
for path in site.getsitepackages():
    path = path.replace("lib", "Lib")
    test_validate_path = os.path.join(path, 'pyxform/validators/odk_validate/bin/ODK_Validate.jar')
    if os.path.exists(test_validate_path):
        validate_path = test_validate_path
    test_iana_path = os.path.join(path, 'pyxform/iana_subtags.txt')
    if os.path.exists(test_iana_path):
        iana_path = test_iana_path

block_cipher = None


a = Analysis(['..\\src\\main.py'],
             pathex=['C:\\Users\\piete\\Desktop\\UW\\xlsform-offline'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [('..\\res\\about.html', os.getcwd() + '\\src\\res\\about.html', 'DATA')],
          [('pyxform\\validators\\odk_validate\\bin\\ODK_Validate.jar', validate_path, 'DATA')],
          [('pyxform\\iana_subtags.txt', iana_path, 'DATA')],
          name='ODK XLSform Offline.exe',
          icon='..\\pkg\icon.ico',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
