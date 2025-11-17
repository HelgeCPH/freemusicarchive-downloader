import re
import requests
from urllib.parse import urlparse, urlunparse
from bs4 import BeautifulSoup
from enum import Enum


class UrlValidationResult(Enum):
    VALID = 0
    INVALID_URL = 1
    INVALID_PAGE = 2


class UrlValidationErrors(Enum):
    INVALID_URL = "Error: URL must start with 'https://freemusicarchive.org/'"
    INVALID_PAGE = "Error: this is not a music listing page"


def get_error_message(result):
    return {
        UrlValidationResult.INVALID_URL: UrlValidationErrors.INVALID_URL.value,
        UrlValidationResult.INVALID_PAGE: UrlValidationErrors.INVALID_PAGE.value,
    }.get(result, "Unknown error")


def validate_url(url):
    if not url.startswith('https://freemusicarchive.org/'):
        return UrlValidationResult.INVALID_URL

    # Remove query parameters from URL
    parsed_url = urlparse(url)._replace(query=None)
    url = urlunparse(parsed_url)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    if not soup.find("div", {"class": "play-item"}):
        return UrlValidationResult.INVALID_PAGE

    return UrlValidationResult.VALID
