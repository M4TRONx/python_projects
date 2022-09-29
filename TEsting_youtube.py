
from pytube import YouTube
import os
from pathlib import Path

a = int(input("Select \n1/ VIDEO DOWNLOAD \n2/ VIDEO TO AUDIO DOWNLOAD \nSELECT : "))

if a==1:

    link = input("Enter Video Link : ")

    save_path = str(os.path.join(Path.home(), "Downloads"))

    try:
        url= YouTube(link)
        video= url.streams.get_highest_resolution()
        print("Video Downloading-----")
        video.download(save_path)
        print("Video Download Successfully !!! ")

    except:

        print("Something Went Wrong !!! ")

elif a==2:

    link = input("Enter Video Link To Convert Audio : ")

    save_path = r"E:\All Youtube Audios"

    try:
        url= YouTube(link)
        video= url.streams.get_audio_only()
        print("Audio Downloading-----")
        video.download(save_path)
        print("Audio Download Successfully !!! ")

    except:

        print("Something Went Wrong !!! ")

else:
    print("Wrong Type\nPLease Again Enter ")


print("\n\n\n\n\nTHANK YOU <3\nMADE BY M4TRONx")