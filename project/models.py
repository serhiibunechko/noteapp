from datetime import datetime
from . import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    heading = db.Column(db.String(200), nullable=False)
    note = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "Message {}".format(self.id)
