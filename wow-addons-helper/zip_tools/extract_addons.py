import os
import zipfile
from dir_mng import dir_general
import time


def extract_package(path, path_of_addons):
    print("extract addons zip")
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        dir_general.del_dir(path)
        os.makedirs(path)

    with zipfile.ZipFile(path_of_addons, 'r') as zipf:
        for info in zipf.infolist():
            yield info.filename
            zipf.extract(info.filename, path)

    print("extract done")

# start =  time.clock()
# extract_package('.\\Addons', r'Addons.zip')
# end = time.clock() - start
# print("running time is -----" + str(start) + " seconds" )
#
# for info in extract_package('.\\Addons', r'Addons.zip'):
#     print(info)