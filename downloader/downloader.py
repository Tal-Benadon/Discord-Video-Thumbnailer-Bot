import yt_dlp
import os

video_dir = './video_temp_dir'

def turncate_title(title):
    return title[0:10]    

def handle_wrong_facebook_title(title):
    return

def download_video(video_url: str ):

    os.makedirs(video_dir, exist_ok=True)
    video_path_template = os.path.join(video_dir,'%(title)s.%(ext)s')
  
    ydl_opt = {'outtmpl': video_path_template}

    with yt_dlp.YoutubeDL(ydl_opt) as ydl:
        info = ydl.extract_info(video_url, download=False)
        if not info.get('type') is None or info.get('type') != "playlist":
            
            ydl.download([video_url])
            print(f"info {info}")
            initial_title = info.get('title','unkown_title')
            video_ext = info.get('ext', 'mp4')
            
            original_video_path = os.path.join(video_dir, f"{initial_title}.{video_ext}")
            video_title = turncate_title(initial_title)
            new_video_path = os.path.join(video_dir, f'{video_title}.{video_ext}')
            if os.path.exists(original_video_path):
                os.rename(original_video_path, new_video_path)
            # video_path = os.path.join(video_dir, f'{video_title}.{video_ext}')
            return new_video_path
   