"""
This assumes you already have yt-dlp installed. 
Use homebrew: "brew install yt-dlp"

Sample command:
yt-dlp --merge-output-format mp4 -o "/Volumes/T7_SSD/outputfile.py" "https://www.youtube.com/watch?v=PXMJ6F"
"""

import subprocess
from modules.settings import OUT_FOLDER


def get_url() -> str:
    print("\n Please paste the YouTube URL for the video below.")
    return input(": ")

def get_filename() -> str:
    print("\n Please enter the name for the output file below. (.mp4 will be added)")
    return input(": ")

def generate_file_output(filename: str) -> str:
    if not filename:
        filename = "YouTube Download"
    return f"{OUT_FOLDER}/{filename}.mp4"

def run_command(url: str, file_output: str) -> None:
    command: str = f'yt-dlp --merge-output-format mp4 -o "{file_output}" "{url}"'
    subprocess.run(command, shell=True, check=False)
    

