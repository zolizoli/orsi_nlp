import urllib.request
from bs4 import BeautifulSoup

base_url = 'http://www.futas.net/naptar/day.php?date='
info_ur = 'http://www.futas.net/naptar/'

year = range(2013, 2019)
month = range(1, 13)
day = range(1, 32)

for y in year:
    for m in month:
        for d in day:
            pattern = str(y) + str(m).zfill(2) + str(d).zfill(2)
            url = base_url + pattern
            with urllib.request.urlopen(url) as response:
                try:
                    html = response.read()
                    soup = BeautifulSoup(html, "lxml")
                    events = soup.find_all('a', {'class': 'entry'})
                    for e in events:
                        info = e['href']
                        event_url = info_ur + info
                        event_page = urllib.request.urlopen(event_url)\
                            .read().decode('utf-8')
                        startp = event_page.find('Helyszín:')
                        print(event_page[startp:startp+80])

                except Exception as e:
                    print(e)
                    continue
