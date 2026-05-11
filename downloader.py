import yt_dlp
from yt_dlp import YoutubeDL


def download_video(url, config):
    with YoutubeDL(config) as ydl:
        ydl.download([url])


def download_audio(url, config):
    with YoutubeDL(config) as ydl:
        ydl.download([url])


def download_clip(url, config):
    with YoutubeDL(config) as ydl:
        ydl.download([url])


no_warnings = True
quiet = True

test_opts = {
    "quiet": quiet,
    "no_warnings": no_warnings, }


def get_video_formats(url):
    with YoutubeDL(test_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    formats = info["formats"]

    available_qualities = set()

    for f in formats:
        height = f.get("height")

        if height and height >= 144:
            available_qualities.add(height)

    available_qualities = sorted(available_qualities)

    quality_map = {}

    print("\nAvailable qualities:")

    for no, quality in enumerate(available_qualities, start=1):
        print(f"{no}. {quality}p")

        quality_map[str(no)] = quality

    return quality_map


def display_video_metadata(url):

    with YoutubeDL(test_opts) as ydl:
        meta_data = ydl.extract_info(url, download=False)

    year = meta_data.get("upload_date")[:4]
    month = meta_data.get("upload_date")[4:6]
    day = meta_data.get("upload_date")[6:]

    meta_data["upload_date"] = f"{year}-{month}-{day}"

    print("\n=== VIDEO INFO ===\n")
    print(f"Title: {meta_data.get('title')}")
    print(f"Duration: {meta_data.get('duration')} seconds")
    print(f"Views: {meta_data.get('view_count'):,}")
    print(f"Uploader: {meta_data.get('uploader')}")
    print(f"Upload date: {meta_data.get('upload_date')}")
    # for f in formats:
    #     if f.get("ext") == "mp4":
    #         print(
    #             f.get("format_id"),
    #             f.get("ext"),
    #             f.get("resolution"),
    #         )
    return meta_data
