import os
import time
import datetime
import shutil


dir = "F:/downloads"
files = os.listdir(dir)

# Extensions for Categorizations
images = ["png", "jpg", "jpeg", "bmp", "gif", "svg"]
videos = ["mp4", "3gp", "ogg", "wmv", "webm", "flv", "avi", "mpeg"]
installers = ["exe", "msi"]
documents = ["zip", "txt", "csv", "json",
             "xls", "xlsx", "doc", "docx", "pdf"]

dirpath = "F:/Downloads_"


# loop through and identify File Category
for file in files:
    filename = os.path.join(dir, file)
    createdyear = str(time.localtime(os.stat(filename).st_mtime).tm_year)
    createdmonth = str(time.localtime(os.stat(filename).st_mtime).tm_mon)
    # Identify File Extension
    if os.path.isdir(os.path.join(dir, file)):
        category = "Directory"
    else:
        file_ext = file.split('.')[-1]
        if images.__contains__(file_ext):
            category = "Images"
        elif videos.__contains__(file_ext):
            category = "Videos"
        elif installers.__contains__(file_ext):
            category = "Installers"
        elif documents.__contains__(file_ext):
            category = "Documents"
        else:
            category = "Others"
    des_dir = os.path.join(dirpath, category,
                           createdyear, createdmonth, file)
    # Check Dir Exists and Create One
    # Main Category
    if not os.path.exists(os.path.join(dirpath, category)):
        os.makedirs(os.path.join(dirpath, category))
    # SubCategory-Year
    if not os.path.exists(os.path.join(dirpath, category, createdyear)):
        os.makedirs(os.path.join(dirpath, category, createdyear))
    # SubCategory-Month
    if not os.path.exists(os.path.join(dirpath, category, createdyear, createdmonth)):
        os.makedirs(os.path.join(dirpath, category, createdyear, createdmonth))

    # Move File
    shutil.move(filename, des_dir)
