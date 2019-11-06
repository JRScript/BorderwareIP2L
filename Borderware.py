import requests
import re
from bs4 import BeautifulSoup
def border(c):
    r = requests.get("http://reputationauthority.org/lookup?ip=" + IP)
    soup = BeautifulSoup(r.content, 'html.parser')
    doc = open('html.txt', "w+")
    doc.write(soup.prettify())
    doc.close()
    doc2 = open('html.txt', 'r')
    contents = doc2.read()
    parse = re.findall("(?si)Reputation\sScore\:.*?style\=.*?\>\n\s+(?P<Socre>.*?)\s+\<\/td>.*?ISP\sLocation\:.*?\">\n\s+(?P<ISPLocation>.*?)\s+\<\/td>.*?ISP\:.*?\">\n\s+(?P<ISP>.*?)\s+<\/td>", contents)
    print(parse)
    doc2.close()

IP = input("IP: ")

X = border(IP)
