import mysql.connector
from datetime import date
from ML.ml import ML
ml=ML()
mydb= mysql.connector.connect(
        host= "localhost",
        user="root",
        password="my-secret-password",
        auth_plugin='mysql_native_password',
        database="photons"
        )
conn=mydb.cursor ()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def movie_details_full(Movie_ID):
#     with engine.connect() as conn:
         print(Movie_ID)
         conn.execute("SELECT * FROM Mov1 WHERE Movie_ID ="+str(Movie_ID))
         row=conn.fetchall()
         return list(row[0])
    

def movies_with_filters(number_of_movies, genre,released_after,rated_more_than,language):
#      with engine.connect() as conn:
          print ("select Movie_ID,Posters from Mov1 where Release_Year >= \""+released_after+"\" and Rating > \""+rated_more_than+"\"  and Language=\""+language+"\" order by Popularity desc limit "+str(number_of_movies) )

          rows =conn.execute("select Movie_ID,Posters from Mov1 where Release_Year >= \""+released_after+"\" and Rating > \""+rated_more_than+"\"  AND Genres like \"%"+genre+"%\" AND Language=\""+language+"\" order by Popularity desc limit "+str(number_of_movies) )
          rows=conn.fetchall()
          return rows
    
# def related(movie_id):
#         return ml.related_to_movie(movie_id)

def movies(number_of_movies, genre,released_after,rated_more_than,language,search):
#      with engine.connect() as conn:
        rows =conn.execute("select Movie_ID,Posters from Mov1 where Release_Year >= \""+released_after+"\" AND Rating > \""+rated_more_than+"\" AND Title like \"%"+search+"%\" AND Genres like \"%"+genre+"%\" AND Language=\""+language+"\" order by Rating desc LIMIT "+str(number_of_movies) )
        rows=conn.fetchall()
        if(len(rows)==0):
                result=ml.recommend_by_string(search)
                rows2=[]
                for i in range(number_of_movies-len(rows)):
                        row3=conn.execute("select Movie_ID,Posters from Mov1 where Movie_ID="+str(result[i]))
                        row3=conn.fetchall()
                        rows2.append(row3[0])
                rows=rows+rows2
                return (rows,1)
        return (rows,0)

def movies_by_popularity(number_of_movies):
          conn.execute(("SELECT Movie_ID,Posters FROM Mov1 ORDER BY Popularity DESC LIMIT "+str(number_of_movies)))
          rows=conn.fetchall()
          return rows
def get_bookmark_posters(movie_id):
          conn.execute("SELECT Movie_ID,Posters FROM Mov1 where Movie_ID="+str(movie_id))
          rows=conn.fetchall()
          return rows        

def add_review(movie_id,user_id,title,review):
#       with engine.connect() as conn:
        sentiment=1
        conn.execute("INSERT INTO Reviews (Movie_ID,User_ID,Review,Likes,Dislikes,Title,Sentiment) VALUES (\""+movie_id+"\",\""+user_id+"\",\""+review+"\",0,0,\""+title+"\","+str(sentiment)+")")
        conn.execute("commit")
        conn.execute(("SELECT Review_ID FROM Reviews WHERE Movie_ID = \""+movie_id+"\" AND User_ID = \""+user_id+"\" AND Review = \""+review+"\""))
        row=conn.fetchall()
        row=str(row[0][0])
        conn.execute(("select Reviews from Mov1 where Movie_ID="+movie_id+""))
        temp=conn.fetchall()
        temp=str(list(temp)[0][0])
        conn.execute(("UPDATE Mov1 SET Reviews = \""+ temp+"|"+row +"\" WHERE Movie_ID ="+movie_id))
        conn.execute("commit")
        conn.execute(("select Reviews from Users1 where User_ID="+user_id))
        temp=conn.fetchall()
        temp=str(list(temp)[0][0])
        conn.execute(("UPDATE Users1 SET Reviews = \""+ temp+"|"+row +"\" WHERE User_ID ="+user_id+""))
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
          conn.execute(("INSERT INTO Users1 (Email,User_Name,Password,Name) VALUES (\""+email+"\",\""+user_name+"\",\""+password.hexdigest()+"\",\""+name+"\")"))
          conn.execute("commit")
          conn.execute(("SELECT User_ID FROM Users1 WHERE Email =\""+email+"\" AND user_name = \""+user_name+"\" AND password = \""+password.hexdigest()+"\""))
          row=conn.fetchall()
          return list(list(row)[0])[0]

