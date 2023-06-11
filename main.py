import pandas as pd
from bs4 import BeautifulSoup
import requests

url="https://www.imdb.com/chart/top"
page=requests.get(url)

c=page.content
#print(c)

soup=BeautifulSoup(page.content,"html.parser")
#print(soup.prettify())

sm=soup.find_all('td',class_='titleColumn')
movies=[]

for movie in sm:
    movie=movie.get_text().replace('\n',"")
    movie=movie.strip(" ")
    movies.append(movie)

sr=soup.find_all('td',class_='ratingColumn imdbRating')
ratings=[]
for rating in sr:
    rating=rating.get_text().replace('\n',"")
    rating=rating.strip(" ")
    ratings.append(rating)

data=pd.DataFrame()
data['Movies Names']=movies
data['ratings']=ratings
data.head()
data.to_csv("ftb.csv",index=False)