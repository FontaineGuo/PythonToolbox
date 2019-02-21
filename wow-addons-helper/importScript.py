# -- coding: utf-8 --
import os
import shutil
import tqdm
from hashlib import md5
from functools import partial
import zipfile
import shutil

def move_dir(srcDir, tgtDir):
    # listdir will show 
    for file in tqdm.tqdm(os.listdir(srcDir),unit='files',desc = srcDir):
        srcFile = os.path.join(srcDir, file)
        tgtFile = os.path.join(tgtDir, file)

        # use shutil tools could easily copy the file but will occur error when 
        # copy a folder
        # shutil.copy(srcFile,tgtFile) 

        if os.path.isfile(srcFile):
            if not os.path.exists(tgtDir):
                os.makedirs(tgtDir)

            if not os.path.exists(tgtFile) or (
                   os.path.exists(tgtFile) and (
                   os.path.getsize(tgtFile) != 
                   os.path.getsize(srcFile))):

                src_fp = open(srcFile, 'rb')
                md5_src = md5(src_fp.read()).hexdigest()
                md5_tgt = None
                src_fp.close()

                while not (md5_src == md5_tgt):
                    shutil.move(srcFile,tgtFile)
                    # with open(srcFile, 'rb') as sf:
                    #     with open(tgtFile, 'wb') as tf:
                    #         record_size = 1048576 # 1024B * 1024 = 1 MB
                    #         records = iter(partial(sf.read, record_size), b'')
                    #         size = int(os.path.getsize(os.path.abspath(srcFile))/record_size)
                    #         for data in tqdm.tqdm(records,
                    #                               total=size,
                    #                               unit='MB',
                    #                               desc = srcFile,
                    #                               mininterval=1,
                    #                               ncols=80):
                    #             tf.write(data)
                    with open(tgtFile, 'rb') as hash_sample:
                        md5_tgt = md5(hash_sample.read()).hexdigest()
            
        if os.path.isdir(srcFile):
            move_dir(srcFile, tgtFile)


tempDir = '.\\Addons'
zipf = zipfile.ZipFile('Addons.zip')
print("extract addons zip")
if not os.path.exists(tempDir):
                os.makedirs(tempDir)
zipf.extractall(path = tempDir)
move_dir(".\\Addons", "C:\\Users\\Fontaine\\Desktop\\Temp")
os.removedirs(tempDir)
   
