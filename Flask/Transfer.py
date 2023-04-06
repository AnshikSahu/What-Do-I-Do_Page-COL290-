import csv
from database import engine
from sqlalchemy import text
with open("./#main.csv", 'r') as file:
   
   csvreader = csv.DictReader(file)
   i=0
   with engine.connect() as conn:
    conn.execute("DROP TABLE Movies")
    conn.execute("CREATE TABLE Movies(Movie_ID int AUTO_INCREMENT,Title varchar(200) default \"\",Genres varchar(500) default \"\",Release_Year varchar(100) default \"2000\",Tag_Line varchar(1000) default \"\",Overview varchar(10000) default \"\",Revenue varchar(100) default \"0\",Language varchar(100) default \"en\",Director varchar(1000) default \"\",Actors varchar(1000) default \"\",Runtime varchar(100) default \"0\",Age_certificate varchar(100) default \"U\",Homepage varchar(200) default \"\",Posters varchar(200) default \"\",Popularity varchar(100) default \"0\",Vote_Count varchar(100) default \"0\",Rating varchar(100) default \"7\",TMDB_ID varchar(100),IMDB_ID varchar(100),PRIMARY KEY(Movie_ID) )")
    for row in csvreader:
      i+=1
      print(i) 
      conn.execute(text(" INSERT INTO Movies(Title,Genres,Release_Year,Tag_Line,Overview,Revenue,Language,Director,Actors,Runtime,Age_certificate,Homepage,Posters,Popularity,Vote_Count,Rating,TMDB_ID,IMDB_ID) VALUES (\""+row[ "Title" ].replace("\""," ")+ "\" ,\""  +row[ "Genres" ].replace("\""," ")+ "\" ,\""  +row[ "Release Year" ].replace("\""," ")+ "\" ,\""  +row[ "Tag Line" ].replace("\""," ")+ "\" ,\""  +row[ "Overview" ].replace("\""," ")+ "\" ,\""  +row[ "Revenue"].replace("\""," ")+ "\" ,\""  +row[ "Language" ].replace("\""," ")+ "\" ,\""  +row[ "Director"].replace("\""," ")+ "\" ,\""  +row[ "Actors" ].replace("\""," ")+ "\" ,\""  +row[ "Runtime" ].replace("\""," ")+ "\" ,\""  +row[ "Age Certificate"].replace("\""," ")+ "\" ,\""  +row[ "Homepage" ].replace("\""," ")+ "\" ,\""  +row[ "Poster" ].replace("\""," ")+ "\" ,\""  +row[ "Popularity" ].replace("\""," ")+ "\" ,\""  +row[ "Vote Count"].replace("\""," ")+ "\" ,\""  +row[ "Rating" ].replace("\""," ")+ "\" ,\""  +row[ "TMDB ID"].replace("\""," ")+ "\" ,\""  +row[ "IMDB ID"].replace("\""," ")+ "\"  ) "))
   print(i)   
  
 