from pytubefix import YouTube
from pytubefix.cli import on_progress


url1 = "https://youtu.be/motX94ztOzo?si=3TQ28uCzzn9-Q9Q-"
url2 = "https://www.youtube.com/watch?v=motX94ztOzo&si=3TQ28uC"

yt = YouTube(url1, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_highest_resolution()