import mysql.connector

mydb= mysql.connector.connect(
        host= "localhost",
        user="root",
        password="my-secret-password",
        auth_plugin='mysql_native_password',
        database="photons"
        )
conn=mydb.cursor ()

def movie_details_full(Movie_ID):
#     with engine.connect() as conn:
         print(Movie_ID)
         conn.execute("SELECT * FROM Movies WHERE Movie_ID ="+str(Movie_ID))
         row=conn.fetchall()
         return list(row[0])
    

def movies_with_filters_and_search(number_of_movies, genre,released_after,rated_more_than,language,search):
#      with engine.connect() as conn:
          rows =conn.execute("SELECT Movie_ID,Posters FROM Movies WHERE Release_Year >= \""+released_after+"\" AND Rating > \""+rated_more_than+"\" AND Title like \""+search+"%\" LIMIT "+str(number_of_movies) )
          rows=conn.fetchall()
          return rows
    
def movies_by_popularity(number_of_movies):
          conn.execute(("SELECT Movie_ID,Posters FROM Movies ORDER BY Vote_Count DESC LIMIT "+str(number_of_movies)))
          rows=conn.fetchall()
          return rows
def get_bookmark_posters(movie_id):
          conn.execute("SELECT Movie_ID,Posters FROM Movies where Movie_ID="+str(movie_id))
          rows=conn.fetchall()
          return rows        

def add_review(movie_id,user_id,title,review):
#       with engine.connect() as conn:
        conn.execute("INSERT INTO Reviews (Movie_ID,User_ID,Review,Likes,Dislikes,Title) VALUES (\""+movie_id+"\",\""+user_id+"\",\""+review+"\",0,0,\""+title+"\")")
        conn.execute("commit")
        conn.execute(("SELECT Review_ID FROM Reviews WHERE Movie_ID = \""+movie_id+"\" AND User_ID = \""+user_id+"\" AND Review = \""+review+"\""))
        row=conn.fetchall()
        row=str(row[0][0])
        conn.execute(("select Reviews from Movies where Movie_ID="+movie_id+""))
        temp=conn.fetchall()
        temp=str(list(temp)[0][0])
        conn.execute(("UPDATE Movies SET Reviews = \""+ temp+"|"+row +"\" WHERE Movie_ID ="+movie_id))
        conn.execute("commit")
        conn.execute(("select Reviews from Users where User_ID="+user_id))
        temp=conn.fetchall()
        temp=str(list(temp)[0][0])
        conn.execute(("UPDATE Users SET Reviews = \""+ temp+"|"+row +"\" WHERE User_ID ="+user_id+""))
        conn.execute("commit")
        # old_rating = movie_details_full(movie_id)[-4]# replace with rating index
        # number_of_votes = movie_details_full(movie_id)[-5]# replace with number of votes index
        # new_rating = (float(old_rating)*float(number_of_votes) + float(rating)*2)/(float(number_of_votes)+2)
        # change_rating(movie_id,str(new_rating))
        # conn.execute(text("UPDATE Movies SET Vote_Count =\""+str(int(number_of_votes)+1)+"\" WHERE Movie_ID = "+movie_id))


def get_reviews(movie_id):

          conn.execute(("select * from Reviews where Movie_ID ="+movie_id+" order by Likes desc limit 5"))
          lis=conn.fetchall()
          for i in range (len(lis)):
              templ=list(lis[i])
              templ.append(user_details_with_ID(str(lis[i][2]))[4])
              lis[i]=templ
          return lis
def get_reviews_by_user(user_id):
          conn.execute(("select * from Reviews where User_ID ="+str(user_id)+" order by Likes desc limit 5"))
          lis=conn.fetchall()
          for i in range (len(lis)):
              templ=list(lis[i])
              templ.append(user_details_with_ID(str(lis[i][2]))[4])
              lis[i]=templ
          return lis

def add_user(email,user_name,password,name):
#       with engine.connect() as conn:
          conn.execute(("INSERT INTO Users (Email,User_Name,Password,Name) VALUES (\""+email+"\",\""+user_name+"\",\""+password+"\",\""+name+"\")"))
          conn.execute("commit")
          conn.execute(("SELECT User_ID FROM Users WHERE Email =\""+email+"\" AND user_name = \""+user_name+"\" AND password = \""+password+"\""))
          row=conn.fetchall()
          return list(list(row)[0])[0]

