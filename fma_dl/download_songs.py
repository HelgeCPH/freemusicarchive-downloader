# Thx ChatGPT

import os
import urllib.request

def download_songs(urls, dest, silent):

    # create the songs directory if it doesn't exist
    if not os.path.exists(dest):
        os.makedirs(dest)

    for url in urls:
        # remove any whitespace at the beginning or end of the url
        url = url.strip()

        if not silent:
            print('Downloading song: ' + url)
            
        # create a filename for the downloaded file by taking the last part of the URL
        filename = url.split('/')[-1]

        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36')

        # make the request and save the downloaded file
        with urllib.request.urlopen(req) as response, open(os.path.join(dest, filename), 'wb') as outfile:
            outfile.write(response.read())
