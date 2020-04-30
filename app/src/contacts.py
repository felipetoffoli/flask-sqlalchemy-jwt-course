from flask_restful import Resource, marshal
from app.src.models import Contact
from app import request, db
from app.schemas import contact_field
from app.decorator import jwt_required

class Contacts(Resource):
    @jwt_required
    def get(self, current_user):
        contacts = Contact.query.all()
        return marshal(contacts, contact_field, 'contacts')

    @jwt_required
    def post(self, current_user):
        if not request.is_json:
            return {'message': 'parametros precisam ser json'}

        playload = request.json
        name = playload.get('name')
        cellphone = playload.get('cellphone')

        contact = Contact(name, cellphone)
        db.session.add(contact)
        db.session.commit()
        return marshal(contact, contact_field, 'contact')

    @jwt_required
    def put(self, current_user):
        if not request.is_json:
            return {'message': 'parametros precisam ser json'}

        playload = request.json
        _id = playload.get('id')
        name = playload.get('name')
        cellphone = playload.get('cellphone')

        contact = Contact.query.get(_id)
        if not contact:
            return {'message': 'Contato não existe'}
        contact.name = name
        contact.cellphone = cellphone
        
        db.session.add(contact)
        db.session.commit()
        return marshal(contact, contact_field, 'contact')

    @jwt_required
    def delete(self, current_user):
        if not request.is_json:
            return {'message':'parametros precisam ser json'}
        
        playload = request.json
        _id = playload.get('id')

        contact = Contact.query.get(_id)
        if not contact:
            return {'message': 'Contato não existe'}
        
        db.session.delete(contact)
        db.session.commit()
        return marshal(contact, contact_field, 'contact')
