from flask import Flask, request, session, redirect, url_for, render_template, flash
from flaskext.mysql import MySQL
import pymysql 
import functions

app = Flask(__name__) #referencing this file



@app.route('/')
def index():
    link=functions.movies_by_popularity(10)
    return render_template('index.html',link=link)

app.secret_key = 'cairocoders-ednalan'
 
mysql = MySQL()
   
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'my-secret-password'
app.config['MYSQL_DATABASE_DB'] = 'photons'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
 
# http://localhost:5000/pythonlogin/ - this will be the login page
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # Output message if something goes wrong...
        # Check if "username" and "password" POST requests exist (user submitted form)
        if 'User_Name' in request.form and 'Password' in request.form:
            # Create variables for easy access
            username = request.form['User_Name']
            password = request.form['Password']
            # Check if account exists using MySQL
            cursor.execute('SELECT * FROM Users WHERE User_Name = %s AND Password = %s', (username, password))
            # Fetch one record and return result
            account = cursor.fetchone()
        # If account exists in accounts table in out database
            if account:
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account['User_ID']
                session['username'] = account['User_Name']
                # Redirect to home page
                return redirect(url_for('index', link=functions.movies_by_popularity(10)))
            else:
                # Account doesnt exist or username/password incorrect
                flash('Incorrect username/password!')
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('index'))

@app.route('/friendsprofile')
def friendsprofile():
    return render_template('friendsprofile.html')

@app.route('/strangerprofile')
def strangerprofile():
    return render_template('strangerprofile.html')

@app.route('/movie')
def movie():
    movie_id = request.args.get('movie_id')
    list=functions.movie_details_full(movie_id)
    return render_template('movie_page.html',movie_id=list[0],movie=list[1],genres=list[2],year=list[3],tag_line=list[4],overview=list[5],revenue=list[6],language=list[7],director=list[8],actors=list[9],runtime=list[10],age=list[11],homepage=list[12],poster=list[-7],popularity=list[13],rating=list[15],review=functions.get_reviews(movie_id),link=functions.movies_by_popularity(10),stars=int(float(list[-4])/2))

@app.route('/add_bookmark',methods=['POST','GET'])
def add_bookmark():
    if request.method=='POST':
        movie_id=request.form['movie_id']
        functions.add_bookmark(str(session['id']),movie_id)
        list=functions.movie_details_full(movie_id)
        return render_template('movie_page.html',movie_id=list[0],movie=list[1],genres=list[2],year=list[3],tag_line=list[4],overview=list[5],revenue=list[6],language=list[7],director=list[8],actors=list[9],runtime=list[10],age=list[11],homepage=list[12],poster=list[-7],popularity=list[13],rating=list[15],review=functions.get_reviews(movie_id),link=functions.movies_by_popularity(10),stars=int(float(list[-4])/2))

@app.route('/bookmarks')
def bookmarks():
    user_bookmarks = functions.get_bookmarks(str(session['id']))
    user_bookmarks.pop(0)
    print(user_bookmarks)
    l1=[]
    for i in user_bookmarks:
        l1.append(functions.get_bookmark_posters(int(i)))
    print(l1)
    return render_template('bookmarks.html', list=l1)
    
@app.route('/profile',methods=['POST','GET'])
def profile():
    if request.method == 'GET':
        user_details=functions.user_details_with_ID(str(session['id']))
        first_name=user_details[-5].split()[0]
        last_name=user_details[-5].split()[-1]
        email=user_details[2]
        password=user_details[5]
        user_name=user_details[4]
        about=user_details[-1]
        return render_template('profile.html',first_name=first_name,user_name=user_name,sur_name=last_name,email=email,password=password,about=about,review=functions.get_reviews_by_user(session['id']))
    if request.method=='POST':
        for i in request.form.keys():print(i)
        user_details=functions.user_details_with_ID(str(session['id']))
        first_name=request.form['First_Name']
        last_name=request.form['Sur_Name']
        functions.update_user_name(str(session['id']),first_name+" "+last_name)
        email=request.form['Email']
        functions.update_user_email(str(session['id']),email)
        password=request.form['Password']
        functions.update_user_password(str(session['id']),password)
        user_name=user_details[4]
        about=request.form['About']
        functions.update_about(str(session['id']),about)
        return render_template('profile.html',first_name=first_name,user_name=user_name,sur_name=last_name,email=email,password=password,about=about,review=functions.get_reviews_by_user(session['id']))
    
@app.route('/add_review',methods=['POST','GET'])
def add_reveiw():
    if request.method=='POST':
        title=request.form['fname']
        review=request.form['w3review']
        movie_id=request.form['movie_id']
        functions.add_review(movie_id,str(session['id']),title,review)
        list=functions.movie_details_full(movie_id)
        return render_template('movie_page.html',movie_id=list[0],movie=list[1],genres=list[2],year=list[3],tag_line=list[4],overview=list[5],revenue=list[6],language=list[7],director=list[8],actors=list[9],runtime=list[10],age=list[11],homepage=list[12],poster=list[-7],popularity=list[13],rating=list[15],review=functions.get_reviews(movie_id),link=functions.movies_by_popularity(10),stars=int(float(list[-4])/2))


# @app.route('/modify_profile')
# def modify_profile():


@app.route('/loginotp')
def loginotp():
    return render_template('loginotp.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/search_results',methods=['POST','GET'])
def search_results():
    if request.method == 'POST':
        string=request.form['search']
        return render_template('search_results.html',list=functions.movies_with_filters_and_search(12,"|","0","0","en",str(string)))
    
@app.route('/new_user',methods=['POST','GET'])
def new_user():
    if request.method=='POST' :
        print(request.form)
        name=request.form['Name']
        user_name=request.form['User_Name']
        email=request.form['Email']
        password=request.form['Password']
        bool=functions.exists_user(user_name)
        if (bool):
            return render_template('index.html')
        else:
            functions.add_user(email,user_name,password,name)
            session['loggedin'] = True
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute('SELECT * FROM Users WHERE User_Name = %s AND Password = %s', (user_name, password))
            # Fetch one record and return result
            account = cursor.fetchone()
            session['id'] = account['User_ID'] #TODO
            session['username'] = account['User_Name']
            return render_template('login.html') # I will modify this

@app.route('/community')
def community():
    return render_template("community.html")

if __name__=="__main__":
    app.run(host="10.17.5.13", port=8080, debug=True)

