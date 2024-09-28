import yt_dlp
import os

video_dir = './video_temp_dir'

def download_video(video_url: str ): # // if video_dir not provided, create a dir within bot directory for the temp videos

    os.makedirs(video_dir, exist_ok=True)
    video_path = os.path.join(video_dir,'%(title)s.%(ext)s')
  
    ydl_opt = {'outtmpl': video_path}

    with yt_dlp.YoutubeDL(ydl_opt) as ydl:
        ydl.download([video_url])
        
    return video_path