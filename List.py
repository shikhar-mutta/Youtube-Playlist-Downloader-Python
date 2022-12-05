from pytube import YouTube
from pytube.cli import on_progress

list = input("Input Saparated by comma List of Videos: \n").split(',')
count = 0
for video_link in list:
    count=count+1
    if count > 0:
        try:
            YouTube(video_link , on_progress_callback=on_progress).streams.filter(res="720p").first().download(output_path="./", filename_prefix=str(count) +" ")
            print(str(count)+" Completed ")

        except:
             print(str(count) + "---------unavailable---------" + str(YouTube(video_link).title))
