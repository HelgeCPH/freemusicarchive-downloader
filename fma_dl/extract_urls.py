import re

def extract_urls(page):
    # compile the regex pattern
    pattern = re.compile(r'<div class="play-item[^\n]*')

    # search for all matches in the page
    matches = pattern.findall(page)

    url_pattern = re.compile(r'https:\\/\\/files.freemusicarchive.org[^&]*')

    return [url_pattern.findall(match)[0].replace('\/', '/').split('"')[0] for match in matches]