from myblog import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeigKey('users.id'), nullable=False)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    create_date = db.Column(db.DataTime, nullable=False, default=datetime.utcnow)

    def __init__(self, author, title, body) -> None:
        self.author = author
        self.title = title
        self.body = body
    
    def __repr__(self) -> str:
        return f'Post: {self.title}'

