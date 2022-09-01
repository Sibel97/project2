from application import app
from flask import Flask, request, Response
import random

@app.route('/get_Author', methods=['GET'])
def Author():
    Author = random.choice(["Darren Shan", "Stephen King", "James Patterson", "David Baldacci"])
    print(Author)
    return Response(Author, mimetype='text/plain')