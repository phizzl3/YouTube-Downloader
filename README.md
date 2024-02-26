# YouTube-Downloader

 Download YouTube videos using yt-dlp on MacOS

## Notes

This assumes you already have yt-dlp installed.
Use homebrew: "brew install yt-dlp"

* Gets the URL of the video
* Gets your desired output filename
* Downloads an .mp4 version of the file to the specified folder

The script generates a config.json file in the following location
~/PyAppFiles/YouTube Downloader/config.json
This file can be updated to change the default output directory if you
want to use something other than the default ~/Downloads folder.

## Build info

To build an executable using pyinstaller for MacOS

```bash
pyinstaller -F -n "YouTube Downloader" ./youtube_downloader/main.py 
```
