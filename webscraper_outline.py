import requests

from BeautifulSoup import BeautifulSoup


def tradeSpider(maxPages):

    page = 1

    while page <= maxPages:

        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=phones&_sacat=0&_fsrp=' + str(page)

        sourceCode = requests.get(url)

        plainText = sourceCode.text

        soup = BeautifulSoup(plainText)

        for link in soup.findAll('a',{'class':'vip'}):

            href = link.get('href')

            title = link.string

            print(title)

            print(' ')

            print(href)

            print(' ')

            getSingleItemData(href)

        page += 1

def getSingleItemData(itemUrl):

    sourceCode = requests.get(itemUrl)

    plainText = sourceCode.text

    soup = BeautifulSoup(plainText)

    for itemPrice in soup.findAll('span',{'class':'notranslate'}):

        print(itemPrice.string)

        print(' ')

        print(' ')

    for link in soup.findAll('a'):

        href = link.get('href') #if only giving end of url, can write: href = "https://URLEXAMPLE.com" + link.get('href')

        print('LINKS WITHIN THIS PAGE:')

        print(href)

        print(' ')

        print(' ')

tradeSpider(1)