def user_details_with_ID(user_id):

          conn.execute(("SELECT * FROM Users WHERE User_ID = "+user_id))
          row=conn.fetchall()
          return list(list((row)[0]))

        

def update_user_name(user_id,user_name):
#      with engine.connect() as conn:
          conn.execute(("UPDATE Users SET Name = \""+user_name+"\" WHERE User_ID =\""+user_id+"\""))
          conn.execute("commit")
def update_about(user_id,about):
#      with engine.connect() as conn:
         conn.execute(("UPDATE Users SET About = \""+about+"\" WHERE User_ID =\""+user_id+"\""))
         conn.execute("commit")
def update_user_password(user_id,password):
#      with engine.connect() as conn:
          conn.execute(("UPDATE Users SET Password = \""+password+"\" WHERE User_ID = "+"\""+user_id+"\""))
          conn.execute("commit")
def update_user_email(user_id,email):
#      with engine.connect() as conn:
          conn.execute(("UPDATE Users SET Email = \""+email+"\" WHERE User_ID = "+"\""+user_id+"\""))
          conn.execute("commit")
def exists_user(user_name):
#      with engine.connect() as conn:
         conn.execute(("select * from Users where User_Name = \""+user_name+"\""))
         temp=conn.fetchall()
         if(len(temp))==0:
             return False
         else:
             return True

def add_bookmark(user_id,movie_id):
         conn.execute ("select Bookmarks from Users where User_ID="+user_id)
         temp=conn.fetchall()[0][0]
         temp=temp+"|"+movie_id
         lis=temp.split("|")
         lis = list(dict.fromkeys(lis)) # to remove redundency
         temp=""
         for i in lis:
                 temp=temp+"|"+i
         conn.execute(("UPDATE Users SET Bookmarks= \""+temp+"\" WHERE User_ID="+user_id))
         conn.execute("commit")

def get_bookmarks(userid):
        conn.execute("select Bookmarks from Users where User_ID="+userid)
        temp=conn.fetchall()[0][0]
        l=temp.split("|")
        return l


# def find_user(user_name):
#      with engine.connect() as conn:
#          row=conn.execute(text("SELECT User_ID FROM Users WHERE User_Name = \""+user_name+"\""))
#          try:
#             return int(list(list(row)[0])[0])
#          except:
#              return -1

# # def remove_bookmark(user_id,movie_id):
# #     with engine.connect() as conn:
# #         conn.execute(text("UPDATE users SET bookmarks = bookmarks.replace(%s,'') WHERE id = %s", ['|'+ str(movie_id),user_id]))
# #         ()

# # def add_friend(user_id,friend_id):
# #     with engine.connect() as conn:
# #         conn.execute(text("UPDATE users SET friends = friends.concat(%s) WHERE id = %s", ['|'+ str(friend_id),user_id]))
# #         ()
# #         conn.execute(text("UPDATE users SET friends = friends.concat(%s) WHERE id = %s", ['|'+ str(user_id),friend_id]))
# #         ()

# # def remove_friend(user_id,friend_id):
# #     with engine.connect() as conn:
# #         conn.execute(text("UPDATE users SET friends = friends.replace(%s,'') WHERE id = %s", ['|'+ str(friend_id),user_id]))
# #         ()
# #         conn.execute(text("UPDATE users SET friends = friends.replace(%s,'') WHERE id = %s", ['|'+ str(user_id),friend_id]))
# #         ()

# # def get_friends(user_id):
# #     with engine.connect() as conn:
# #         conn.execute(text("SELECT friends FROM users WHERE id = %s", [user_id]))
# #         row = conn.fetchone()
# #         return row[0]
    
# # def get_bookmarks(user_id):
# #     with engine.connect() as conn:
# #         conn.execute(text("SELECT bookmarks FROM users WHERE id = %s", [user_id]))
# #         row = conn.fetchone()
# #         return row[0]
    
