"""
Youtube downloader with pytube
"""

from pytube import YouTube
from pytube.contrib.playlist import Playlist
from moviepy.editor import *
from os import remove


def mp4_2_mp3(mp4, mp3):
    """
    Converts a mp4 file into a mp3 file
    :param mp4: MP4 filepath
    :param mp3: MP3 filepath
    :return: full mp3 filepath
    """
    file_to_convert = AudioFileClip(mp4)
    file_to_convert.write_audiofile(mp3)
    file_to_convert.close()
    return mp3


def yt_downloader_audio(url: str, verbose=True):
    """
    Downloads a video from YouTube and converts it to audio (mp3 format)
    It will overwrite any files with the same names
    :param url: Link to the YouTube video to download
    :param verbose: bool. manages print statements, default true
    :return: filepath to the mp3 file
    """
    yt_video = YouTube(url)
    if verbose:
        print(f'Downloading: {yt_video.title}.')
    download = yt_video.streams.get_highest_resolution()
    file = download.download()
    file_audio = mp4_2_mp3(file, file[:-4]+'.mp3')
    remove(file)
    return file_audio


def yt_downloader_video(url: str, verbose=True):
    """
    Downloads a video from YouTube with the highest resolution
    It will overwrite any files with the same names
    :param url:
    :param verbose: bool. manages print statements, default true
    :return: filepath
    """
    yt_video = YouTube(url)
    if verbose:
        print(f'Downloading: {yt_video.title}.')
    download = yt_video.streams.get_highest_resolution()
    file = download.download()
    return file


def yt_playlist_downloader_audio(url: str):
    """
    Gets the videos from the playlist, downloads them and turns them to audio, removing the video file.
    Requires the playlist to be public, otherwise the video urls are None
    :param url:
    :return: None
    """
    playlist = Playlist(url)
    print(f'Getting {playlist.length} videos from the playlist: {playlist.title}.')
    for video_url in playlist.video_urls:
        yt_downloader_audio(video_url, verbose=False)
    return None


def yt_playlist_downloader_video(url: str):
    """
    Gets the videos from the playlist and downloads them.
    Requires the playlist to be public, otherwise the video urls are None
    :param url:
    :return: None
    """
    playlist = Playlist(url)
    print(f'Getting {playlist.length} videos from the playlist: {playlist.title}.')
    for video_url in playlist.video_urls:
        file = yt_downloader_video(video_url, verbose=False)
        print(f'File {file} downloaded')
    return None


if __name__ == '__main__':
    # print(yt_downloader_audio('https://www.youtube.com/watch?v=D9G1VOjN_84'))  # Enemy
    # print(yt_downloader_video('https://www.youtube.com/watch?v=CAb_bCtKuXg'))  # Life is fun
    yt_playlist_downloader_audio('https://www.youtube.com/playlist?list=PLe7U0LAI1OjSgYBm8_L2RvMDEt1vNtXC4')
    # yt_playlist_downloader_video('https://www.youtube.com/playlist?list=PLhO47R5IHH3As4gVKHXC8tJvDCj3TZzoy')
