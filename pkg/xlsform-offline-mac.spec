# -*- mode: python -*-

import site;
for path in site.getsitepackages():
    test_validate_path = os.path.join(path, 'pyxform/validators/odk_validate/bin/ODK_Validate.jar')
    if os.path.exists(test_validate_path):
        validate_path = test_validate_path
    test_iana_path = os.path.join(path, 'pyxform/iana_subtags.txt')
    if os.path.exists(test_iana_path):
        iana_path = test_iana_path

a = Analysis(['../src/main.py'])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='ODK XLSForm Offline',
          console=False
)
coll = COLLECT(exe,
               a.binaries,
               [('res/about.html', os.getcwd() + '/src/res/about.html', 'DATA')],
               [('pyxform/validators/odk_validate/bin/ODK_Validate.jar', validate_path, 'DATA')],
               [('pyxform/iana_subtags.txt', iana_path, 'DATA')],
               name='ODK XLSForm Offline',
               strip=True
)
app = BUNDLE(coll,
             name='ODK XLSForm Offline.app',
             icon='icon.icns',
             info_plist={ 'NSHighResolutionCapable': 'True' }
)