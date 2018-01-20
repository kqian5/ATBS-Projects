#! python3
#! downloadXkcd.py - downloads every xkcd comic

import requests, bs4, os


# make a directory called "xkcd"
os.makedirs("xkcd", exist_ok=True)

def download_image(page="http://xkcd.com/"):
    # download url
    while not page.endswith("#"):
        res = requests.get(page)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)

        # find url of pic and download
        elem = soup.select("#comic img")
        if elem == []:
            print("Could not find image")
        else:
            pic_url = "http:" + elem[0].get("src")
            pic = requests.get(pic_url)
            pic.raise_for_status()

            # save contents of pic to file
            pic_file = open(os.path.join("xkcd", os.path.basename(pic_url)), "wb")
            for chunk in pic.iter_content(100000):
                pic_file.write(chunk)
            pic_file.close()

        prev = soup.select('a[rel="prev"]')[0].get("href")
        download_image("http://xkcd.com/" + prev)


download_image()


