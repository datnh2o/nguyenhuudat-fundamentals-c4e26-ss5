from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
import pyexcel
url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)


# 2. Download content
raw_data= conn.read()
page_content = raw_data.decode("utf8")
with open("dantri.html","wb") as f:
    f.write(raw_data)


# 3.Find ROI
soup = BeautifulSoup(page_content,"html.parser")
ul = soup.find("ul","")

# 4. Extract ROI
li_list = ul.find_all("li")
# print (li_list)
song_list = []
for li in li_list:
    h3= li.h3
    a= h3.a
    title = a.string
    h4 = li.h4
    a= h4.a
    artist = a.string
    songs = {
    "artist":artist,
    "title": title
    }
    song_list.append(songs)
    # print(title)
    # print(artist)
pyexcel.save_as(records=song_list, dest_file_name="songs.xlsx")


# 5. Download from youtube
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 100, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
for song in song_list:
    name = song["title"]
    print(name)
    dl.download([name])