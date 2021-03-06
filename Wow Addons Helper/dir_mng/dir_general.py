import os, shutil
from dir_mng import file_tools
import ntpath
# current_path = os.path.dirname(__file__)
# print(current_path)
def get_dir_path():
    pass


def copy_dir(src_dir, tgt_dir):
    # get the file number
    # for root, dirs, files in os.walk(srcDir):
    for dir_file in os.listdir(src_dir):
        s_file = os.path.join(src_dir,dir_file)
        t_file = os.path.join(tgt_dir,dir_file)


        # excute copy process if this is a file
        if os.path.isfile(s_file):
            if not os.path.exists(tgt_dir):
                os.makedirs(tgt_dir)
            if os.path.exists(t_file):
                # check the MD5, if the result is the same
                # do not copy this file
                if not file_tools.checkMd5(s_file, t_file):
                   shutil.copy(s_file, t_file)
            else:
                # if the file not exists , copy it directly
                shutil.copy(s_file, t_file)
            yield [s_file, t_file]


        if os.path.isdir(s_file):
            yield  from copy_dir(s_file, t_file)


def del_dir(dir_path):
    shutil.rmtree(dir_path)

def check_wow_retail_path(dir_path):
    dir_names = dir_path.split('\\')
    if (dir_names[-1] == "_retail_") and (dir_names[-2] == "World of Warcraft"):
        return True
        # print("found it !")
    else:
        return  False 
        # print("Not found it !")


# test
## del_dir('C:\\Users\\Fontaine\\Desktop\\Temp\\Addons')
## copy_dir('C:\\Users\\Fontaine\\Desktop\\Temp\\SICP','C:\\Users\\Fontaine\\Desktop\\Temp\\teest_dir')
## check_wow_retail_path("G:\\TempStorge\\asd\\qwd\\World of Warcraft\\_retail_")
# for s in copy_dir('C:\\Users\\Fonta\\Desktop\\Temp\\SICP','C:\\Users\\Fonta\\Desktop\\Temp\\teest_dir'):
#     print(s)
# for s in copy_dir('C:\\Users\\Fontaine\\Desktop\\Temp\\SICP', 'C:\\Users\\Fontaine\\Desktop\\Temp\\teest_dir'):
#     print(s[0] + ' to ' + s[1])

#




