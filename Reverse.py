from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress

playlist = Playlist(input('Enter URL: \n')).video_urls
count = 600
temm = 0
while count not in [0]:
    count = count - 1
    temm = 0
    for  video_link in playlist :
        temm = temm+1
        if temm == count:
            try:
                YouTube(video_link , on_progress_callback=on_progress).streams.filter(res="720p").first().download(output_path="./", filename_prefix=str(count) +" ")
                print(str(count) + " Completed " )

            except:
                print(str(count) + "---------unavailable---------" + str(YouTube(video_link).title))    
                
                
# filter(res="7200p").first()
# list = ["https://www.youtube.com/watch?v=x0OLat0fkzQ","https://www.youtube.com/watch?v=8l4ZjN4MXuQ","https://www.youtube.com/watch?v=C12WRs6LiQs","https://www.youtube.com/watch?v=rt6sHVfzjWM","https://www.youtube.com/watch?v=9Q6gFxqt9SU", "https://www.youtube.com/watch?v=SbSTTfnEMZM&t=899s" , "https://www.youtube.com/watch?v=B7cxLO1qKSw","https://www.youtube.com/watch?v=C2_L0wpY0iQ", "https://www.youtube.com/watch?v=OEP-Q3wVIpI" ]
# count = 0
# for i in list:
#     count= count+1
#     sm = YouTube(i , on_progress_callback=on_progress).streams.filter(res="720p").first().download(output_path="D:\Movie/30th oct", filename_prefix=str(count) +" " )
#     print(count)
