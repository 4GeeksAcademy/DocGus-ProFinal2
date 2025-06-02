from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    mother_last_name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    sex = db.Column(db.String(20), nullable=True)
    role = db.Column(db.String(50), nullable=False)
    education_level = db.Column(db.String(50), nullable=True)
    education_area = db.Column(db.String(100), nullable=True)
    institution = db.Column(db.String(100), nullable=True)
    registration_number = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Considera hashearla
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "mother_last_name": self.mother_last_name,
            "birth_date": self.birth_date.isoformat() if self.birth_date else None,
            "sex": self.sex,
            "role": self.role,
            "education_level": self.education_level,
            "education_area": self.education_area,
            "institution": self.institution,
            "registration_number": self.registration_number,
            "phone": self.phone,
            "email": self.email,
            "created_at": self.created_at.isoformat()
        }
