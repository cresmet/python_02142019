import requests
import lxml
import re
from bs4 import BeautifulSoup


r = requests.get('https://www.keepinspiring.me/dr-seuss-quotes/')

# print(r.content)

c = r.content
soup = BeautifulSoup(c, 'lxml')

# print(soup.prettify().encode('utf-8'))

main_content = soup.find_all('div', attrs={'class': 'author-quotes'})

# print(main_content.encode('utf-8'))

for my_qt in main_content:
    # print((my_qt.text).strip('\'"'))
    # print re.sub('"', '', my_qt.text)

    s = my_qt.text
    s = re.sub(r'[^\w\s]', '', s)
    print(s)
