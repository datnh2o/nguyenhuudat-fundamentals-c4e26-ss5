#tạo 1 kết nối 
#down nội dung trang web về máy
#tìm vòng 'roi'
#lưu data về 1 định dạng nào đó

#1

from urllib.request import urlopen 
from bs4 import BeautifulSoup
import pyexcel
url ="https://dantri.com.vn/"
conn = urlopen(url)
#2
raw_data = conn.read()
page_content = raw_data.decode("utf8") 
#3
soup = BeautifulSoup(page_content, "html.parser")
ul = soup.find("ul", "ul1 ulnew")
#4
li_list = ul.find_all("li")
new_list = []
for li in li_list:
    h4 = li.h4
    a = h4.a
    link = url + a["href"]
    tittle = a.string
    news = {
        "link": link,
        "tittle": tittle,
    }
    new_list.append(news)

pyexcel.save_as(records=new_list, dest_file_name="your_file.xlsx")