import requests

from BeautifulSoup import BeautifulSoup


def Scrape(maxPages):

    page = 1

    while page <= maxPages:

        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=phones&_sacat=0&_fsrp=' + str(page)

        source_code = requests.get(url)

        plain_text = sourceCode.text

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

    source_code = requests.get(itemUrl)

    plain_text = sourceCode.text

    soup = BeautifulSoup(plainText)

    for item_price in soup.findAll('span',{'class':'notranslate'}):

        print(item_price.string)

        print(' ')


    for link in soup.findAll('a'):

        href = link.get('href') #if only giving end of url, can write: href = "https://URLEXAMPLE.com" + link.get('href')

        print('LINKS WITHIN THIS PAGE:')

        print(href)


tradeSpider(1)
