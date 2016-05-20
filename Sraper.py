from bs4 import BeautifulSoup
import requests
import re


url = "http://smithstix.com/music"

r = requests.get(url)

soup = BeautifulSoup(r.content)

divs = soup.find_all("div")

for div in divs:
    print(div.text)

#eventColumns = soup.find_all("div", {"class": "events-row"})
g_data = soup.find_all("div", {"class": "events-list-container"})


for item in g_data:
        title = item.contents[1].find_all("div", {"class": "event-title"})[0].text
        titleEncoded = title.encode("ascii")
        day = item.contents[1].find_all("div", {"class": "day-container"})[0].text
        dayEncoded = day.encode("ascii")
        month = item.contents[1].find_all("div", {"class": "month-container"})[0].text
        monthEncoded = month.encode("ascii")
        year = item.contents[1].find_all("div", {"class": "year-container"})[0].text
        yearEncoded = year.encode("ascii")

print(titleEncoded, dayEncoded.strip(), monthEncoded.strip(), yearEncoded.strip())
        #print (dayEncoded.strip())
        #print (monthEncoded.strip())
        #print (yearEncoded.strip())
