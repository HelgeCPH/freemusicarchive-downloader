import argparse
from download_songs import download_songs
from extract_song_metadata import extract_metadata
from extract_urls import extract_urls
from get_pages import get_pages

from url_validation import UrlValidationResult, get_error_message, validate_url

parser = argparse.ArgumentParser(description='Download music from the Free Music Archive')
parser.add_argument('url', type=str, help='URL of the webpage to download music from')
parser.add_argument('output_dir', type=str, help='Output directory for downloaded songs')
parser.add_argument('--silent', action='store_true', help='Do not log each downloaded song')
parser.add_argument('--meta', action='store_true', help='Extract metadata from downloaded songs')
parser.add_argument('--prune-no-meta', action='store_true', help='Prune songs with missing metadata')

args = parser.parse_args()
url = args.url
output_dir = args.output_dir
silent = args.silent
meta = args.meta
prune_no_meta = args.prune_no_meta

url_validation_result = validate_url(url)
if url_validation_result != UrlValidationResult.VALID:
    print(get_error_message(url_validation_result))
    exit()

print("Fetching pages...")
pages = get_pages(url)

print("Extracting URLs...")
urls = extract_urls(pages)

print("Downloading songs...")
download_songs(urls, output_dir, silent=silent)

if meta:
    print("Extracting metadata...")
    extract_metadata(output_dir, silent=silent, prune=prune_no_meta)

print("Done!")
