from flask import current_app
from app import db
# from app.models.task import Task

class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)

def to_json(self):
    return {
        "id": self.goal_id,
        "title": self.title,
    }

