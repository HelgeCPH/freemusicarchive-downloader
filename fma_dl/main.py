import argparse
from fma_dl.download_songs import download_songs
from fma_dl.scraper import scrape_song_metadata_from_pages
from fma_dl.url_validation import UrlValidationResult, get_error_message, validate_url
from sys import exit
from pathlib import Path


def main(url, output_dir, meta=True, silent=False, limit=1000):
    if not Path(output_dir).is_dir():
        print(f"{output_dir} does not exist!")
        exit()

    url_validation_result = validate_url(url)
    if url_validation_result != UrlValidationResult.VALID:
        print(get_error_message(url_validation_result))
        exit()

    if not silent:
        print("Scraping song metadata from FMA...")
    metadata = scrape_song_metadata_from_pages(url, limit=limit)

    if not silent:
        print("Downloading songs...")
    download_songs(metadata, output_dir, silent=silent)

    if meta:
        if not silent:
            print("Storing metadata...")
        store_metadata(metadata, Path(output_dir, "metadata.json"))

    if not silent:
        print(f"Done! Downloaded {len(metadata)} songs to {output_dir}")


def store_metadata(metadata, out_file):
    import json

    with out_file.open("w") as fp:
        json.dump(metadata, fp, indent=2)


def cmd_main():
    descr = """Download music from the Free Music Archive (FMA)
https://freemusicarchive.org/"""
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument(
        "url", type=str, help="URL of the webpage to download music from"
    )
    parser.add_argument(
        "output_dir", type=str, help="Output directory for downloaded songs"
    )
    parser.add_argument(
        "--meta",
        default=True,
        action=argparse.BooleanOptionalAction,
        help="Store metadata scraped from FMA",
    )
    parser.add_argument(
        "--silent",
        default=False,
        action=argparse.BooleanOptionalAction,
        help="Do not log each downloaded song",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Maximum number of songs to download (default: 10)",
    )

    args = parser.parse_args()
    url = args.url
    output_dir = args.output_dir
    meta = args.meta
    silent = args.silent
    limit = args.limit

    main(url, output_dir, meta, silent, limit)
