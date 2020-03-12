import requests
from bs4 import BeautifulSoup as bs
import urllib.parse

url = 'https://eksisozluk.com/rastgele-entry-numarasi-yazmak--5987143?p='

headers = {
    'User-Agent': (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    )
}

entryLink = urllib.parse.quote('eksisozluk.com/entry/')

pageNum = 1
url = url + str(pageNum)

r = requests.get(url, headers = headers)
while r.status_code == 200:
    url = url[:url.index('=') + 1] + str(pageNum)
    r = requests.get(url, headers = headers)

    soup = bs(r.content, 'html.parser')
    if soup.find(id = 'entry-item-list'):
        entryler = soup.find(id = 'entry-item-list').find_all('li')
        for num, entry in enumerate(entryler, 1):
            content = entry.find(class_='content').get_text(strip = True)
            entryNo = entry.find(class_= 'entry-date permalink').get('href')[7:]

            if entryNo in content:
                print('The entry which gives the link to itself:', 'https://' + entryLink + str(entryNo))
                print('Page number: {} \ncontent: \n{}\n\n'.format(pageNum, content))
        pageNum += 1