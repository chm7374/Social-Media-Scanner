from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import urllib
from urllib.request import urlopen
from lxml import html
import nltk

# This code searches the html of a specific instagram page and relays the information.
def post_scan():
    """url = "https://www.instagram.com/p/CDZPTB3ApFJ/"
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    # kill all script and style elements
    for script in soup(["script"]):
        script.extract()  # rip it out
    # get text
    print(soup)
    text = soup.get_text()
    print(text)
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    print(text)"""
    url = "https://www.instagram.com/p/CDZPTB3ApFJ/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "lxml")
    first_child = soup.find("body")
    print(first_child.find("div").findAll)



if __name__ == '__main__':
    post_scan()
