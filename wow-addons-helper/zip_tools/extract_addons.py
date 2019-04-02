import os
import zipfile




def extract_package(path, path_of_addons):
    print("extract addons zip")
    with zipfile.ZipFile(path_of_addons, 'r') as zipf:
        zipf.extractall(path=path)
    print("extract done")


# extract_package('.\\Addons', r'Addons.zip')