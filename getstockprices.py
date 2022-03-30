import requests
from bs4 import BeautifulSoup
import json

''''
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
url = 'https://uk.finance.yahoo.com/quote/BTC-GBP'

r = requests.get(url)

soup =BeautifulSoup(r.text, 'html.parser')
#print(r.text)
#print(soup)
#print(soup.title.text)


regularMarketPrice = soup.find('fin-streamer', {'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
#print(regularMarketPrice)

regularMarketChange = soup.find('fin-streamer', {'class': 'Fw(500) Pstart(8px) Fz(24px)'}).text
#print(regularMarketChange)
regularMarketChangePercent = soup.find('fin-streamer', {'class': 'Fw(500) Pstart(8px) Fz(24px)'}).text

print(regularMarketChangePercent)
'''
'''
regularMarketPrice = soup.find('div', {'class':'D(ib) Mend(20px)'}).find-all('fin-streamer')[1].text
print(regularMarketPrice)

regularMarketChange = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text
print(regularMarketChange)
regularMarketChangePercent = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text
print(regularMarketChangePercent)
'''





def getData(symbol):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
    url = f'https://uk.finance.yahoo.com/quote/{symbol}'
    
    r = requests.get(url, headers=header)
    soup =BeautifulSoup(r.text, 'html.parser')
    #print(soup)
    stock = {
    'symbol' : symbol,
    'regularMarketPrice' : soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text ,
    'regularMarketChange'  : soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text ,
    'regularMarketChangePercent' : soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text
    }
    return stock

a = 'BTC-USD'
b = 'ETH-USD'
#print(getData(b))


mystocks = ['BTC-USD', 'ETH-USD']
stockdata = list()
#print(l[0])
#l2.append(getData(l[0]))
#print(l2)

for i in range(len(mystocks)):
    stockdata.append(getData(mystocks[i]))

print(stockdata)


with open('stockdata.json', 'w') as f:
    json.dump(stockdata, f)

#print('Fin.')