from flask import Blueprint, request, jsonify
from api.models import db, User
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError

api = Blueprint('api', __name__)

@api.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    required_fields = ["first_name", "last_name", "mother_last_name", "email", "password", "role"]
    if not all(field in data and data[field] for field in required_fields):
        return jsonify({"msg": "Faltan campos obligatorios"}), 400

    try:
        # Crear usuario
        user = User(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            mother_last_name=data.get("mother_last_name"),
            birth_date=data.get("birth_date"),
            sex=data.get("sex"),
            role=data.get("role"),
            education_level=data.get("education_level"),
            education_area=data.get("education_area"),
            institution=data.get("institution"),
            registration_number=data.get("registration_number"),
            phone=data.get("phone"),
            email=data.get("email"),
            password=generate_password_hash(data.get("password"))
        )

        db.session.add(user)
        db.session.commit()

        return jsonify({"msg": "Usuario registrado correctamente"}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"msg": "El correo ya está registrado"}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": f"Error en el servidor: {str(e)}"}), 500