# # def get_interactions(user_id):
# #     with engine.connect() as conn:
# #         conn.execute(text("SELECT interactions FROM users WHERE id = %s", [user_id]))
# #         row = conn.fetchone()
# #         return row[0]
    
# def movie_details_short(movie_id):
#      with engine.connect() as conn:
#          row=conn.execute(text("SELECT Title,Release_Year,Genres,Rating FROM Movies WHERE Movie_ID = "+str(movie_id)))
         
#          return list(list(row)[0])

# def movie_poster(movie_id):
#      with engine.connect() as conn:
#          row=conn.execute(text("SELECT Poster FROM Movies WHERE Movie_ID = "+str(movie_id)))
#          return list(row)[0]

# def change_rating(Movie_ID,Rating):
#      with engine.connect() as conn:
#          conn.execute(text("UPDATE Movies SET Rating = \""+str(Rating)+"\" WHERE Movie_ID ="+str(Movie_ID)))

#def get_review(review_id):
#      with engine.connect() as conn:
#         row=conn.execute(text("SELECT * FROM Reviews WHERE Review_ID = "+review_id))
#         return list(list(row)[0])


# def get_reviews_by_user(movie_id,user_id):
#      with engine.connect() as conn:
#          row =conn.execute(text("SELECT Review_ID FROM Reviews WHERE Movie_ID ="+movie_id+" and User_ID= "+user_id))
#          return list(list(row)[0])[0]
    
# def add_like_review(review_id,user_id):
#       with engine.connect() as conn:
#           temp=conn.execute(text("select Likes from Reviews where Review_ID="+user_id))
#           temp=str(list(temp)[0][0])
#           conn.execute(text("UPDATE Reviews SET Likes = \""+ str(int(temp)+1) +"\" WHERE User_ID ="+user_id+""))
#         #   conn.execute(text("UPDATE Reviews SET likes = likes + 1 WHERE id = %s", [review_id]))
#           temp=conn.execute(text("select Interactions from Users where User_ID="+user_id+""))
#           temp=str(list(temp)[0][0])
#           conn.execute(text("UPDATE Users SET Interactions =\""+temp+"|"+str(review_id)+"\" WHERE User_ID = "+user_id))

# def remove_like_review(review_id,user_id):
#      with engine.connect() as conn:
#          temp=conn.execute(text("select Likes from Reviews where Review_ID="+user_id))
#          temp=str(list(temp)[0][0])
#          conn.execute(text("UPDATE Reviews SET Likes = \""+ str(int(temp)-1) +"\" WHERE User_ID ="+user_id+""))
#          temp=conn.execute(text("select Interactions from Users where User_ID="+user_id+""))
#          temp=str(list(temp)[0][0])
#          temp=temp.replace("|"+review_id,"")
#          conn.execute(text("UPDATE Users SET Interactions =\""+temp+"\" WHERE User_ID = "+user_id))

# def add_dislike_review(review_id,user_id):
#       with engine.connect() as conn:
#           temp=conn.execute(text("select Dislikes from Reviews where Review_ID="+user_id))
#           temp=str(list(temp)[0][0])
#           conn.execute(text("UPDATE Reviews SET Dislikes = \""+ str(int(temp)+1) +"\" WHERE User_ID ="+user_id+""))
#         #   conn.execute(text("UPDATE Reviews SET likes = likes + 1 WHERE id = %s", [review_id]))
#           temp=conn.execute(text("select Interactions from Users where User_ID="+user_id+""))
#           temp=str(list(temp)[0][0])
#           conn.execute(text("UPDATE Users SET Interactions =\""+temp+"|"+str(review_id)+"\" WHERE User_ID = "+user_id))

# def remove_dislike_review(review_id,user_id):
#      with engine.connect() as conn:
#          temp=conn.execute(text("select Dislikes from Reviews where Review_ID="+user_id))
#          temp=str(list(temp)[0][0])
#          conn.execute(text("UPDATE Reviews SET Dislikes = \""+ str(int(temp)-1) +"\" WHERE User_ID ="+user_id+""))
#          temp=conn.execute(text("select Interactions from Users where User_ID="+user_id+""))
#          temp=str(list(temp)[0][0])
#          temp=temp.replace("|"+review_id,"")
#          conn.execute(text("UPDATE Users SET Interactions =\""+temp+"\" WHERE User_ID = "+user_id))


