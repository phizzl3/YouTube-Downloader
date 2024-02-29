"""
This assumes you already have yt-dlp installed. 
Use homebrew: "brew install yt-dlp"
* Gets the URL of the video
* Gets your desired output filename
* Downloads a .mp4 version of the file to the specified folder
"""

import subprocess
from modules.settings import OUT_FOLDER
from modules import display

__version__ = "1.0.0"


def get_url() -> str:
    print("\n Please paste the YouTube URL for the video below.")
    return input(" URL: ")


def get_filename() -> str:
    print("\n Please enter the name for the output file below. (.mp4 will be added)")
    return input(" Name: ")


def generate_file_output(filename: str) -> str:
    if not filename:
        filename = "YouTube Download"
    return f"{OUT_FOLDER}/{filename}.mp4"


def run_command(url: str, file_output: str) -> None:
    command: str = f'yt-dlp --merge-output-format mp4 -o "{file_output}" "{url}"'
    print()  # Just to add some space
    subprocess.run(command, shell=True, check=False)


if __name__ == "__main__":
    while True:
        display.ascii_art(__version__)
        video_url = get_url()
        filename = get_filename()
        output = generate_file_output(filename)
        run_command(url=video_url, file_output=output)
        display.output_message(file_location=output)
        