import csv


def save_to_csv(films):
  
  # select the files
  file = open('films.csv', 'w')
  writer = csv.writer(file)
  writer.writerow(['NAME','YEAR', 'NOTE'])
  
  # for each movie in the received list write 1 line
  for film in films:
    writer.writerow(list(film.values()))
  
f = open('films.csv')