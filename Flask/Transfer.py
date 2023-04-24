import csv
# from database import engine
# from sqlalchemy import text
import mysql.connector

mydb= mysql.connector.connect(
        host= "localhost",
        user="root",
        password="my-secret-password",
        auth_plugin='mysql_native_password',
        database="photons"
        )
# with open("./#main.csv", 'r') as file:
   
# #     csvreader = csv.DictReader(file)
# #     i=0
# #     conn=mydb.cursor ()
# #     conn.execute("CREATE TABLE Movies(Movie_ID int AUTO_INCREMENT,Title varchar(200) default \"\",Genres varchar(500) default \"\",Release_Year varchar(100) default \"2000\",Tag_Line varchar(1000) default \"\",Overview varchar(10000) default \"\",Revenue varchar(100) default \"0\",Language varchar(100) default \"en\",Director varchar(1000) default \"\",Actors varchar(1000) default \"\",Runtime varchar(100) default \"0\",Age_certificate varchar(100) default \"U\",Homepage varchar(200) default \"\",Posters varchar(200) default \"\",Popularity varchar(100) default \"0\",Vote_Count varchar(100) default \"0\",Rating varchar(100) default \"7\",TMDB_ID varchar(100),IMDB_ID varchar(100),PRIMARY KEY(Movie_ID) )")
# #     for row in csvreader:
# #        i+=1
# #        print(i) 
# #        conn.execute(" INSERT INTO Movies(Title,Genres,Release_Year,Tag_Line,Overview,Revenue,Language,Director,Actors,Runtime,Age_certificate,Homepage,Posters,Popularity,Vote_Count,Rating,TMDB_ID,IMDB_ID) VALUES (\""+row[ "Title" ].replace("\""," ")+ "\" ,\""  +row[ "Genres" ].replace("\""," ")+ "\" ,\""  +row[ "Release Year" ].replace("\""," ")+ "\" ,\""  +row[ "Tag Line" ].replace("\""," ")+ "\" ,\""  +row[ "Overview" ].replace("\""," ")+ "\" ,\""  +row[ "Revenue"].replace("\""," ")+ "\" ,\""  +row[ "Language" ].replace("\""," ")+ "\" ,\""  +row[ "Director"].replace("\""," ")+ "\" ,\""  +row[ "Actors" ].replace("\""," ")+ "\" ,\""  +row[ "Runtime" ].replace("\""," ")+ "\" ,\""  +row[ "Age Certificate"].replace("\""," ")+ "\" ,\""  +row[ "Homepage" ].replace("\""," ")+ "\" ,\""  +row[ "Poster" ].replace("\""," ")+ "\" ,\""  +row[ "Popularity" ].replace("\""," ")+ "\" ,\""  +row[ "Vote Count"].replace("\""," ")+ "\" ,\""  +row[ "Rating" ].replace("\""," ")+ "\" ,\""  +row[ "TMDB ID"].replace("\""," ")+ "\" ,\""  +row[ "IMDB ID"].replace("\""," ")+ "\"  ) ")
# #        conn.execute("commit")
# #     print(i)   

# conn=mydb.cursor ()
# conn.execute("select * from Movies where Movie_ID = 1")
# print(conn.fetchall())

