from flask_restful import Resource, marshal
from app.src.models import User
from app import request, db
from app.schemas import user_field
import jwt
import datetime
from flask import current_app


class Login(Resource):
    def post(self):
        playload = request.json
        username = playload.get('username')
        password = playload.get('password')
        print(username, password)
        user = User.query.filter_by(username=username).first()
        if not user and user.compare_password(password):
            return {'message': 'Credenciais estão incorretas'}, 401
        data = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }
        token = jwt.encode(data, current_app.config['SECRET_KEY'])
        return {'access_token': token.decode('utf-8')}

    def get(self):
        user = User.query.all()
        return marshal(user, user_field, 'user')


class Register(Resource):
    def post(self):
        playload = request.json
        username = playload.get('username')
        password = playload.get('password')
        print(username, password)
        user = User(username, password)
        db.session.add(user)
        db.session.commit()

        return marshal(user, user_field, 'user')

    

