import requests
from bs4 import BeautifulSoup

file = open("scraped.txt","w")
count = 1
st = ""

req = "https://internshala.com/internships/page-1"
response = requests.get(req).text
html_file = open("internshala.html","w")
html_file.write(response)
soup = BeautifulSoup(response,'lxml')
internships = soup.find_all("div","internship_meta")
for int in internships:
    profile = int.find("div","heading_4_5 profile").text.strip()
    company = int.find("div","heading_6 company_name").text.strip()
    location = int.find("div",id="location_names").text.strip()
    stipend = int.find("span","stipend").text.strip()
    stri = "" + str(count) + ": Profile: " + str(profile) + " Company: " + str(company) + " Location: " + str(location) + " Stipend: " + str(stipend) + "\n"
    st = st + stri
    count = count + 1

file.write(st)
