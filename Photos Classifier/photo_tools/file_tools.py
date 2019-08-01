import shutil
import os
import stat
import time
from photo_tools import exif_tools

def format_path(path):
    # final_path = path.replace('/', '\\')
    if path == "":
        return ""

    name_list = path.split('/')
    final_path = name_list[0] + '\\'
    for single_name in name_list[1:]:
        final_path = os.path.join(final_path,single_name)
    return final_path

def count_files(path):
    count = 0
    for root,dirs, files in os.walk(path):
        for filename in files:
            filename = os.path.join(root, filename)

            f_name, extend_name = os.path.splitext(filename)
            if extend_name.lower() not in ('.jpg', '.png'):
                continue
            else:
                count += 1
    return count


def move_photo_to_folder(src_folder, tgt_folder):
    # create temp folder for information unknown photo
    temp_folder = os.path.join(tgt_folder , 'temp')
    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)


    for root, dirs, files in os.walk(src_folder, True):
        for filename in files:
            filename = os.path.join(root, filename)

            f_name, extend_name = os.path.splitext(filename)
            if extend_name.lower() not in ('.jpg', '.png'):
                continue

            data_pack = exif_tools.get_exif_date(filename)
            if data_pack[0] == True:
                photo_data = data_pack[1]
                original_time = photo_data[0x9003]

                # transform time format and only leave y-m
                original_time = str(original_time).replace(":", "-")[:10]
                time_tag = original_time[:7]

                tgt_single_folder = tgt_folder + '\\' + time_tag
                tgt_location = tgt_single_folder + '\\' + os.path.basename(filename)

                if not os.path.exists(tgt_single_folder):
                    os.mkdir(tgt_single_folder)
                    # use copy2 to preserver metadata
                    shutil.copy2(filename, tgt_location)
                    yield [filename, tgt_location]
                else:
                    shutil.copy2(filename, tgt_location)
                    yield [filename, tgt_location]
            else:
                shutil.copy2(filename, temp_folder)
                yield [filename, tgt_location]

# move_photo_to_folder("C:\\Users\\Fonta\\Desktop\\Temp\\src", 'C:\\Users\\Fonta\\Desktop\\Temp\\tgt')