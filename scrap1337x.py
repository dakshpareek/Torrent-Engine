#!C:\Python36\python.exe 
from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import cgi
from pickle import dump,load
import json,random,pickle
import time,gzip
from get_ip import IP
import winsound
from fake_useragent import UserAgent
from  more_itertools import unique_everseen

class Games:
        def __init__(self):
                try:
                        self.f1=open('all_movies.txt','rb')
                        self.prev=load(self.f1)
                        self.f1.close()
                except:
                        self.prev=[]
                #self.i=IP()
        
        def get_ip(self):
                return self.i.ip()
                                
        def make_request(self,url,browser,ip):
                proxies_req = Request(url)
                proxies_req.add_header('User-Agent', browser)
                proxies_req.set_proxy(ip,'http')
                #print(ip)
                return proxies_req

        def scrape_data(self,n):
                #browser,ip=self.get_ip()
                ip='208.95.62.81:3128'
                browser=UserAgent()
                print("Page "+str(n)+"-------->")
                #filee=self.filee
                url = "http://1337x.to/movie-library/{}/".format(n)
                pro_req=self.make_request(url,browser.random,ip)
                try:
                        html = urlopen(pro_req).read().decode('utf8','ignore')
                except:
                        html = urlopen(pro_req).read().decode('utf8','ignore')
                soup=BeautifulSoup(html,"lxml")
                games = soup.findAll("div", {"class": "modal-header"})
                imgs = soup.findAll("img", {"class": "lazy"})
                #print(games[0])
                movie_data=[]
                for ig,every in enumerate(games):
                        a_tag=every.find('a')
                        title=a_tag.text
                        print(title)
                        link=a_tag.attrs['href']
                        cat=every.find('div', {"class": "category"})
                        cate=cat.findAll('span')
                        cat=[]
                        for i in cate:
                                cat.append(i.text)
                        #print(title,link,cat)
                        url1="http://1337x.to"+str(link)
                        pro_req1=self.make_request(url1,browser.random,ip)
                        try:
                                html1 = urlopen(pro_req1).read().decode('utf8','ignore')
                        except:
                                html1 = urlopen(pro_req1).read().decode('utf8','ignore')
                        soup1=BeautifulSoup(html1,"lxml")
                        table=soup1.find('table',{"class":"table-list table table-responsive table-striped"})
                        #print(table)
                        try:
                                trs=table.findAll('tr')
                        except:
                                print("e")
                        #print(trs[0])
                        #print(trs[1])
                        igg=imgs[ig].attrs['data-original']
                        #print(igg)
                        all_tor=[]
                        k=1
                        til=len(trs)//2
                        if til>=10:
                                til=11
                        if til<=2:
                                til=2
                        try:
                                for j in trs[1:til]:
                                        lk=j.findAll('a')
                                        link2=lk[1].attrs['href']
                                        tit=lk[1].text
                                        #print(tit)
                                        tds=j.findAll('td')
                                        size=tds[4].text
                                        url2="http://1337x.to"+str(link2)
                                        pro_req2=self.make_request(url2,browser.random,ip)
                                        try:
                                                html2 = urlopen(pro_req2).read().decode('utf8','ignore')
                                        except:
                                                print("E")
                                        soup2=BeautifulSoup(html2,"lxml")
                                        mg=soup2.findAll('ul',{"class":"download-links-dontblock btn-wrap-list"})
                                        mglink=mg[0].find('a').attrs['href']
                                        all_tor.append([tit,size,mglink])
                                        #time.sleep(0.5)
                        except:
                                print("Exception")
                                
                        movie_data.append([title,igg,cat,all_tor])
                        print(len(all_tor))
                #print(movie_data)
                self.prev=movie_data + self.prev
                #data1=list(unique_everseen(self.prev))
                #pfile = r'testdata{}.pkl.gz'.format(filee)
                #pickle.dump(data1, gzip.open(pfile, "w"), pickle.HIGHEST_PROTOCOL)
                #mv='all_movies.txt'.format(filee)
                f1=open('all_movies.txt','wb+')
                dump(self.prev,f1,protocol=2)
                f1.close()
                
                
                                

pags=range(100,150)
for i in pags:
        gm=Games()
        gm.scrape_data(i)
