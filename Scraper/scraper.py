import requests
from bs4 import BeautifulSoup
import mechanize
import os

if os.path.exists("htmlDump.txt"):
  os.remove("htmlDump.txt")

session = requests.Session()
url = 'https://www.tabroom.com/index/index.mhtml'

pageText = session.get(url)

soup = BeautifulSoup(pageText.text, 'html.parser') # extract

tournsDump = soup.find_all('tbody')[0]
tournsDump = tournsDump.prettify()

# temporary dump into file so we can sort through the html and figure out what we're tryna extract

f = open(r'/Users/arnav/Desktop/Arnav/Debate/Coaching/Code/Shopping Cart/Tournament-Shopping-Cart/Scraper/htmlDump.txt', "w+")
f.write(str(tournsDump))