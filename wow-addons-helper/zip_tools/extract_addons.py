import os
import zipfile




def extract_package(path, path_of_addons):
    zipf = zipfile.ZipFile(path_of_addons)
    print("extract addons zip")
    # if not os.path.exists(tempDir):
    #                 os.makedirs(tempDir)
    zipf.extractall(path = path)