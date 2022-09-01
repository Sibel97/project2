from application import app
from flask import Flask, request, Response
import random

@app.route('/get_Genre', methods=['GET'])
def Genre():
    Genre = random.choice(["Romance", "Comedy", "Fantasy", "Horror", "Crime", "Drama"])
    print(Genre)
    return Response(Genre, mimetype='text/plain')