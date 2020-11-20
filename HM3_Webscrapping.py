from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import lxml
import requests
import re

# to be inserted in a loop to get to the different pages, from 1 to 300
base_url = "https://www.goodreads.com/list/show/1.Best_Books_Ever?page=1"

html = urlopen(base_url)

soup = BeautifulSoup(html.read(), features="lxml")
links = []
regex = "/book/show/."

for link in soup.find_all("a"):
	if re.match(regex, str(link.get("href"))):
		links.append(link.get("href"))
links = list(dict.fromkeys(links))

url_trunk = "https://www.goodreads.com"

links = [ url_trunk+link for link in links]


outfile = open("test.txt", "w")
for link in links:
 	outfile.write(link)
 	outfile.write("\n")
outfile.close()







#links = re.findall('href="/book/show/*')

# stuff = requests.get(base_url)

# html_doc = stuff.text

# #soup = BeautifulSoup(stuff, features="lxml")
# soup = BeautifulSoup(stuff.content, features="lxml")

# pretty_soup = soup.prettify()

# links = soup.find_all('href')
# print(links)
#for link in links:
#	names = link.contents[0]
#	fullLink = link.get('href')
#	print([names,fullLink])


#f = open("test.txt", "w", encoding="utf-8")
#f.write(soup.prettify())
#f.close()


