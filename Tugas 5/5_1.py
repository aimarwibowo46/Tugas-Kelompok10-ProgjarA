from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

def get_soup(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser')

def getGoBlog(num):
    soup = get_soup("https://go.dev/doc/")
    #Get value tag a with beautifoulsoup in article tag
    tag = soup.find_all('article')
    
    #Get value tag a with beautifulsoup in article tag
    tag_a = tag[0].find_all('a')
    
    total=1
    for i in tag_a:

        #Get value tag a with beautifulsoup in article tag
        tag_a_text = i.get_text()
        print("{}. akan mengambil: {}".format(total, tag_a_text))
        total+=1
        if total == num+1:
            break
    
    return True

def main():
    msg = input("> Jumlah link yang ingin di ambil: ")
    getGoBlog(int(msg))

if __name__ == '__main__':
    main()
