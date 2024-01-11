# Pytube Wrapper

This is a simple library which let's you download either individual youtube videos or entire playlists.

It uses python pytube library.

Installing required libraries:
```shell
pip install -r requirements.txt
```

Usage:
```
python runner.py [-h] [--force-overwrite] {download-video,download-playlist} url dest_folder

positional arguments:
  {download-video,download-playlist}
                        Action to perform (download-video or download-playlist)
  url                   URL of the video or playlist
  dest_folder           Destination folder

optional arguments:
  -h, --help            show this help message and exit
  --force-overwrite     Overwrite existing video if it exists in destination folder
```
