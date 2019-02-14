import requests
import lxml
import re
from bs4 import BeautifulSoup


r = requests.get(
    'https://www.bighivemind.com/70-brilliant-dr-suess-quotes-everything-reading-love/')

# print(r.content)

c = r.content
soup = BeautifulSoup(c, 'lxml')

# print(soup.prettify().encode('utf-8'))

main_content = soup.find_all('div', attrs={'class': 'quote'})

# print(main_content.encode('utf-8'))

for my_qt in main_content:

    # using regex to stip double quotes
    s = my_qt.text
    #s = re.sub(r'[^\w\s]', '', s)
    print(s)
