#Handling imports and such =============================================

import os
try:
    from pytube import YouTube as yt
    from pytube import Playlist as pl
    from art import *
except ModuleNotFoundError:
    if input("Install missing dependencies?(Y/n)>>")=="n":
        pass
    else:
        try:
            os.system('pip install pytube')
            os.system('pip install art')
        except:
            print('Import Error: pip not installed')

#Title =================================================================
tprint("YTDownloader")

#Install type/location =================================================
VoM = input("Select Music(default, mp3) or Video(mp4)\n(3,4)>> ")
print("\n")

inp = input("Select download directory\n(D, M, specify(from user dir))>> ")
print("\n")
if inp.upper() == "D":
    path = "Downloads"
elif inp.upper() == "M":
    path = "Music"
else:
    path = inp

#Final download path ===================================================
fullpath = os.path.join(os.getenv('USERPROFILE'), path)
print("Saving to:", fullpath+"\n")

#Downloading loop (with parameters) ====================================

print("Links:")
if VoM == '4': #Only do video if input =4 as default is mp3
    while True: #Loop until error or user just typing newline to exit(should have a whole lot of errors... hopefully, so true until nl to exit)
        link = input(">> ")

        try:
            yt(link).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(fullpath)
        except:
            print("bye bye...\n-Daselsdis")
            break
else:
    while True:
        link = input(">> ")

        try:
            yt(link).streams.filter(only_audio=True).first().download(fullpath)
        except:
            print("bye bye...\n-Daselsdis")
            break