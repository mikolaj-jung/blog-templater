from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blogs = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()

    return render_template("index.html", blogs=blogs)

@app.route('/blog/<int:num>')
def get_blog(num):
    print(num)
    blogs = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()

    return render_template("post.html", num=num, blogs=blogs)

if __name__ == "__main__":
    app.run(debug=True)
