import os, shutil
from dir_mng import file_tools

def get_dir_path():
    pass


def copy_dir(src_dir, tgt_dir):
    # get the file number
    # for root, dirs, files in os.walk(srcDir):
    for dir_file in os.listdir(src_dir):
        s_file = os.path.join(src_dir,dir_file)
        t_file = os.path.join(tgt_dir,dir_file)

        
        if os.path.isfile(s_file):
            if not os.path.exists(tgt_dir):
                os.makedirs(tgt_dir)
            if os.path.exists(t_file):
                if not file_tools.checkMd5(s_file, t_file):
                    shutil.copy(s_file, t_file)
            else:
                shutil.copy(s_file, t_file)



        if os.path.isdir(s_file):
            copy_dir(s_file, t_file)
        

def del_dir(dirPath):
    shutil.rmtree(dirPath)

def _check_path():
    pass


# test
## del_dir('C:\\Users\\Fontaine\\Desktop\\Temp\\Addons')
copy_dir('C:\\Users\\Fontaine\\Desktop\\Temp\\SICP','C:\\Users\\Fontaine\\Desktop\\Temp\\teest_dir')