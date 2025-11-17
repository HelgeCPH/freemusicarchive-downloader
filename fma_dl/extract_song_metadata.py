# Thx ChatGPT

import os
import mutagen

def extract_metadata(src_dir, silent, prune):
    # create a new file for writing the title-author pairs in UTF-8 format
    with open(os.path.join(src_dir, 'meta.txt'), 'w', encoding='utf-8') as f:
        # loop through each file in the directory
        for filename in os.listdir(src_dir):
            # check if the file is an MP3 file
            if filename.endswith('.mp3'):
                # open the file and get the metadata
                filepath = os.path.join('songs', filename)
                audio = mutagen.File(filepath)

                # get the title and author from the metadata
                title = audio.get('TIT2', ['Unknown Title'])[0]
                author = audio.get('TPE1', ['Unknown Artist'])[0]

                # check if the metadata is missing
                if title == 'Unknown Title' or author == 'Unknown Artist':
                    # print a message indicating the missing metadata
                    if not silent:
                        print('Unknown metadata: ', filepath)

                    if prune:
                        # delete the file
                        os.remove(filepath)

                else:
                    # write the title-author pair to the text file
                    f.write(f'{title} - {author}\n')
