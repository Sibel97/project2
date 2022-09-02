from application import app
from flask import Flask, request, Response

@app.route('/get_book', methods = ['POST'])
def effect():
    books = {"Lady of the shades": ("Romance", "Darren Shan"), "One Summer" : ("Romance", "David Baldacci"), "Two from the heart": ("Romance","James Patterson"), "The dead zone": ("Romance","Stephen King"), \
        "Lord Loss":("Horror", "Darren Shan"), "IT": ("Horror", "Stephen King"), "Cradle and all": ("Horror","James Patterson"), "Deliver us from evil": ("Horror", "David Baldacci") \
            ,"Possession of the dead": ("Crime", "Darren Shan"), "Mr Mercedes": ("Crime","Stephen King"), "Along came a spider": ("Crime", "James Patterson"), "Walk the wire": ("Crime", "David Baldacci"), \
                "Cirque du Freak": ("Fantasy","Darren Shan"), "The eyes of the dragon": ("Fantasy", "Stephen King"), "Witch and Wizard": ("Fantasy", "James Patterson"), "The finisher": ("Fantasy","David Baldacci")}
    BookChoice = request.get_json()
    Genre = BookChoice["Genre"]
    Author = BookChoice["Author"]
    book = list(books.keys())[list(books.values()).index((Genre,Author))]
    effect = f"{book} By {Author} - Genre: {Genre}"
    return Response(effect, mimetype='text/plain')

    

