#!/bin/bash
set -e

VERSION=$(grep VERSION src/main.py | sed -e "s|.*'\(.*\)'|\1|")

README='pkg/Read me.txt'

WIN_BINARY='dist/win/ODK XLSForm Offline.exe'
WIN_README='dist/win/Read me.txt'

if [[ -e "$WIN_BINARY" ]]; then
	echo 'Windows version exists';
	fold -w 80 -s "$README" > "$WIN_README";
	mac2unix "$WIN_README" && unix2dos "$WIN_README";
	cd dist/win;
	zip -r9 "ODK-XLSForm-Offline-Windows-$VERSION.zip" . -x "*.DS_Store"
	cd ../..;
fi