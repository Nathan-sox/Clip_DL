
# Standard Library
import os
import sys
from datetime import datetime

# Local
from history import add_to_history

from downloader import download_clip
from downloader import display_video_metadata
from downloader import get_video_formats
from downloader import download_audio
from downloader import download_video


def main():
    # History variables
    history_file = "history.json"

    download_link = input("URL Here: ")

    meta_data = display_video_metadata(download_link)

    print("\n1. Download Video")
    print("2. Download Audio")
    print("3. Download Clip")

    download, ydl_opts = get_format(download_link)

    success = False

    # Download the format
    try:
        download(download_link, ydl_opts)
        print("\nDone")
        success = True

    except Exception as e:
        print(f"\nError: {e}")

    # Only save successful downloads
    if success:
        title = meta_data.get("title")
        add_to_history(
            download_link,
            title,
            history_file
        )

        print("File saved successfully!")


def progress_hook(d):
    # checks if the status is downloading and updates the download bar
    if d['status'] == 'downloading':

        percent = d.get('_percent_str', '0%').strip()
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')

        # Simple progress bar implementation
        downloaded_bytes = d.get('downloaded_bytes', 0)
        total_bytes = d.get('total_bytes') or 1

        hash_fragment = downloaded_bytes / total_bytes

        bar_length = 20
        hash_amount = int(hash_fragment * bar_length)

        hashes = "#" * hash_amount
        spaces = "-" * (bar_length - hash_amount)

        sys.stdout.write(
            f"\rDownloading [{hashes}{spaces}] "
            f"{percent} | Speed: {speed} | ETA: {eta}"
        )

        sys.stdout.flush()

    # Prints done when done downloading the video/audio
    elif d['status'] == 'finished':
        print("\nDownload Completed")


def get_format(download_link):

    user_format_choice = input("\nChoice: ")

    # Downloads video if option 1 is picked
    if user_format_choice == "1":

        # Returns available qualities
        video_formats = get_video_formats(download_link)

        user_quality_choice = input("\nChoose a quality: ")

        selected_height = video_formats.get(user_quality_choice)

        if not selected_height:
            sys.exit("Invalid choice")

        ydl_opts = {
            'format': (
                f'bestvideo[height<={selected_height}]'
                f'+bestaudio/best'
            ),

            'merge_output_format': 'mp4',
        }

        # Sets the download path
        folder = os.path.join("downloads", "video")

        os.makedirs(folder, exist_ok=True)

        # Stores download function
        download = download_video

    # Downloads audio if option 2 is picked
    elif user_format_choice == "2":

        ydl_opts = {
            'format': 'bestaudio/best',

            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }],
        }

        # Sets folder path
        folder = os.path.join("downloads", "audio")

        os.makedirs(folder, exist_ok=True)

        # Stores download function
        download = download_audio

    # Downloads clip if option 3 is picked
    elif user_format_choice == "3":

        video_formats = get_video_formats(download_link)

        user_quality_choice = input("\nChoose a quality: ")

        selected_height = video_formats.get(user_quality_choice)

        if not selected_height:
            sys.exit("Invalid choice")

        # Sets clip start and end time
        start_time = input("\nStart time(HH:MM:SS): ")
        end_time = input("End time(HH:MM:SS): ")

        # Compare start_time and end_time
        start = datetime.strptime(start_time, "%H:%M:%S")
        end = datetime.strptime(end_time, "%H:%M:%S")

        if start >= end:
            sys.exit("Start time must be before end time")
        else:
            print("\nValid Clip range")

        ydl_opts = {
            'format': (
                f'bestvideo[height<={selected_height}]'
                f'+bestaudio/best'
            ),

            'merge_output_format': 'mp4',

            'postprocessor_args': ['-ss', start_time, '-to', end_time]
        }

        # Sets clips folder path
        folder = os.path.join("downloads", "clips")

        os.makedirs(folder, exist_ok=True)

        # Stores download function
        download = download_clip

    # Exits if invalid option
    else:
        sys.exit("Please choose one of the valid options.")

    # Adds shared configuration
    add_basic_configurations(ydl_opts, folder)

    # Returns the download function and options
    return download, ydl_opts


def add_basic_configurations(opts, folder):

    # Shared yt-dlp configuration
    opts["quiet"] = True
    opts["no_warnings"] = True
    opts["progress_hooks"] = [progress_hook]

    opts["outtmpl"] = os.path.join(
        folder,
        "%(title)s.%(ext)s"
    )


if __name__ == "__main__":
    main()
