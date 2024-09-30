import yt_dlp
import os

video_dir = './video_temp_dir'

def download_video(video_url: str ):

    os.makedirs(video_dir, exist_ok=True)
    video_path_template = os.path.join(video_dir,'%(title)s.%(ext)s')
  
    ydl_opt = {'outtmpl': video_path_template}

    with yt_dlp.YoutubeDL(ydl_opt) as ydl:
        info = ydl.extract_info(video_url, download=False)
        print(info)
        # video_path = os.path.join(video_dir, f"{info['title']}.{info['ext']}")
        
    # return video_path