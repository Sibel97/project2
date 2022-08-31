from application import db

class Books(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100))
    Author = db.Column(db.String(50))
    Genre = db.Column(db.String(50))
    def __str__(self):
        return f"{self.ISBN}: {self.Title} by  {self.Author}. Genre: {self.Genre}"