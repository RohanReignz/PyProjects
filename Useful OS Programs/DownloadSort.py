# a program that automatically sorts out downloaded files into folder based on filetype

import os
from datetime import datetime
from time import sleep
while True:
    DOWNLOAD_DIRECTORY = 'path/to/download/directory' # example: 'E:/Downloads/', remember to put / in the end
    while datetime.minute() != 30:
        sleep(300)
        if datetime.minute() == 30:
            break
    os.chdir(DOWNLOAD_DIRECTORY)
    names = os.listdir()
    paths = []
    for name in names:
        path = DOWNLOAD_DIRECTORY + name
        paths.append(path)
    file_extensions = []
    for p in paths:
        filename, file_ext = os.path.splitext(p)
        file_extensions.append(file_ext)
    # make folders based on extensions
    ord_ext = list(dict.fromkeys(file_extensions))
    ord_ext_splitted = [x.strip('.') for x in ord_ext]
    for foldername in ord_ext_splitted:
        if os.path.exists(DOWNLOAD_DIRECTORY+foldername.capitalize()+' Files'):
            continue
        else:
            os.mkdir(foldername.capitalize()+' Files')
    if os.path.exists(DOWNLOAD_DIRECTORY+' Files'):
        os.rmdir(DOWNLOAD_DIRECTORY+' Files')
    sleep(2)
    for p in paths:
        if '.' in p:
            try:
                filename, file_extension = os.path.splitext(p)
                file_extension_splitted = file_extension.strip('.')
                os.rename(p, DOWNLOAD_DIRECTORY+file_extension_splitted.capitalize()+' Files/'+ os.path.basename(p))
            except Exception:
                continue
        else:
            continue

    print("Done!")
    continue