def user_details_with_ID(user_id):

          conn.execute(("SELECT * FROM Users1 WHERE User_ID = "+user_id))
          row=conn.fetchall()
          return list(list((row)[0]))

# def update_profile_pic
# updates string name of pic file

def update_user_name(user_id,user_name):
#      with engine.connect() as conn:
          conn.execute(("UPDATE Users1 SET Name = \""+user_name+"\" WHERE User_ID =\""+user_id+"\""))
          conn.execute("commit")
def update_about(user_id,about):
#      with engine.connect() as conn:
         conn.execute(("UPDATE Users1 SET About = \""+about+"\" WHERE User_ID =\""+user_id+"\""))
         conn.execute("commit")
def update_user_password(user_id,password):
#      with engine.connect() as conn:
          conn.execute(("UPDATE Users1 SET Password = \""+password.hexdigest()+"\" WHERE User_ID = "+"\""+user_id+"\""))
          conn.execute("commit")
def update_user_email(user_id,email):
#      with engine.connect() as conn:
          conn.execute(("UPDATE Users1 SET Email = \""+email+"\" WHERE User_ID = "+"\""+user_id+"\""))
          conn.execute("commit")
def exists_user(user_name):
#      with engine.connect() as conn:
         conn.execute(("select * from Users1 where User_Name = \""+user_name+"\""))
         temp=conn.fetchall()
         if(len(temp))==0:
             return False
         else:
             return True

def add_bookmark(user_id,movie_id):
         conn.execute ("select Bookmarks from Users1 where User_ID="+user_id)
         temp=conn.fetchall()[0][0]
         temp=temp+"|"+movie_id
         lis=temp.split("|")
         lis = list(dict.fromkeys(lis)) # to remove redundency
         temp=""
         for i in lis:
                 temp=temp+"|"+i
         conn.execute(("UPDATE Users1 SET Bookmarks= \""+temp+"\" WHERE User_ID="+user_id))
         conn.execute("commit")

def get_bookmarks(userid):
        conn.execute("select Bookmarks from Users1 where User_ID="+userid)
        temp=conn.fetchall()[0][0]
        l=temp.split("|")
        return l

def remove_bookmarks(userid,movie_id):
        conn.execute("select Bookmarks from Users1 where User_ID= "+userid)
        temp=conn.fetchall()[0][0]
        l=temp.split("|")
        l=l.remove(movie_id)
        if len(l)==0:
                conn.execute("update Users1 set Bookmarks= \"\"")
                conn.execute("commit")
                return
        str=l[0]
        l=l.pop(0)
        for i in l :
                str=str+"|"+i
        conn.execute("update Users1 set Bookmarks= \""+str+"\"")
        conn.execute("commit")

def add_like_review(postid,userid, movieid):
        conn.execute("select Liked_Users from Reviews where Review_ID="+postid)
        temp=conn.fetchall()[0][0]
        l=[]
        if(temp != None):
                l=temp.split("|")
        conn.execute("select Likes from Reviews where Review_ID ="+postid)
        num=conn.fetchall()[0][0]
        conn.execute("select Dislikes from Reviews where Review_ID ="+postid)
        dislikes=conn.fetchall()[0][0]

        if userid in l: 
                return (int(num),int(dislikes))
        else:
                conn.execute("update Reviews set Liked_Users =\""+num+"|"+userid+"\" where Review_ID ="+postid)
                conn.execute("commit")
                conn.execute("select Likes from Reviews where Review_ID ="+postid)
                temp=conn.fetchall()[0][0]
                conn.execute("update Reviews set Likes = \""+str(int(num)+1)+"\" where Review_ID ="+postid)
                conn.execute("commit")
                return (int(num)+1,int(dislikes))


