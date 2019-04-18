from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
my_url = 'http://redditlist.com/all?page='


#opens connection and grabs page
filename = "subs.csv"
f = open(filename, "w")



for i in range(15):
	my_url = my_url + str(i)
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()
	#html parser
	page_soup = soup(page_html, "html.parser")

	containers = page_soup.findAll("span", {"class":"subreddit-url"})
	for container in containers:

		sub = container.a.text.strip()
		f.write(sub + "\n")
	my_url = my_url[:-1]
f.close()
