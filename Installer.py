"""
MIT License

Copyright (c) 2026 Dion2k

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from yt_dlp import YoutubeDL
import time
import os

print(" _______  __                   ______                     __              __ __                    ")
print("|       \|  \                 |      \                   |  \            |  \  \                   ")              
print("| ▓▓▓▓▓▓▓\\▓▓ ______  _______  \▓▓▓▓▓▓_______   _______ _| ▓▓_    ______ | ▓▓ ▓▓ ______   ______   ")
print("| ▓▓  | ▓▓  \/      \|       \  | ▓▓ |       \ /       \   ▓▓ \  |      \| ▓▓ ▓▓/      \ /      \  ")
print("| ▓▓  | ▓▓ ▓▓  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\ | ▓▓ | ▓▓▓▓▓▓▓\  ▓▓▓▓▓▓▓\▓▓▓▓▓▓   \▓▓▓▓▓▓\ ▓▓ ▓▓  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ")
print("| ▓▓  | ▓▓ ▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓ | ▓▓ | ▓▓  | ▓▓\▓▓    \  | ▓▓ __ /      ▓▓ ▓▓ ▓▓ ▓▓    ▓▓ ▓▓   \▓▓ ")
print("| ▓▓__/ ▓▓ ▓▓ ▓▓__/ ▓▓ ▓▓  | ▓▓_| ▓▓_| ▓▓  | ▓▓_\▓▓▓▓▓▓\ | ▓▓|  \  ▓▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓▓▓▓ ▓▓       ")
print("| ▓▓    ▓▓ ▓▓\▓▓    ▓▓ ▓▓  | ▓▓   ▓▓ \ ▓▓  | ▓▓       ▓▓  \▓▓  ▓▓\▓▓    ▓▓ ▓▓ ▓▓\▓▓     \ ▓▓       ")
print("\ ▓▓▓▓▓▓▓ \▓▓ \▓▓▓▓▓▓ \▓▓   \▓▓\▓▓▓▓▓▓\▓▓   \▓▓\▓▓▓▓▓▓▓    \▓▓▓▓  \▓▓▓▓▓▓▓\▓▓\▓▓ \▓▓▓▓▓▓▓\▓▓       ")
print("\nMade by D1on2k")

time.sleep(2)

print("\nPress 1 for installing MP3")
print("Press 2 for installing MP4")
print("Press 3 for installing FLAC")
print("Press 4 for installing WAV")

setup = input("\nEnter What you want to install: ")

if setup == "1":
    EnterURL = input("Enter your URL for MP3: ")
    
    setpath = input("Enter a path or save to folder: ")
    if setpath:
        os.makedirs(setpath, exist_ok=True)
    
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
    
    setpath = input("Enter a path or save to folder: ")
    if setpath:
        os.makedirs(setpath, exist_ok=True)

    while (len(EnterURL2.strip()) == 0):
        EnterURL2 = input("You typed nothing try again here: ")

    while True:
        try:
            width = int(input("Enter your desired width e.g 1920: "))
            height = int(input("Enter your desired height e.g 1080: "))
            break

        except ValueError:
            print("\nPlease enter a numbers not letters.")

    ydl_opts = {"format": f"bestvideo[width<={width}][height<={height}]+bestaudio/best[width<={width}][height<={height}]",
                "outtmpl": "%(title)s.%(ext)s",
                "quiet": False,
                "merge_output_format": "mp4",}
    
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
    
    setpath = input("Enter a path or save to folder: ")
    if setpath:
        os.makedirs(setpath, exist_ok=True)

    while (len(EnterURL3.strip()) == 0):
        EnterURL3 = input("You typed nothing try again here: ")
    
    ydl_opts = {"format": "bestaudio/best","postprocessors": 
              [{"key": "FFmpegExtractAudio","preferredcodec": 
                "flac"}],}
    
    with YoutubeDL(ydl_opts) as ydl: 
        try:
            print(f"Downloading: {EnterURL3}")
            ydl.download([EnterURL3])
            print("Music was downloaded successfully!")

        except Exception as ex:
            print("Error dowloading the music, maybe check if the URL is valid or correct.")
            print(str(ex))

elif setup == "4":
    EnterURL4 = input("Enter your URL for WAV: ")

    while (len(EnterURL4.strip()) == 0):
        EnterURL4 = input("You typed nothing try again here: ")
    
    ydl_opts = {"format": "bestaudio/best", "postprocessors":
               [{"key": "FFmpegExtractAudio", "preferredcodec":
                 "wav"}],}
    
    with YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"Downloading: {EnterURL4}")
            ydl.download([EnterURL4])
            print("Music was downloaded successfully!")

        except Exception as ex:
            print("Error downloading the music, maybe check if the URL is valid or correct.")
            print(str(ex))

print("\nExiting. Thanks for using my YouTube downloader!!!")
