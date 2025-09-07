from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.Enum('STUDENT','FACULTY','ADMIN'), nullable=False)
    contact = db.Column(db.String(15))
    department = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Event(db.Model):
    __tablename__ = 'events'
    event_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.Enum('CULTURAL','TECHNICAL','SPORTS','ACADEMIC','OTHER'))
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    venue_id = db.Column(db.String(36), db.ForeignKey('venues.venue_id'))
    created_by = db.Column(db.String(36), db.ForeignKey('users.user_id'))
    approval_status = db.Column(db.Enum('PENDING','APPROVED','REJECTED'), default='PENDING')
    capacity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
