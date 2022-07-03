import requests
from bs4 import BeautifulSoup

res = requests.get('https://free-proxy-list.net')
content = BeautifulSoup(res.text, 'lxml')
table = content.find('table')
rows = table.find_all('tr')
cols = [[col.text for col in row.find_all('td')] for row in rows]


proxies = []
proxy_index = 0

for col in cols:
    try:
        if col[4] == 'elite proxy' and col[6] == 'yes':
            proxies.append('https://' + col[0]) #+ ':' + col[1])
    except:
        pass

def fetch():
    global proxy_index

    while proxy_index < len(proxies):
        try:
            #print('Trying proxy:', proxies[proxy_index])
            #res = requests.get( proxies={'https': proxies[proxy_index]}, params=params, timeout=5)
            #return res
            single_proxy =  proxies[proxy_index]
            #print(single_proxy)
            return single_proxy
            #print(single_proxy)

        except:
            print('Bad proxy...')
            proxy_index += 1
def run():
    fetch()
    #print(fetch())
    #fetch()
    global proxy_index
    proxy_index += 1
run()

#if __name__ == '__main__':
#    run()
