import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_string = "postgresql://postgres:root@localhost:5432/AnimeDB"
db = create_engine(db_string)

Session = sessionmaker(db)  
session = Session()

animes = pd.read_csv('anime.csv')

animes = animes.dropna(axis=0)

dictGenres = {}

for thisAnime in animes.itertuples():
	genres = thisAnime[3]
	genresArr = genres.split(',')
	for genre in genresArr:
		if (str(genre).strip() not in list(dictGenres.keys())):
			dictGenres[str(genre).strip()] = len(dictGenres)

for genre in dictGenres:
	session.execute(f"insert into genre (genre_id, genre_name) values ({dictGenres[genre]},'{genre}');")
	session.commit()


for thisAnime in animes.itertuples():
	anime_id = thisAnime[1]
	name = thisAnime[2]
	genres = thisAnime[3]
	anime_type = thisAnime[4]
	episodes = thisAnime[5]
	if(episodes == 'Unknown'):
		episodesInt = 999
	else:
		episodesInt = int(episodes)
	rating = thisAnime[6]
	members = thisAnime[7]
	session.execute(f"INSERT INTO anime(anime_id, name, type, rating, members, episodes)VALUES ({anime_id}, '{name}', '{anime_type}', {rating}, {members}, {episodesInt});")
	session.commit()
	genresArr = genres.split(',')
	for genre in genresArr:
		thisGenreId = dictGenres[str(genre).strip()]
		session.execute(f"INSERT INTO anime_genre(anime_id, genre_id)VALUES ({anime_id}, {thisGenreId});")
		session.commit()