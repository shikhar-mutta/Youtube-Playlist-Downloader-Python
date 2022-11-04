from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress


playlist = Playlist(input('Enter URL: \n')).video_urls
count = 0
for video_link in playlist:
    count=count+1
    if count > 0: 
        try:
            YouTube(video_link , on_progress_callback=on_progress).streams.filter(res="720p").first().download(output_path="./", filename_prefix=str(count) +" ")
            print(str(count)+" Completed ")

        except:
            print(str(count) + " unavailable"+ YouTube(video_link).get_highest_resolution())

