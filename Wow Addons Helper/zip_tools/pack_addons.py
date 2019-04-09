import zipfile
import os


_folder_names = [r'Interface', r'WTF']

def zip_dir(root_path, out_file_path):
    print('processing zip')
    zip_tgt = zipfile.ZipFile(out_file_path, 'w', zipfile.ZIP_DEFLATED)

    parent_folder = root_path

    for dir_p in _folder_names:
        dirpath = os.path.join(root_path, dir_p)
        for root, dirs, files in os.walk(dirpath):
            for dir_name in dirs:
                absolute_path = os.path.join(root, dir_name)
                relative_path = absolute_path.replace(parent_folder + '\\', '')
                zip_tgt.write(absolute_path, relative_path)
                # yield "Add " + absolute_path + " to archive."
            for file_name in files:
                absolute_path = os.path.join(root,file_name)
                relative_path = absolute_path.replace(parent_folder + '\\', '')
                zip_tgt.write(absolute_path, relative_path)
                yield "Add " + absolute_path + " to archive."

    # print('done')
    zip_tgt.close()

# for s in zip_dir("C:\\Users\\Fontaine\\Desktop\\Temp\\SICPs",
#                  "C:\\Users\\Fontaine\\Desktop\\Temp\\Addons.zip"):
#     print(s)

