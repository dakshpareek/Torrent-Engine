#!C:\Python36\python.exe 
from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import cgi
from pickle import dump,load
import json,random
import time
from get_ip import IP
import winsound
from fake_useragent import UserAgent
import pickle,os,cgi
from pickle import load
import cgi, cgitb
print("Content-type: text/html")
form = cgi.FieldStorage()
id = str(form.getvalue('id'))
n=id
n=n.replace(" ","+")
print(n)
'''
		#self.i=IP()
		#self.browser,self.ip=self.i.ip()
		#self.thepiratebay(n)
		#self.yts(n)
		

	def get_ip(self):
		return self.i.ip()

	def make_request(self,url):
		proxies_req = Request(url)
		proxies_req.add_header('User-Agent', self.browser.random)
		#proxies_req.set_proxy(self.ip,'http')
		return proxies_req

	def thepiratebay(self,url):
		url = "https://thepiratebay3.org/index.php?q="+str(url)
		req1= self.make_request(url)
		html = urlopen(req1).read().decode('utf8')
		soup=BeautifulSoup(html,"lxml")
		movies = soup.findAll("div", {"class": "detName"})
		all_data=[]
		i=0
		Getting All Data From Search
		for every_movie in movies:
			a_tag=every_movie.findAll("a")
			print("ID:-> "+ str(i)+" " + a_tag[0].text)
			#print(a_tag[0].attrs["href"])
			all_data.append([a_tag[0].attrs["title"],a_tag[0].attrs["href"]])
			i+=1
		Get Id to see magnet link
		getid=int(input("Enter Id to Get Magnet Link"))
		link=all_data[getid][1]
		req2=self.make_request(link)
		html = urlopen(req2).read().decode('utf8')
		soup=BeautifulSoup(html,"lxml")
		movies = soup.findAll("div", {"class": "download"})
		a_tag=movies[0].findAll("a")
		print(":Magnet Link:")
		print(a_tag[0].attrs["href"])

	def yts(self,url):
		url = "https://yts.am/browse-movies/{}/all/all/0/latest".format(url)
		req1= self.make_request(url)
		html = urlopen(req1).read().decode('utf8')
		soup=BeautifulSoup(html,"lxml")
		movies = soup.findAll("a", {"class": "browse-movie-link"})
		all_data=[]
		i=0
		for every_movie in movies:
			title=every_movie.findAll("img")
			title=title[0].attrs['alt']
			link=every_movie.attrs['href']
			print("ID :-> "+str(i)+" "+title)
			all_data.append([title,link])
			i+=1
		Get Id to see magnet link
		getid=int(input("Enter Id to Get Magnet Link"))
		link=all_data[getid][1]
		req2=self.make_request(link)
		html = urlopen(req2).read().decode('utf8')
		soup=BeautifulSoup(html,"lxml")
		movies = soup.findAll("p", {"class": "hidden-xs hidden-sm"})
		movies = movies[0].findAll("a")
		for every_movie in movies:
			print(every_movie.text)
			print("Torrent File")
			print(every_movie.attrs['href'])
	

mv=Movie()
'''

