from urllib.request import urlopen
from urllib.parse import quote
from requests import get
from bs4 import BeautifulSoup
import re
import codecs

output = codecs.open("data.txt",'wb',encoding="utf-8")


url = "input_address";

urls = []
for i in range(1,20):
    urls.append(url+str(i)+"1") #Extend data crawling


for url in urls:
    html = urlopen(url)
    source = html.read()
    html.close()

    q_urls=[]

    soup = BeautifulSoup(source, "html.parser", from_encoding = 'utf-8')
    questions = soup.find_all(class_="question")

    for question in questions:
        link = question.a.get('href')
        url = link
        q_urls.append(url)


    for q_url in q_urls:
        source = get(q_url)
        soup = BeautifulSoup(source.content, "html.parser", from_encoding = 'utf-8')
        question_title = soup.find(class_="c-heading__title")
        question_content = soup.find(class_="c-heading__content")
        print(question_title.text.strip())
        output.write(question_title.text.strip())
        if(question_content):
            print(question_content.text.strip())
            output.write(question_content.text.strip())

output.close()
