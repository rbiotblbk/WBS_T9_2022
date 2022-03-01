from ftplib import FTP 
import os 
from pathlib import Path 
import json 

os.chdir(Path(__file__).parent)

# Read Config
with open("./ftp.json", mode= "r") as file:
    content = file.read()
    json_dict = json.loads(content)


# Connection Data
FTP_SERVER = json_dict["ftp_server"]
FTP_USER = json_dict["ftp_user"]
FTP_PASS = json_dict["ftp_pass"]

FTP_DIR_NAME = json_dict["ftp_dirname"]

# FTP Credentials
ftp = FTP(FTP_SERVER)
ftp.login(FTP_USER, FTP_PASS)


# Folder Navigation
FTP_DIR_NAME = "Mohamed"
ftp.cwd(FTP_DIR_NAME)


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