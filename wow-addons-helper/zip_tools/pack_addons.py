import zipfile
import os


folder_names = [r'Interface', r'WTF']

def zip_dir(root_path, out_file_path):
    zip_tar = zipfile.ZipFile(out_file_path, 'w', zipfile.ZIP_DEFLATED)

    parent_folder = root_path

    for dir_p in folder_names:
        dirpath = os.path.join(root_path, dir_p)
        for root, dirs, files in os.walk(dirpath):
            for dir_name in dirs:
                absolute_path = os.path.join(root, dir_name)
                out_path = os.path.join(out_file_path, dir_name)
                zip_tar.write(absolute_path, out_path)
                print("Add '%s' to archive." % absolute_path)
            for file_name in files:
                absolute_path = os.path.join(root_path,file_name)
                out_path = os.path.join(out_file_path, file_name)
                zip_tar.write(absolute_path, out_path)
                print("Add '%s' to archive." % absolute_path)

        print('done')
        zip_tar.close()