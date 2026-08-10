from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=True)
    job_url = db.Column(db.String(100), nullable=True)
    deadline = db.Column(db.Date(), nullable=True)
    status = db.Column(db.String(50), default="Saved", nullable=False)
    job_desc = db.Column(db.Text(), nullable=True)
    notes = db.Column(db.Text(), nullable=True)
