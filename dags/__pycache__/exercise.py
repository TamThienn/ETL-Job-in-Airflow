import requests
import pandas as pd
from bs4 import BeautifulSoup

symbol = []
firstname = []
lastname = []
username = []

url = 'https://webscraper.io/test-sites/tables'
response = requests.get(url)
t = response.text
soup = BeautifulSoup(t, features="html.parser")
trs = soup.find_all('tr')
for i in range(len(trs)):
   tds = trs[i].find_all('td')
   if len(tds) > 0  : 
      if str(tds[0].text) != '-':
         symbol.append(tds[0].text)
         firstname.append(tds[1].text)
         lastname.append(tds[2].text)
         username.append(tds[3].text)

data = {
   "#":symbol,
   "First Name":firstname,
   "Last Name":lastname,
   "Username":username
}

df = pd.DataFrame(data)
print(df)