def add_unlike_review(postid,userid, movieid):
        conn.execute("select Disliked_Users from Reviews where Review_ID="+postid)
        temp=conn.fetchall()[0][0]
        l=[]
        if(temp != None):
                l=temp.split("|")
        conn.execute("select Likes from Reviews where Review_ID ="+postid)
        likes=conn.fetchall()[0][0]     
        conn.execute("select Dislikes from Reviews where Review_ID ="+postid)
        num=conn.fetchall()[0][0]
        if userid in l: 
                return (int(likes),int(num))
        else:
                conn.execute("update Reviews set Disliked_Users =\""+num+"|"+userid+"\" where Review_ID ="+postid)
                conn.execute("commit")
                conn.execute("select Dislikes from Reviews where Review_ID ="+postid)
                temp=conn.fetchall()[0][0]
                conn.execute("update Reviews set Dislikes = \""+str(int(num)+1)+"\" where Review_ID ="+postid)
                conn.execute("commit")
                return (int(likes),int(num)+1)


def add_vector (user_id,lis):
        str=""
        for i in lis:
                lis=lis.append("|"+str(i))
        conn.execute ("update Users1 set Vector= \""+str+"\" where User_ID =\""+user_id+"\"")
        conn.execute("commit")
def fetch_vector (user_id):
        conn.execute ("select Vector from Users1 where User_ID ="+user_id)
        str=conn.fetchall()[0][0] 
        if str=="":
                return [0 for i in range (2500)]
        lis=str.split("|")
        lis1=[]
        for i in lis:
               lis1.append(int(i))
        return lis1

def Top_movies_by_genres (genre):
        lis=genre.split("|")
        if len(lis)==0:
         lis=["Action","Thriller"]
        if len(lis)==1:
         lis=lis.append("Action")
        if lis==None:
         lis=["Action","Thriller"]
        print(lis)
        conn.execute("select Movie_ID,Posters from Mov1 where Genres like \"%"+lis[0]+"%\" and Genres like \"%"+lis[1]+"%\" order by Popularity desc limit "+str(5))
        rows=conn.fetchall()
        return rows
# def find_user(user_name):
#      with engine.connect() as conn:
#          row=conn.execute(text("SELECT User_ID FROM Users1 WHERE User_Name = \""+user_name+"\""))
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
#           temp=conn.execute(text("select Interactions from Users1 where User_ID="+user_id+""))
#           temp=str(list(temp)[0][0])
#           conn.execute(text("UPDATE Users1 SET Interactions =\""+temp+"|"+str(review_id)+"\" WHERE User_ID = "+user_id))

# def remove_like_review(review_id,user_id):
#      with engine.connect() as conn:
#          temp=conn.execute(text("select Likes from Reviews where Review_ID="+user_id))
#          temp=str(list(temp)[0][0])
#          conn.execute(text("UPDATE Reviews SET Likes = \""+ str(int(temp)-1) +"\" WHERE User_ID ="+user_id+""))
#          temp=conn.execute(text("select Interactions from Users1 where User_ID="+user_id+""))
#          temp=str(list(temp)[0][0])
#          temp=temp.replace("|"+review_id,"")
#          conn.execute(text("UPDATE Users1 SET Interactions =\""+temp+"\" WHERE User_ID = "+user_id))

