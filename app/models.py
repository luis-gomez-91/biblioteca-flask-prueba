from app import db

class Autor(db.Model):
    __tablename__ = 'autores'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)