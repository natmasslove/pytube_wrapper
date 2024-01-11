import argparse

import lib.pytube_wrapper as pytube

parser = argparse.ArgumentParser(description="YouTube Video and Playlist Downloader")

# Arguments
parser.add_argument('action', type=str, choices=['download-video', 'download-playlist'], help='Action to perform (download-video or download-playlist)')
parser.add_argument('url', type=str, help='URL of the video or playlist')
parser.add_argument('dest_folder', type=str, help='Destination folder')
parser.add_argument('--force-overwrite', action='store_true', help='Overwrite existing video if it exists in destination folder')

# Parse arguments
args = parser.parse_args()
skip_video_if_exists = not(args.force_overwrite)

# Call the appropriate function based on the subcommand
if args.action == "download-video":
    pytube.download_video_from_url(
        args.url, args.dest_folder, skip_video_if_exists
    )
elif args.action == "download-playlist":
    pytube.download_playlist_from_url(
        args.url, args.dest_folder, skip_video_if_exists
    )
