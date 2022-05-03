import requests 
from bs4 import BeautifulSoup
from save_csv import save_to_csv


# url of most popular films
url_imdb = ('https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm')
films = []

# settings
r_imdb = requests.get(url_imdb)
html_imdb = r_imdb.text
soup = BeautifulSoup (html_imdb, 'html.parser')

table = soup.find ('tbody')
lines = table.find_all ('tr')

for line in lines:
  
  item = line.find_all('td')
  data = item[1].text
  
  name = data.split('\n')[1]
  year = data.split('\n')[2]
  
  note = item[2].text
  note= note.split('\n')[1]

  film = {
  'name' : name,
  'year' : year,
  'note' : note
  }

  films.append(film)

save_to_csv(films)