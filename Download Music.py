# Download Music from You Tube By Link

# You have to write in you terminal computer: pip install pytube
# You have to write in you terminal computer: pip install moviepy

#Create by Randy Barrantes
from pickle import TRUE
from pytube import YouTube
import moviepy.editor as mp
import re
import os

# Functions
def ask_the_user_for_condition(Message):
    """Function to ask the user if he wants to repeat the action
    enter more data"""
    Validate = True
    Result = True    
    while Validate:
        Letra = input(Message)
        if Letra == "Y" or Letra == "y":
            Validate = False
            Result = True
        elif Letra == "N" or Letra == "n":
            Validate = False
            Result = False
        else:
            print("ERROR: Inserted Letter is Invalid. You must type (Y/N): ")
            Validate = True
    return Result

Repeat= True
while Repeat:
    # insert the video link that you want save.
    Link=input("Copy the video link: ")
    path=input("Copy the direction explorer, where you want save the music?: ")
    yt=YouTube(Link)
    print("")

    #Download
    print("Donwload...")
    ys= yt.streams.filter(only_audio=True).first().download(path)
    print("Donwload completed...")
    print("")

    #Transform MP4 to MP3
    print("Trasnform file...")
    for file in os.listdir(path):
        if re.search('mp4', file):
            mp4_path=os.path.join(path, file)
            mp3_path=os.path.join(path, os.path.splitext(file)[0]+'.mp3')
            new_file=mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp3_path)
    print("Done!")
    input("")
    Repeat=ask_the_user_for_condition("Do you want repeat the acction?, Press (Y/N)")
print("")
print("Thanks")
print("")
input("Press ENTER for exit")
