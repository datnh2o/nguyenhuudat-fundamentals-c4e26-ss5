# Part 1: 

from youtube_dl import YoutubeDL
import pyexcel
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)

raw_data = conn.read() 
page_content = raw_data.decode("utf8")

soup = BeautifulSoup(page_content, "html.parser")

section = soup.find("section", "section chart-grid")

div = section.find("div")

li_list = div.ul.find_all("li")

news_list = []

for li in li_list:
    h3 = li.h3
    a = h3.a
    name = a.string

    h4 = li.h4
    a = h4.a
    title = a.string 
    
    news = {
        "Name" : name,
        "Title" : title,
    }
    news_list.append(news)

pyexcel.save_as(records=news_list, dest_file_name="Topmusic.xlsx")


# Part 2: 

options = {
    'default_search': 'ytsearch',
    'max_downloads': 6 , 
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)

for i in news_list:
    dl.download(i["Name"] + (i["Title"]))