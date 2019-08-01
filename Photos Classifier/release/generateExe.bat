call activate py35_qt
pyinstaller -F  -i ..\src\photo.ico -n "Photo Classifier" ..\main.py -w