from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy

class Table(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = 0
    price = 0
    description = 0
    photo = 0
    isActive = 0


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('FAQ.html')

if __name__=='__main__':
    app.run(debug=True)