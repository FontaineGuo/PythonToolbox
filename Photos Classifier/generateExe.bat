call activate py36_qt
pyinstaller -F  -i src\photo.ico -n "Photo Classifier" main.py -w