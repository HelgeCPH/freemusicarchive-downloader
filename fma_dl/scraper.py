from bs4 import BeautifulSoup
from json import loads, dump
import requests


def find_all_songs(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    songs_html = soup.find_all("div", {"class": "play-item"})
    return songs_html


def find_song(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    song_html = soup.find("div", {"class": "play-item"})
    return song_html


def extract_metadata(div_html):
    metadata_str = div_html.get("data-track-info")
    metadata = loads(metadata_str)

    return metadata


def find_last_page_idx(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    page_links_html = soup.find("div", {"class": "pagination-full"})
    page_links_html.find_all("a")
    # The second last element links to the last page
    # The last element is an ">" symbol linking to the next page
    last_page_str = page_links_html.find_all("a")[-2]
    last_page_idx = int(last_page_str.get_text())

    return last_page_idx


def scrape_song_metadata_from_pages(url, limit=1000):
    metadata = []

    # Maximum number of songs per page is 200. Larger values return pages of
    # default size 20.
    params = {"pageSize": 200, "page": 1}
    response = requests.get(url, params=params)
    last_page_idx = find_last_page_idx(response.content)

    for idx in range(1, last_page_idx + 1):
        if idx > 1:
            # For the first page, extract the data from the response object from
            # the request above.
            response = requests.get(url, params=params)
        for song_html in find_all_songs(response.content):
            song_metadata = extract_metadata(song_html)
            metadata.append(song_metadata)

            if len(metadata) >= limit:
                return metadata
