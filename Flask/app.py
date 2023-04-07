from flask import Flask, jsonify, request,render_template, url_for
import functions
app = Flask(__name__) #referencing this file

movies = [
    {}
]
User_ID=1
@app.route('/')
def index():
    link=functions.movies_by_popularity(10)
    return render_template('index.html',mname="Titanic",link=link)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/movie')
def movie():
    movie_id = request.args.get('movie_id')
    list=functions.movie_details_full(movie_id)
    return render_template('movie_page.html',movie=list[1],genres=list[2],year=list[3],tag_line=list[4],overview=list[5],revenue=list[6],language=list[7],director=list[8],actors=list[9],runtime=list[10],age=list[11],homepage=list[12],poster=list[-6],popularity=list[13],rating=list[15],review=functions.get_reviews(movie_id))

@app.route('/profile',methods=['POST','GET'])
def profile():
    if request.method == 'GET':
        user_details=functions.user_details_with_ID(str(User_ID))
        first_name=user_details[-5].split()[0]
        last_name=user_details[-5].split()[-1]
        email=user_details[2]
        password=user_details[5]
        user_name=user_details[4]
        about=user_details[-1]
        return render_template('profile.html',first_name=first_name,user_name=user_name,sur_name=last_name,email=email,password=password,about=about)
    if request.method=='POST':
        for i in request.form.keys():print(i)
        user_details=functions.user_details_with_ID(str(User_ID))
        first_name=request.form['First_Name']
        last_name=request.form['Sur_Name']
        functions.update_user_name(str(User_ID),first_name+" "+last_name)
        email=request.form['Email']
        functions.update_user_email(str(User_ID),email)
        password=request.form['Password']
        functions.update_user_password(str(User_ID),password)
        user_name=user_details[4]
        about=request.form['About']
        functions.update_about(str(User_ID),about)
        return render_template('profile.html',first_name=first_name,user_name=user_name,sur_name=last_name,email=email,password=password,about=about)
    
        

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
            print("Hiiiiiiii")
            return render_template('signup.html')
        else :
            functions.add_user(email,user_name,password,name)
            return render_template('login.html')

if __name__=="__main__":
    app.run(debug=True)

