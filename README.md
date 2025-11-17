# Free Music Archive Downloader (`fma-dl`)

This is a command-line tool for downloading music from the [Free Music Archive (FMA)](https://freemusicarchive.org).
The script allows you to download songs and store respective metadata.
Download URLs and metadata are extracted from FMAs websites.

This program can be used to download songs, e.g., from FMAs charts or genres.

This is a fork and refactored version from [`yallowraven`'s freemusicarchive-downloader](https://github.com/yallowraven/freemusicarchive-downloader)


## Requirements

- Python > 3.11 (above 3.7 should work but I did not test)
- [Poetry](https://python-poetry.org/) for development


## Installation

### Running `fma-dl` with [`pipx`](https://pipx.pypa.io)

1. [Install `pipx`](https://pipx.pypa.io/stable/installation/)
2. `pipx install git+https://github.com/HelgeCPH/freemusicarchive-downloader`
3. Run `fma-dl` as described below under usage.

### From PyPI

TBD

### For development

1. Clone this repository.
2. Install the required dependencies and this tool: `poetry install`
3. Use this tool in its virtual environment: `poetry shell`, see usage below.


## Usage

```bash
fma-dl [-h] [--meta | --no-meta] [--silent | --no-silent] [--limit LIMIT] url output_dir

positional arguments:
  url                   URL of the webpage to download music from
  output_dir            Output directory for downloaded songs

options:
  -h, --help            show this help message and exit
  --meta, --no-meta     Store metadata scraped from FMA
  --silent, --no-silent
                        Do not log each downloaded song
  --limit LIMIT         Maximum number of songs to download (default: 10)
```


## Examples

- Download the 15 highest ranked songs from the all time charts to `/tmp/music`:
  ```
  fma-dl https://freemusicarchive.org/music/charts/all /tmp/music --limit 15 --silent --no-meta
  ```
- Download the 142 most recent songs from the genre "Blues" to `/tmp/music`:
  ```
  fma-dl https://freemusicarchive.org/genre/Blues <output_dir> --meta
  ```
