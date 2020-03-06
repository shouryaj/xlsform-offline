# -*- mode: python ; coding: utf-8 -*-

import site;
for path in site.getsitepackages():
    test_validate_path = os.path.join(path, 'pyxform/validators/odk_validate/bin/ODK_Validate.jar')
    if os.path.exists(test_validate_path):
        validate_path = test_validate_path
    test_iana_path = os.path.join(path, 'pyxform/iana_subtags.txt')
    if os.path.exists(test_iana_path):
        iana_path = test_iana_path

block_cipher = None

a = Analysis(['../src/main.py'],
             pathex=['/Users/shouryaj/Desktop/odk/xlsform-offline'],
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
          [],
          exclude_binaries=True,
          name='ODK XLSForm Offline',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               [('res/about.html', os.getcwd() + '/src/res/about.html', 'DATA')],
               [('pyxform/validators/odk_validate/bin/ODK_Validate.jar', validate_path, 'DATA')],
               [('pyxform/iana_subtags.txt', iana_path, 'DATA')],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='ODK XLSForm Offline')
app = BUNDLE(coll,
             name='ODK XLSForm Offline.app',
             icon='icon.icns',
             info_plist={ 'NSHighResolutionCapable': 'True' },
             bundle_identifier=None)
