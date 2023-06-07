# Big important stuff:
# Youtube playlists and mixes are a different thing, you cannot directly download mixes from just the link.
# As an example, a playlist's link's Id is in my experience 34 chars long, and can take the form: 
# "https://www.youtube.com/playlist?list="+Id. Mixes on the other hand have shorter playlist's link's Id, in my experience 13
# chars long, and can take the form: "https://www.youtube.com/watch?v=VIDEOID&list=MIXID".
# You can only download playlist, and I suspect only Public or Occult ones from your channel or whoever's if they are
# accessible from the outside via link.

# MORE EVEN MORE IMPORTANT STUFF:
# How to solve this: I found this answer on reddit and I will credit it at the end, the trick is to load the mix, and next, 
# add to queue a random video. Now you don't have a mix, you have a queue of videos, now you can make a playlist out of this.
# Make sure to make it Public or Occult, now that playlist's link should follow what's said above and you are good to go :D.
# Credit where credits due: https://www.reddit.com/r/youtube/comments/b33ecs/comment/hj74ays/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
# Moreover, all the resources and pytube libraries have been an amazing tool and for any doubt feel free to ask me the author
# or check those docs.
# Have an amazing time, your truly: Daselsdis
# Also, feel free to tinker with this stuff, it has MIT license, free code :D (I wouldn't have made it this far without it).


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
tprint("YTDPlaylists")

#Install type/location =================================================
VoM = input("Select Music(default, mp3) or Video(mp4)\n(3,4)>> ")
print("\n")

inp = input("Select download directory\n(D, M, specify(from user dir))>> ")
print("\n")
if inp == "D":
    path = "Downloads"
elif inp == "M":
    path = "Music"
else:
    path = inp

#Downloading loop (with parameters) ====================================

print("Playlists links:")
if VoM == 4: #Only do video if input =4 as default is mp3
    while True: #Loop until error or user just typing newline to exit(should have a whole lot of errors... hopefully, so: True until nl to exit)
        playl = pl(input(">> "))
        try:
            i=0
            l=str(len(playl.video_urls))
            for url in playl.video_urls:
                vid = yt(url)
                i+=1
                print("("+str(i)+"/"+l+")-"+"Downloading: "+vid.title+".")
                vid.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(os.path.join(os.getenv('USERPROFILE'), path+"\\"+playl.title))
        except:
            print("bye bye...\n-Daselsdis")
            break
else:
    while True:
        playl = pl(input(">> "))
        try:
            i=0
            l=str(len(playl.video_urls))
            for url in playl.video_urls:
                vid = yt(url)
                i+=1
                print("("+str(i)+"/"+l+")-"+"Downloading: "+vid.title+".")
                vid.streams.filter(only_audio=True).first().download(os.path.join(os.getenv('USERPROFILE'), path+"\\"+playl.title))
        except:
            print("bye bye...\n-Daselsdis")
            break


