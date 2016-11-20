# coding:utf-8

from bs4 import BeautifulSoup
import requests

url = r'http://www.maiziedu.com/course/913/'

web_data = requests.get(url)
print web_data
soup = BeautifulSoup(web_data.text, 'lxml')
print soup
dirt_url = soup.select('body > div.video-lists-container.marginB40 > div.VLCleft > div > div > ul > li > a')
print dirt_url

names = []
host = r'http://www.maiziedu.com'
video_urls = []
for i in dirt_url:
	print i.text, i.get('href')
	video_urls.append(i.get('href'))
print video_urls
try:
	for j in video_urls:
		m = host + j
		print m
except:
	pass
else:
	pass