# def add_dislike_review(review_id,user_id):
#       with engine.connect() as conn:
#           temp=conn.execute(text("select Dislikes from Reviews where Review_ID="+user_id))
#           temp=str(list(temp)[0][0])
#           conn.execute(text("UPDATE Reviews SET Dislikes = \""+ str(int(temp)+1) +"\" WHERE User_ID ="+user_id+""))
#         #   conn.execute(text("UPDATE Reviews SET likes = likes + 1 WHERE id = %s", [review_id]))
#           temp=conn.execute(text("select Interactions from Users1 where User_ID="+user_id+""))
#           temp=str(list(temp)[0][0])
#           conn.execute(text("UPDATE Users1 SET Interactions =\""+temp+"|"+str(review_id)+"\" WHERE User_ID = "+user_id))

# def remove_dislike_review(review_id,user_id):
#      with engine.connect() as conn:
#          temp=conn.execute(text("select Dislikes from Reviews where Review_ID="+user_id))
#          temp=str(list(temp)[0][0])
#          conn.execute(text("UPDATE Reviews SET Dislikes = \""+ str(int(temp)-1) +"\" WHERE User_ID ="+user_id+""))
#          temp=conn.execute(text("select Interactions from Users1 where User_ID="+user_id+""))
#          temp=str(list(temp)[0][0])
#          temp=temp.replace("|"+review_id,"")
#          conn.execute(text("UPDATE Users1 SET Interactions =\""+temp+"\" WHERE User_ID = "+user_id))


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

#
# conn.execute(("DROP TABLE Reviews"))
 #conn.execute("commit")
# conn=mydb.cursor ()
# conn.execute(("CREATE TABLE Users1 (User_ID int AUTO_INCREMENT,Reviews varchar(5000) default \"\",Email varchar(200),Mobile varchar(100),User_Name varchar(100),Password varchar(100),Name varchar(200),Interactions varchar(1000) default \"\",Bookmarks varchar(1000) default \"\",Friends varchar(3000) default \"\",About varchar(2000),PRIMARY KEY(User_ID))"))
# conn.execute("commit")
#conn.execute(("CREATE TABLE Reviews (Review_ID int AUTO_INCREMENT,Movie_ID varchar(100),User_ID varchar(100),Review varchar(10000),Likes varchar(100) default \"0\",Dislikes varchar(100) default \"0\",Date varchar(100) default=\"25/04/2023\",PRIMARY KEY(Review_ID))"))
# conn.execute("alter table Reviews add Title mediumtext")
# # with engine.connect() as conn:
# #         conn.execute(text("INSERT INTO Users1 (Email,Mobile,User_Name,Password,Name) VALUES (\"cs1210571@cse.iitd.ac.in\",\"9778521795\",\"Pumwakintolly\",\"atul\",\"Adithya Bijoy\")"))

# # #add_review("1","1","This is the best movie ever","9.5")
# #with engine.connect() as conn:
# #     conn.execute("alter table Users1 drop About")
# #         conn.execute(text("update Movies set Posters=\"https://images.app.goo.gl/7pSniDf3sURmvH61A\" where Title= \"WALL.E\"" ))
# #    conn.execute(text("alter table Users1 add About mediumtext default \"I love this website\""))
# #add_user("cs1210123$cse.iitd.ac.in","Aditya","anshik","9778521795","Aditya Gupta")
# #update_user_name("2","Pumwkintolly")
# # with engine.connect() as conn:
# #     conn.execute(text("delete from Users1 where Name=\"Aditya Gupta\""))
# #print(movies_with_filters_and_search(12,"|","0","0","en","A"))
# #print(movie_details_short("12"))
# #print(add_user("cs1210571@cse.iitd.ac.in","Pumwakintlly","Anish","Adithya Bijoy"))
# #print(user_details_with_ID("1"))
#conn.execute("alter table Movies drop Bookmarks")
#conn.execute("alter table Users1 add Bookmarks mediumtext")
# conn.execute("select * from Movies")
# obj=conn.fetchall()
# print(obj)
# add_bookmark("1","1")
# movie_details_full("1234")

