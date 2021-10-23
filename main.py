from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress



playlist = Playlist("https://www.youtube.com/playlist?list=PLir19lgiavA0B5111KZP-R2PYM_8jF8By").video_urls
count =0
for video_link in playlist:
    count=count+1
    if count >= 5 :
        try:
            YouTube(video_link , on_progress_callback=on_progress).streams.filter(res="720p").first().download("DBMS\Pathak Sir")
            print(str(count)+" Completed    ")

        except:
            print(video_link + " unavailable")