# # def delete_review(review_id):  // I will implement this only if I have time
# #      with engine.connect() as conn:
# #          conn.execute(text("DELETE FROM Reviews WHERE Review_ID ="+review_id))
# #          conn.execute(text(""))
# #          conn.execute(text("UPDATE Movies SET reviews = reviews.replace(%s,'') WHERE reviews like %s", ['|'+ str(review_id),review_id]))
# #          conn.execute(text("UPDATE users SET reviews = reviews.replace(%s,'') WHERE reviews like %s", ['|'+ str(review_id),review_id]))

# # def add_post(user_id,title,post,tags,movie_id):
# #     with engine.connect() as conn:
# #         conn.execute(text("INSERT INTO posts (user_id,title,post,tags,likes,dislikes,movie_id) VALUES (%s,%s,%s,%s,0,0,%s)", [user_id,title,post,tags,movie_id]))
# #         ()
# #         conn.execute(text("SELECT id FROM posts WHERE user_id = %s AND title = %s AND post = %s AND tags = %s AND movie_id = %s", [user_id,title,post,tags,movie_id]))
# #         row = conn.fetchone()
# #         conn.execute(text("UPDATE users SET posts = posts.concat(%s) WHERE id = %s", ['|'+str(row[0]),user_id]))
# #         ()

# # def get_post_full(post_id):
# #     with engine.connect() as conn:
# #         conn.execute(text("SELECT * FROM posts WHERE id = %s", [post_id]))
# #         row = conn.fetchone()
# #         return row

# # def get_post_short(post_id):
# #     with engine.connect() as conn:
# #         conn.execute(text("SELECT title,post,user_id FROM posts WHERE id = %s", [post_id]))
# #         row = conn.fetchone()
# #         return row

# # def get_posts_by_user(user_id):
# #     with engine.connect() as conn:
# #         conn.execute(text("SELECT id FROM posts WHERE user_id = %s", [user_id]))
# #         rows = conn.fetchall()
# #         return rows
    
# # def get_posts_by_likes(number_of_posts):
# #     with engine.connect() as conn:
# #         conn.execute(text("SELECT id FROM posts ORDER BY likes DESC LIMIT %s", [number_of_posts]))
# #         rows = conn.fetchall()
# #         return rows
    
# # def get_posts_by_relevance(number_of_posts):
# #     with engine.connect() as conn:
# #         conn.execute(text("SELECT id FROM posts ORDER BY id DESC, likes LIMIT %s", [number_of_posts]))
# #         rows = conn.fetchall()
# #         return rows

# # def add_like_post(post_id,user_id):
# #     with engine.connect() as conn:
# #         conn.execute(text("UPDATE posts SET likes = likes + 1 WHERE id = %s", [post_id]))
# #         ()
# #         conn.execute(text("UPDATE users SET interactions = interactions.concat(%s) WHERE id = %s", ['|'+str(post_id),user_id]))
# #         ()

# # def remove_like_post(post_id,user_id):
# #     with engine.connect() as conn:
# #         conn.execute(text("UPDATE posts SET likes = likes - 1 WHERE id = %s", [post_id]))
# #         ()
# #         conn.execute(text("UPDATE users SET interactions = interactions.replace(%s,'') WHERE id = %s", [post_id,user_id]))
# #         ()

# # def remove_dislike_post(post_id,user_id):
# #     with engine.connect() as conn:
# #         conn.execute(text("UPDATE posts SET dislikes = dislikes - 1 WHERE id = %s", [post_id]))
# #         ()
# #         conn.execute(text("UPDATE users SET interactions = interactions.replace(%s,'') WHERE id = %s", ['|'+ str(post_id),user_id]))
# #         ()

# # def add_dislike_post(post_id,user_id):
# #     with engine.connect() as conn:
# #         conn.execute(text("UPDATE posts SET dislikes = dislikes + 1 WHERE id = %s", [post_id]))
# #         ()
# #         conn.execute(text("UPDATE users SET interactions = interactions.concat(%s) WHERE id = %s", ['|'+ str(post_id),user_id]))
# #         ()

