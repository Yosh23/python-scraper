from bs4 import BeautifulSoup as bs
import lxml

with open('test.html', 'r') as html_file:
    content = html_file.read()

    soup =  bs(content, 'lxml')
    titles = soup.find_all('title')
    h1s = soup.find_all('h1')

    for title in titles:
        print(title.text)

    for h1 in h1s:
        print(h1.text)