from ftplib import FTP 
import os 
from pathlib import Path 

os.chdir(Path(__file__).parent)

# Connection Data
FTP_SERVER = "ngcobalt414.manitu.net"
FTP_USER = "XXXXX"
FTP_PASS = "XXXX"

dir_name = "Mohamed"

# FTP Credentials
ftp = FTP(FTP_SERVER)
ftp.login(FTP_USER, FTP_PASS)


# Folder Navigation
dir_name = "Mohamed"
ftp.cwd(dir_name)


def upload_file():
    file_to_upload = "file_upload.txt" 
    ftp.storbinary("STOR " + file_to_upload, open(file_to_upload, 'rb'))
    print("Uploaded Successfully!")


def download_file():
    # List the files and folder 
    files = ftp.nlst()  
    print(files)

    for file in files:
        print(file)

          #check if file is a file'
        root, ext = os.path.splitext(file)
        if ext:
            print("Downloading:", file)
            local_file = open(root + "_download" + ext, "wb")

            ftp.retrbinary("RETR " + file, local_file.write)
            local_file.close()
      
    
    print("Downloaded Succesfully")


if __name__ == "__main__":
    
    # upload_file()
    download_file()