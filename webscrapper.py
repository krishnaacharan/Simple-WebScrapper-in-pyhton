from bs4 import BeautifulSoup
import requests
import sys
#reading the webpage as text
html=requests.get("https://syndicode.com/2019/01/09/33-concepts-every-js-developer-should-know/").text

#Using lxml parser to parse the text to html content
soup=BeautifulSoup(html,'lxml')
#finding the main class
points=soup.find("main")
#finding ordered list in div of main class
article=points.find("div",class_="article__content").ol
#accessing to all points that we need
s=[]
for a,i in  zip(article.findAll('li'),range(0,100)):
    s.append(str(i)+". "+a.text)
    print(str(i)+". "+a.text)
# s array to store scraped values and sendon them into adata.txt file
with open("data.txt",'w') as f:
    for sa in s:
        f.write(str(sa))
        f.write("\n")

