from flask import Flask, jsonify, request,render_template, url_for

app = Flask(__name__) #referencing this file

movies = [
    {}
]

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/movie')
def movie():
    return render_template('movie_page.html')

if __name__=="__main__":
    app.run(debug=True)