# with open("./#main.csv", 'r') as file:
#     print("Hi.. I am here")
#     csvreader = csv.DictReader(file)
#     print ("I have reached here")
#     i=0
#     conn=mydb.cursor ()
#     print("Here")
#     conn.execute("drop table Mov")
#     print("Dropped movies")
#     conn.execute("CREATE TABLE Mov(Movie_ID int AUTO_INCREMENT,Title mediumtext ,Genres mediumtext ,Release_Year varchar(100) default \"2000\",Tag_Line mediumtext ,Overview mediumtext ,Revenue mediumtext ,Language varchar(100) default \"en\",Director mediumtext ,Actors mediumtext ,Runtime varchar(100) default \"0\",Age_certificate varchar(100) default \"U\",Homepage mediumtext ,Posters mediumtext ,Popularity varchar(100) default \"0\",Vote_Count varchar(100) default \"0\",Rating varchar(100) default \"7\",TMDB_ID varchar(100),IMDB_ID varchar(100),PRIMARY KEY(Movie_ID) )")
#     print("created table")
#     for row in csvreader:
#        i+=1
#        print(i) 
#        print(row["poster_path"])
#        conn.execute((" INSERT INTO Mov(Title,Genres,Release_Year,Tag_Line,Overview,Revenue,Language,Director,Actors,Runtime,Homepage,Posters,Popularity,Vote_Count,Rating,TMDB_ID,IMDB_ID) VALUES (\""+row[ "title" ].replace("\""," ")+ "\" ,\""  +row[ "genres" ].replace("\""," ")+ "\" ,\""  +((row[ "release_date" ]).split("-")[0]).replace("\""," ")+ "\" ,\""  +row[ "tagline" ].replace("\""," ")+ "\" ,\""  +row[ "overview" ].replace("\""," ")+ "\" ,\""  +row[ "revenue"].replace("\""," ")+ "\" ,\""  +row[ "original_language" ].replace("\""," ")+ "\" ,\""  +row[ "directors"].replace("\""," ")+ "\" ,\""  +row[ "cast" ].replace("\""," ")+ "\" ,\""  +row[ "runtime" ].replace("\""," ")+ "\" ,\""  +row[ "homepage" ].replace("\""," ")+ "\" ,\"https://image.tmdb.org/t/p/original"  +row[ "poster_path" ].replace("\""," ")+ "\" ,\""  +row[ "popularity" ].replace("\""," ")+ "\" ,\""  +row[ "vote_count"].replace("\""," ")+ "\" ,\""  +row[ "vote_average" ].replace("\""," ")+ "\" ,\""  +row[ "id"].replace("\""," ")+ "\" ,\""  +row[ "imdb_id"].replace("\""," ")+ "\"  ) "))
# #       print("\""+row[ "title" ].replace("\""," ")+ "\" ,\""  +row[ "genres" ].replace("\""," ")+ "\" ,\""  +((row[ "release_date" ]).split("-")[0]).replace("\""," ")+ "\" ,\""  +row[ "tagline" ].replace("\""," ")+ "\" ,\""  +row[ "overview" ].replace("\""," ")+ "\" ,\""  +row[ "revenue"].replace("\""," ")+ "\" ,\""  +row[ "original_language" ].replace("\""," ")+ "\" ,\""  +row[ "directors"].replace("\""," ")+ "\" ,\""  +row[ "cast" ].replace("\""," ")+ "\" ,\""  +row[ "runtime" ].replace("\""," ")+ "\" ,\""  +row[ "homepage" ].replace("\""," ")+ "\" ,\""  +row[ "poster_path" ].replace("\""," ")+ "\" ,\""  +row[ "popularity" ].replace("\""," ")+ "\" ,\""  +row[ "vote_count"].replace("\""," ")+ "\" ,\""  +row[ "vote_average" ].replace("\""," ")+ "\" ,\""  +row[ "id"].replace("\""," ")+ "\" ,\""  +row[ "imdb_id"].replace("\""," ")+ "\"  ) ")) 
#        conn.execute("commit")
#     print(i)   

# conn.execute(("SELECT * FROM Movies "))
# rows=conn.fetchall()
# print (rows)
# conn=mydb.cursor ()
# conn.execute("alter table Reviews add Disliked_Users mediumtext")

# with open("./#main.csv", 'r') as file:
 
