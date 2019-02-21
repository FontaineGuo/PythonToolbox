# coding = utf-8
# this script is for backup world of warcraft addons and personal setting
# the addons and wtf folder will package into one zip file

import zipfile
import os



# the root path of the _retail folder
retail_path = r'F:\BattleNetApps\World of Warcraft\_retail_'

# the path of WTF files, which contains personal setting profiles
folder_names = [r'Interface', r'WTF']

# zip file target
target_path = '' 

def ZipDir(rootpath, dirs,outFilePath):
    zip_tar = zipfile.ZipFile(outFilePath, 'w', zipfile.ZIP_DEFLATED)

    parent_folder = rootpath

    for dir_single in dirs:
        dirpath = os.path.join(rootpath, dir_single)
        for root, folders, filenames in os.walk(dirpath):        
            for folder_name in folders:
                absolute_path = os.path.join(root, folder_name)
                relative_path = absolute_path.replace(parent_folder+'\\', '')
                zip_tar.write(absolute_path, relative_path)
                print("Add '%s' to archive." % absolute_path)
            for file_name in filenames:
                absolute_path = os.path.join(root, file_name)
                relative_path = absolute_path.replace(parent_folder+'\\', '')
                zip_tar.write(absolute_path, relative_path)
                print("Add '%s' to archive." % absolute_path)
    print('done')
    zip_tar.close()

if __name__ == '__main__':
    ZipDir(retail_path,folder_names, r'Addons.zip')
