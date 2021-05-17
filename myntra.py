import requests
import json
from bs4 import BeautifulSoup

count = 1
final_st = ""
file1 = open("myn.json","w")

pgno = 1
req = "https://www.myntra.com/tshirts"
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0", "Connection" : "keep-alive"}
response = requests.get(req,headers=headers).text
file = open("myntra.html","w")
soup = BeautifulSoup(response,'lxml')
file.write(soup.prettify())
products = soup.find_all("script",type="application/ld+json")
for prod in products:
    if(prod != None):
        st = json.loads(prod.string)
        stfr = json.dumps(st,indent=4)
        file1.write(stfr)
        #print(stfr)

'''while count < 10000:
    pgno = 1
    req = "https://www.myntra.com/tshirts?p=" + str(pgno) + "&plaEnabled=false"
    print(req)
    response = requests.get(req).text
    soup = BeautifulSoup(response,'lxml')
    products = soup.find_all("li","product-base")
    print(products)
    for prod in products:
        link = prod.find("a",target="_blank").href
        print(link)
        count = count + 1
        break
    
    break'''
