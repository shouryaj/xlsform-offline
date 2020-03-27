import site;
for path in site.getsitepackages():
    test_validate_path = os.path.join(path, 'pyxform/validators/odk_validate/bin/ODK_Validate.jar')
    if os.path.exists(test_validate_path):
        validate_path = test_validate_path
    test_iana_path = os.path.join(path, 'pyxform/iana_subtags.txt')
    if os.path.exists(test_iana_path):
        iana_path = test_iana_path

a = Analysis(['../src/main.py'])
pyz = PYZ(a.pure, a.zipped_data)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          [('res\\about.html', os.getcwd() + '\\src\\res\\about.html', 'DATA')],
          [('pyxform\\validators\\odk_validate\\bin\\ODK_Validate.jar', validate_path, 'DATA')],
          [('pyxform\\iana_subtags.txt', iana_path, 'DATA')],
          name='ODK Xlsform Offline.exe',
          upx=True,
          console=False
)