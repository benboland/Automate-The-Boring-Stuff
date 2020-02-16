#! python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads

import requests, os, bs4, threading
os.makedirs('xkcd', exist_ok=True)      # store comics in ./xkcd

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # download the page
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # find the URL of the comic image
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            comicUrl = 'https:' + comicUrl
            # download the image
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# create and start the thread objects
downloadThreads = []        # a list of all the thread objects
for i in range(0, 1400, 100):   # loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
