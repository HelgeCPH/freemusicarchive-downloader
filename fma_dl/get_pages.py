import argparse
import re
import requests
from urllib.parse import urlparse, urlunparse, urljoin

def get_pages(url):
    # Set initial page parameters
    page_size = 200
    page_number = 1
    music_listing = ''

    # Loop through pages until no more pages with listings are found
    while True:
        # Build URL with page parameters
        query_params = {'pageSize': page_size, 'page': page_number}
        url_with_params = urljoin(url, '?' + '&'.join([f"{k}={v}" for k, v in query_params.items()]))

        # Request page and check for listings
        response = requests.get(url_with_params)
        page = response.content.decode()

        if not re.search(r'<div class="play-item[^\n]*', page):
            break
        
        music_listing += page
        page_number += 1

    return music_listing