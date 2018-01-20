#! python3
# lucky.py - Opens several google search results

import requests, sys, webbrowser, bs4


search_terms = " ".join(sys.argv[1:])
res = requests.get("https://www.google.com/search?q=" + search_terms)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select(".r a")
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open("http://google.com" + linkElems[i].get("href"))


