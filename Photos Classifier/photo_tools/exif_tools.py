import os
import time
from PIL import Image

def get_exif_date(src_photo):
    try:
        photo_file = Image.open(src_photo)
    except:
        raise "Can't open the file [%s]\\n" % src_photo

    try:
        exif_data = photo_file._getexif()
        if exif_data:
            print("Get exif data")
            return [True ,exif_data]
        else:
            print("Don't get!")
            create_time = os.stat(src_photo)
            return [False, time.strftime("%Y-%m-%d",
            time.localtime(create_time[-2]))]
    except Exception as e:
        print(e)


# ob = get_exif_date("C:\\Users\\Fonta\\Desktop\\WeChat Image_20190416172003.jpg")
# ob = get_exif_date("C:\\Users\\Fonta\\Desktop\\2.jpg")
# Have to check if the exif item exists
# print((ob[1])[0x9003])