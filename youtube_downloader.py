"""
Youtube downloader with pytube
TODO:
    - Check file existing (avoid overwrite)
    - Delete MP4 file
    - MP4 Downloader function
    - Playlist downloader function
"""

from pytube import YouTube
from moviepy.editor import *


def mp4_2_mp3(mp4, mp3):
    file_to_convert = AudioFileClip(mp4)
    file_to_convert.write_audiofile(mp3)
    file_to_convert.close()


def yt_downloader_audio(url: str):
    yt_video = YouTube(url)
    print(f'Downloading {yt_video.title}.')
    download = yt_video.streams.get_highest_resolution()
    file = download.download()
    mp4_2_mp3(file, file[:-4]+'.mp3')


if __name__ == '__main__':
    yt_downloader_audio('https://www.youtube.com/watch?v=D9G1VOjN_84&list=PLe7U0LAI1OjSgYBm8_L2RvMDEt1vNtXC4')
