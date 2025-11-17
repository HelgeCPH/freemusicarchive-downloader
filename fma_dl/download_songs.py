import requests
import shutil
from pathlib import Path


def download_song(url, local_file):
    if not local_file.exists():
        with requests.get(url, stream=True) as response:
            with local_file.open("wb") as fp:
                shutil.copyfileobj(response.raw, fp)

    return local_file


def download_songs(metadata, destination_dir, silent=False):
    for song_metadata in metadata:
        target_file = Path(destination_dir, song_metadata["fileName"])
        url = song_metadata["fileUrl"]
        if not silent:
            print(f"Downloading {url} to {target_file}...")

        download_song(url, target_file)
