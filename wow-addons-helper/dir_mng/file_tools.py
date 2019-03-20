import os
from hashlib import md5

def checkMd5(srcFile, tgtFile):
    src_fp = open(srcFile, 'rb')
    md5_src = md5(src_fp.read()).hexdigest()
    src_fp.close()

    tgt_fp = open(tgtFile, 'rb')
    md5_tgt = md5(tgt_fp.read()).hexdigest()
    tgt_fp.close()

    if md5_src == md5_tgt:
        # print("md5 check successed")
        return True
    else:
        # print("md5 check failed")
        return False


    # with open(file_name) as file_to_check:
    #     # read contents of the file
    #     data = file_to_check.read()    
    #     # pipe contents of the file through
    #     md5_returned = hashlib.md5(data).hexdigest()


# test
# checkMd5("C:\\Users\\Fontaine\\Desktop\\Temp\\test.txt",
#          "C:\\Users\\Fontaine\\Desktop\\Temp\\test\\test.txt")

def format_path(path):
    # final_path = path.replace('/', '\\')
    name_list = path.split('/')
    final_path = name_list[0] + '\\'
    for single_name in name_list[1:]:
        final_path = os.path.join(final_path,single_name)
    return final_path

def count_files(path):
    count = 0
    for root,dirs, files in os.walk(path):
        for f in files:
            count += 1
    return count

# print(format_path("C:/Users/Fontaine/Desktop/Temp/World of Warcraft/_retail_"))