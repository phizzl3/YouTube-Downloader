"""
Load (use defaults first if not found) json data from
file, and use that data to generate a config file for import.
"""

from pathlib import Path
from modules.loadjsondata import loadjson


# json file location
_CONFIG: Path = Path().home() / "PyAppFiles" / "YouTube Downloader" / "config.json"

# Default values for config json data
_DEFAULTS: dict[str, any] = {
    "Comments": [
        "Enter the full path to the folder where you",
        "want to store your downloaded files.",
        "If you want the files to go to your downloads folder,",
        "Enter the word: 'Downloads'.",
    ],
    "Output Folder": "Downloads",
}

# Load (or set defaults) settings json data
data: dict[str, any] = loadjson(_CONFIG, default_data=_DEFAULTS)

# Set output folder
if data["Output Folder"].title() == "Downloads":
    OUT_FOLDER: str = str(Path().home() / "Downloads")
else:
    OUT_FOLDER: str = data["Output Folder"]
