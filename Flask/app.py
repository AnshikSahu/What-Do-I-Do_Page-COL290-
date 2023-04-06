from flask import Flask, jsonify, request,render_template, url_for
import functions
app = Flask(__name__) #referencing this file

movies = [
    {}
]

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

@app.route('/profile')
def profile():
    return render_template('profile.html')

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

if __name__=="__main__":
    app.run(debug=True)

