import requests as rq
from bs4 import BeautifulSoup
from bs4 import NavigableString

qUrl = 'https://books.toscrape.com/'
qHeaders = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'} 

qResp = rq.get(url = qUrl , headers = qHeaders)

#print(qResp.status_code)
#print(qResp.content)
#print(type(qResp.content))

bSoup = (BeautifulSoup)
bSoup = BeautifulSoup (qResp.content,'html.parser')

#print (bSoup.h3)
#print (bSoup.ol.children)

def removeExtra(itration):
    return list (filter(lambda x : type (x) != NavigableString, itration))

# print (removeExtra(bSoup.ol.children))

olChilds = removeExtra(bSoup.ol.children)
#print (olChilds[0].h3.getText ()) 

#print (olChilds[4].h3.getText ()) 


###--- title search type 1 ---###
#titleList = []
#for ol in olChilds:
#    titleList.append (ol.h3.getText())
#print (titleList)

###--- title search type 2 ---###
titleList = [ol.h3.getText() for ol in olChilds]
#print (titleList)

###--- search only selected title from 5th number to 8th number ---###
titleList = [ol.h3.getText() for ol in olChilds]
print (titleList[4:8])




