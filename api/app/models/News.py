from sqlalchemy import func

from app import database

db = database.getDatabase()

class News(db.Model):
    __tablename__ = 'News'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())
