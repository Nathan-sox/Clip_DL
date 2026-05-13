# Clip_DL
#### Video Demo: <https://youtu.be/N_XggS_HnmI>

## Description
Clip_DL is a simple YouTube downloader with a CLI interface. It supports downloading videos, audio, and clips from YouTube links.

Note: You will need to download and install ffmpeg to utilize the trimming function and audio extraction/downloading function.
---

## Project Files
1. `reformatting.py`
2. `project.py`
3. `downloader.py`
4. `history.py`
5. `test_project.py`

---

## 1. reformatting.py
A utility script that formats headers in a text file. It checks if the first character of a line is `*`, and if so, adds `===` to each side using the `str.center()` method.

---

## 2. project.py
The main file. It handles the menu and processes user input, passing it into functions from other modules.

It first prompts the user for a YouTube link, then asks them to choose a download format:

- **Video** — prompts the user to choose from the available qualities for that video.
- **Audio** — downloads the audio directly in `.m4a` format. Quality selection was intentionally left out since audio was a secondary feature to the main clipping functionality.
- **Clip** — prompts the user to choose a quality, then a start and end time for the clip. The time range is validated before downloading.

> **Note:** The program does not retry on invalid input — it exits with an error message. This was a deliberate design choice to keep the scope manageable. A retry mechanism is planned for a future version.

---

## 3. downloader.py
The download module. It exposes simple functions that `project.py` calls to handle downloads. It also includes two helper functions:

- `get_video_formats` — fetches and displays the available video qualities for a given URL.
- `display_video_metadata` — fetches and displays metadata about the video.

Both functions display their relevant information as a side effect, which keeps the main file cleaner.

---

## 4. history.py
Tracks download history using a JSON file (`history.json`). Each entry stores:
- The video URL
- The video title
- The date and time of the download

---

## 5. test_project.py
Sadly the tests was written by AI, It tests two parts of the project:

- **History functions** — verifies that `save_history` and `load_history` work correctly, including edge cases like missing or empty files, and that `add_to_history` appends entries correctly.
- **`add_basic_configurations`** — verifies that the function correctly adds the required keys to the `ydl_opts` dictionary without overwriting existing ones.

These were chosen because they are the only functions that can be tested without network access or user input.

---

## Video:
https://youtu.be/N_XggS_HnmI In this video I explain how to use it. If you have any questions or misunderstandings about the code pls let me know in the comments of the video. Sorry for the background noise in advance.😅


*Thank you to Mr. Malan and the entire CS50P team for this amazing course.*🙇 
## And thank YOU for coming by :)
