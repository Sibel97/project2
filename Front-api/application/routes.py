from application import app, db
from flask import Flask, request, render_template, url_for
from application.models import Books
import requests


# home route
@app.route('/')
def home():
    return render_template("Home.html")




@app.route('/Generate', methods = ['GET'])
def Generate():
    Genre = requests.get('http://Genre-api:5000/get_Genre')
    Author = requests.get('http://Author-api:5000/get_Author')
    result = requests.post('http://Book-api:5000/get_book', json = {"Author": Author.text, "Genre": Genre.text} )
    book = Books( Title = result.text, Author = Author.text, Genre= Genre.text)
    db.session.add(book)
    db.session.commit()
    last = Books.query.order_by(Books.id.desc()).limit(1).all()
    return render_template('layout.html', book = book, last = last)


@app.route('/PreviousBooks', methods=['GET'])
def Previous():
    books = map(str,Books.query.all())
    return render_template('books.html', books = books)