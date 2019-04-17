import shutil
import os
import stat
import time


def move_photo_to_folder(src_folder, tgt_folder):
    for root, dirs, files in os.walk(src_folder, True):
        print(root)

move_photo_to_folder("C:\\Users\\Fonta\\Desktop", '')