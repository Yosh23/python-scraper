from bs4 import BeautifulSoup as bs
import lxml

with open('file.html', 'r') as html_file:
    content = html_file.read()

    soup =  bs(content, 'lxml')
    ps = soup.find_all('p')
    print(ps)
    for p in ps:
        print(p.text)