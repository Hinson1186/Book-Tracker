from src.models.user import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    cover_image_url = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<Book {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'cover_image_url': self.cover_image_url
        }