# # def delete_post(post_id):
# #     with engine.connect() as conn:
# #         conn.execute(text("DELETE FROM posts WHERE id = %s", [post_id]))
# #         ()
# #         conn.execute(text("UPDATE users SET posts = posts.replace(%s,'') WHERE posts like %s", ['|'+ str(post_id),post_id]))
# #         ()

# # def get_post_by_genre(genre,number_of_posts):
# #     with engine.connect() as conn:
# #         conn.execute(text("SELECT id FROM posts WHERE tags like %s ORDER BY id DESC, likes LIMIT %s", [genre,number_of_posts]))
# #         rows = conn.fetchall()
# #         return rows


# # def update_user_mobile(user_id,mobile):
# #     with engine.connect() as conn:
# #         conn.execute(text("UPDATE users SET mobile = %s WHERE id = %s", [mobile,user_id]))
# #         ()

# # def update_user_name(user_id,name):
# #     with engine.connect() as conn:
# #         conn.execute(text("UPDATE users SET name = %s WHERE id = %s", [name,user_id]))
# #         ()

# # def update_profile_picture(user_id,profile_picture):
# #     with engine.connect() as conn:
# #         conn.execute(text("UPDATE users SET profile_picture = %s WHERE id = %s", [profile_picture,user_id]))
# #         ()

# # def update_user_about(user_id,about):
# #     with engine.connect() as conn:
# #         conn.execute(text("UPDATE users SET about = %s WHERE id = %s", [about,user_id]))
# #         ()

# conn.execute(("DROP TABLE Users"))
# conn.execute("commit")
# conn.execute(("CREATE TABLE Users (User_ID int AUTO_INCREMENT,Reviews varchar(5000) default \"\",Email varchar(200),Mobile varchar(100),User_Name varchar(100),Password varchar(100),Name varchar(200),Interactions varchar(1000) default \"\",Bookmarks varchar(1000) default \"\",Friends varchar(3000) default \"\",About varchar(2000),PRIMARY KEY(User_ID))"))
# conn.execute("commit")
#conn.execute(("CREATE TABLE Reviews (Review_ID int AUTO_INCREMENT,Movie_ID varchar(100),User_ID varchar(100),Review varchar(10000),Likes varchar(100) default \"0\",Dislikes varchar(100) default \"0\",PRIMARY KEY(Review_ID))"))
# conn.execute("alter table Reviews add Title mediumtext")
# # with engine.connect() as conn:
# #         conn.execute(text("INSERT INTO Users (Email,Mobile,User_Name,Password,Name) VALUES (\"cs1210571@cse.iitd.ac.in\",\"9778521795\",\"Pumwakintolly\",\"atul\",\"Adithya Bijoy\")"))

# # #add_review("1","1","This is the best movie ever","9.5")
# #with engine.connect() as conn:
# #     conn.execute("alter table Users drop About")
# #         conn.execute(text("update Movies set Posters=\"https://images.app.goo.gl/7pSniDf3sURmvH61A\" where Title= \"WALL.E\"" ))
# #    conn.execute(text("alter table Users add About mediumtext default \"I love this website\""))
# #add_user("cs1210123$cse.iitd.ac.in","Aditya","anshik","9778521795","Aditya Gupta")
# #update_user_name("2","Pumwkintolly")
# # with engine.connect() as conn:
# #     conn.execute(text("delete from Users where Name=\"Aditya Gupta\""))
# #print(movies_with_filters_and_search(12,"|","0","0","en","A"))
# #print(movie_details_short("12"))
# #print(add_user("cs1210571@cse.iitd.ac.in","Pumwakintlly","Anish","Adithya Bijoy"))
# #print(user_details_with_ID("1"))
#conn.execute("alter table Movies drop Bookmarks")
#conn.execute("alter table Users add Bookmarks mediumtext")
# conn.execute("select * from Movies")
# obj=conn.fetchall()
# print(obj)
# add_bookmark("1","1")
# movie_details_full("1234")