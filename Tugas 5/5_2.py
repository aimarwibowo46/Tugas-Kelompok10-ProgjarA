from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

def get_soup(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser')

def getGoPackage(msg, num):
    url = "https://pkg.go.dev/search?limit={}&m=package&q={}#more-results".format(num, msg)
    soup = get_soup(url)

    #Get value with beautifoulsoup in class SearchSnippet
    SearchSnippet = soup.find_all('div', class_='SearchSnippet')
    total = 1 
    for hasil in SearchSnippet:

        #Get p and a tag with beautifulsoup in class SearchSnippet
        p = hasil.find_all('p')

        if (p != []):    
            text = p[0].get_text().split(' ')
            text = text[12:]
            text = ' '.join(text)
        else:
            text ="Tidak ada"

        #Get text from a tag
        link = hasil.find_all('a')
        url_hasil_search = "https://pkg.go.dev" + link[0].get('href')
        
        print("Hasil {}\nkegunaan package: {}\nUrl: {}\n\n".format(total, text, url_hasil_search))
        total+=1

    return True

def getGoBlog(msg):
    url = "https://pkg.go.dev/search?q=" + msg
    soup = get_soup(url)

    #Get value with beautifoulsoup in class SearchSnippet
    SearchSnippet = soup.find_all('div', class_='SearchSnippet')

    #Get href with beautifulsoup in class SearchSnippet
    judul = SearchSnippet[0].find_all('a')
    url_hasil_search = "https://pkg.go.dev" + judul[0].get('href')
    soup = get_soup(url_hasil_search)

    #Get value with beautifoulsoup in class Documentation-indexList
    Documentation_indexList = soup.find_all('ul', class_='Documentation-indexList')

    #Get value li with beautifoulsoup
    Documentation_indexList_li = Documentation_indexList[0].find_all('a')

    # Get all text with beautifulsoup
    for i in Documentation_indexList_li:
        text = i.get_text().split(' ')
        if (text[0] == 'type'):
            print(i.get_text())
        elif (text[0] == 'func'):
            print('\t' + i.get_text())
    return True

def main():   
    # getGoPackage("sort", 30)
    getGoBlog("llrb+petar")

if __name__ == '__main__':
    main()
