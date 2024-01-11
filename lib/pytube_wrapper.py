from pytube import YouTube, Channel, Playlist
from slugify import slugify
import os

def download_video(video: YouTube, dest_folder: str, skip_video_if_exists: bool = True):
    """
    Downloads a YouTube video to the specified destination folder

    :param video: YouTube video object
    :param dest_folder: destination folder to download the video to
    :param skip_video_if_exists: if True, skips the video if it already exists in the destination folder
    :return: None    
    """
    try: 
        ch = Channel(video.channel_url)

        title = slugify(video.title)
        channel_name = slugify(ch.channel_name)
        publish_date = video.publish_date.strftime('%Y%m%d')

        filename = f"{channel_name}-{title}-{publish_date}.mp4"
        full_path = os.path.join(dest_folder, filename)

        if os.path.exists(full_path) and skip_video_if_exists:
            print(f"Skipping.. Video {title} already exists in {dest_folder}")
        else:
            print(f"Downloading {title}...")
            strm = video.streams.get_highest_resolution()
            strm.download(filename=full_path)
            print(f"Stream Info: {strm}")
            print(f"Video {title} downloaded successfully")
    except Exception as ex:
        print(f"Error downloading {video.title}: {str(ex)}")
        if os.path.exists(full_path):
            os.remove()


def download_video_from_url(video_url: str, dest_folder: str, skip_video_if_exists: bool):
    """
    Downloads a YouTube video from the specified URL to the specified destination folder

    :param video_url: URL of the YouTube video
    :param dest_folder: destination folder to download the video to
    :param skip_video_if_exists: if True, skips the video if it already exists in the destination folder
    :return: None
    """
    video = YouTube(video_url)
    download_video(video=video, dest_folder=dest_folder, skip_video_if_exists=skip_video_if_exists)

def download_playlist(playlist: Playlist, dest_folder: str, skip_video_if_exists: bool = True):
    """
    Downloads all the videos in a YouTube playlist to the specified destination folder

    :param playlist: YouTube playlist object
    :param dest_folder: destination folder to download the videos to
    :param skip_video_if_exists: if True, skips the video if it already exists in the destination folder
    :return: None    
    """
    for video in playlist.videos:
        download_video(video=video, dest_folder=dest_folder, skip_video_if_exists=skip_video_if_exists)

def download_playlist_from_url(playlist_url: str, dest_folder: str, skip_video_if_exists: bool = True):
    """
    Downloads all the videos in a YouTube playlist from the specified URL to the specified destination folder

    :param playlist_url: URL of the YouTube playlist
    :param dest_folder: destination folder to download the videos to
    :param skip_video_if_exists: if True, skips the video if it already exists in the destination folder
    :return: None
    """
    playlist = Playlist(playlist_url)
    download_playlist(playlist=playlist, dest_folder=dest_folder, skip_video_if_exists=skip_video_if_exists)