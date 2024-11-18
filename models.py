from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmailLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), default="Sent")  # Options: Sent, Failed
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
