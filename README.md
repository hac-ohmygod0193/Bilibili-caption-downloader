# Bilibili Caption Downloader

This script downloads captions (subtitles) from Bilibili videos and saves them in text files. It extracts the video ID from a given Bilibili URL, fetches the video details, and downloads the subtitles.

## Features

- Extracts Bilibili video ID from a URL.
- Fetches video details using Bilibili API.
- Downloads subtitles and saves them in two formats:
  - Transcript format (plain text).
  - Subtitle format with timestamps.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/bilibili_caption_downloader.git
    cd bilibili_caption_downloader
    ```

2. Install the required Python packages:

    ```sh
    pip install requests
    ```

## Usage

1. Open the `bilibili_caption_downloader.py` file.
2. . Fill in your own **SESSDATA** value
Go to [Bilibili](https://www.bilibili.com/) and use F12 to inspect your website.
And click Application >> Cookie to find your SESSDATA as follow and paste it to the code.
![image](https://github.com/user-attachments/assets/92653779-baf2-447c-9978-15f7df9add6e)
3. Run the script:

    ```sh
    python bilibili_caption_downloader.py
    ```

4. The script will download the captions and save them in the current directory with the video title as the filename.



