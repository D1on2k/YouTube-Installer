from yt_dlp import YoutubeDL
import json
import yt_dlp
import time
import string

print("-----------------------------------------------------")
print("-                                                   -")
print("-                 DionYTInstaller                   -")
print("-                                                   -")
print("-----------------------------------------------------")

time.sleep (2)

print("\nPress 1 for installing MP3")
print("Press 2 for installing MP4")
print("Press 3 for installing FLAC")

setup = input("\nEnter What you want to install: ")

if setup == "1":
    EnterURL = input("Enter your URL for MP3: ")

    while (len(EnterURL.strip()) == 0):
        EnterURL = input("You typed nothing try again here: ")

    while True:
        try:
            BitRate = int(input("Enter your desired bitrate: "))
            if BitRate <= 320:
                break
            else:
                print("\nYou can't put more than 320 kbps try again.")
        except ValueError:
            print("\nPlease enter a numbers not letters.")
    
    ydl_opts = {"format": "bestaudio/best","postprocessors": 
        [{"key": "FFmpegExtractAudio","preferredcodec": 
          "mp3","preferredquality": BitRate,}],}

    with YoutubeDL(ydl_opts) as ydl: 
        try:
            print(f"Downloading: {EnterURL}")
            ydl.download([EnterURL])
            print("Music was downloaded successfully!")

        except Exception as ex:
            print("Error dowloading the music, maybe check if the URL is valid or correct.")
            print(str(ex))

elif setup == "2":
    EnterURL2 = input("Enter your URL for MP4: ")
    
    while (len(EnterURL2.strip()) == 0):
        EnterURL2 = input("You typed nothing try again here: ")

    ydl_opts = {"format": "bestvideo[ext=mp4]+bestaudio[ext=mp4]/mp4+best[height<=480]",
                "outtmpl": "%(title)s.%(ext)s",
                "quiet": False,}
    
    with YoutubeDL(ydl_opts) as ydl: 
        try:
            print(f"Downloading: {EnterURL2}")
            ydl.download([EnterURL2])
            print("Video was downloaded successfully!")
        
        except Exception as ex:
            print("Error dowloading the video, maybe check if the URL is valid or correct.")
            print(str(ex))

elif setup == "3":
    EnterURL3 = input("Enter your URL for FLAC: ")
    
    while (len(EnterURL3.strip()) == 0):
        EnterURL3 = input("You typed nothing try again here: ")
    
    ydl_opts = {"format": "bestaudio/best","postprocessors": 
        [{"key": "FFmpegExtractAudio","preferredcodec": "flac"}],}
    
    with YoutubeDL(ydl_opts) as ydl: 
        try:
            print(f"Downloading: {EnterURL3}")
            ydl.download([EnterURL3])
            print("Music was downloaded successfully!")

        except Exception as ex:
            print("Error dowloading the music, maybe check if the URL is valid or correct.")
            print(str(ex))

print("\nExiting. Thanks for using my YouTube downloader!!!")