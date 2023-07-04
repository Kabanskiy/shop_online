from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Table(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    description = db.Column(db.Text, nullable = False)
    # photo = db.Column(db.String(300), nullable = False)
    isActive = db.Column(db.Boolean, default = True)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']

        table = Table(name=name, price=price, description=description)

        try:
            db.session.add(table)
            db.session.commit()
            return redirect('/')
        except:
            return 'Что-то полшо не так'
    return render_template('create.html')

@app.route('/detail')
def detail():
    return render_template('detail.html')

@app.route('/faq')
def faq():
    return render_template('FAQ.html')

if __name__=='__main__':
    app.run(debug=True)