#     csvreader = csv.DictReader(file)
#     i=0
# conn=mydb.cursor ()
# conn.execute("alter table Mov add Reviews mediumtext")
#     conn.execute("drop table Mov")
#     conn.execute("CREATE TABLE Mov(Movie_ID int AUTO_INCREMENT,Title mediumtext ,Genres mediumtext ,Release_Year varchar(100) default \"2000\",Tag_Line mediumtext ,Overview mediumtext ,Revenue mediumtext ,Language varchar(100) default \"en\",Director mediumtext ,Actors mediumtext ,Runtime varchar(100) default \"0\",Age_certificate varchar(100) default \"U\",Homepage mediumtext ,Posters mediumtext ,Popularity varchar(100) default \"0\",Vote_Count varchar(100) default \"0\",Rating varchar(100) default \"7\",TMDB_ID varchar(100),IMDB_ID varchar(100),PRIMARY KEY(Movie_ID) )")
#     for row in csvreader:
#         i+=1
#         print(i) 
# #       conn.execute( " INSERT INTO Mov(Title,Genres,Release_Year,Tag_Line,Overview,Revenue,Language,Director,Actors,Runtime,Age_certificate,Homepage,Posters,Popularity,Vote_Count,Rating,TMDB_ID,IMDB_ID) VALUES (\""+row[ "Title" ].replace("\""," ")+ "\" ,\""  +row[ "Genres" ].replace("\""," ")+ "\" ,\""  +row[ "Release Year" ].replace("\""," ")+ "\" ,\""  +row[ "Tag Line" ].replace("\""," ")+ "\" ,\""  +row[ "Overview" ].replace("\""," ")+ "\" ,\""  +row[ "Revenue"].replace("\""," ")+ "\" ,\""  +row[ "Language" ].replace("\""," ")+ "\" ,\""  +row[ "Director"].replace("\""," ")+ "\" ,\""  +row[ "Actors" ].replace("\""," ")+ "\" ,\""  +row[ "Runtime" ].replace("\""," ")+ "\" ,\""  +row[ "Age Certificate"].replace("\""," ")+ "\" ,\""  +row[ "Homepage" ].replace("\""," ")+ "\" ,\""  +row[ "Poster" ].replace("\""," ")+ "\" ,\""  +row[ "Popularity" ].replace("\""," ")+ "\" ,\""  +row[ "Vote Count"].replace("\""," ")+ "\" ,\""  +row[ "Rating" ].replace("\""," ")+ "\" ,\""  +row[ "TMDB ID"].replace("\""," ")+ "\" ,\""  +row[ "IMDB ID"].replace("\""," ")+ "\" " ) 
#         conn.execute((" INSERT INTO Mov(Title,Genres,Release_Year,Tag_Line,Overview,Revenue,Language,Director,Actors,Runtime,Homepage,Posters,Popularity,Vote_Count,Rating,TMDB_ID,IMDB_ID) VALUES (\""+row[ "title" ].replace("\""," ")+ "\" ,\""  +row[ "genres" ].replace("\""," ")+ "\" ,\""  +((row[ "release_date" ]).split("-")[0]).replace("\""," ")+ "\" ,\""  +row[ "tagline" ].replace("\""," ")+ "\" ,\""  +row[ "overview" ].replace("\""," ")+ "\" ,\""  +row[ "revenue"].replace("\""," ")+ "\" ,\""  +row[ "original_language" ].replace("\""," ")+ "\" ,\""  +row[ "directors"].replace("\""," ")+ "\" ,\""  +row[ "cast" ].replace("\""," ")+ "\" ,\""  +row[ "runtime" ].replace("\""," ")+ "\" ,\""  +row[ "homepage" ].replace("\""," ")+ "\" ,\"https://image.tmdb.org/t/p/original"  +row[ "poster_path" ].replace("\""," ")+ "\" ,\""  +row[ "popularity" ].replace("\""," ")+ "\" ,\""  +row[ "vote_count"].replace("\""," ")+ "\" ,\""  +row[ "vote_average" ].replace("\""," ")+ "\" ,\""  +row[ "id"].replace("\""," ")+ "\" ,\""  +row[ "imdb_id"].replace("\""," ")+ "\"  ) "))
#         conn.execute("commit")
#     print(i)   
