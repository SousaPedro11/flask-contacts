from flask_restful import Resource, marshal

from app import requests, db
from app.decorator import jwt_required
from app.models import Contact
from app.schemas import contact_field


class Contacts(Resource):
    @jwt_required
    def get(self, current_user):
        contacts = Contact.query.all()
        return marshal(contacts, contact_field, 'contacts')

    @jwt_required
    def post(self, current_user):
        payload = requests.only(['name', 'cellphone'])
        name = payload['name']
        cellphone = payload['cellphone']

        contact = Contact(name, cellphone)
        db.session.add(contact)
        db.session.commit()
        return marshal(contact, contact_field, 'contact')

    @jwt_required
    def put(self, current_user):
        payload = requests.only(['id', 'name', 'cellphone'])
        _id = payload['id']
        name = payload['name']
        cellphone = payload['cellphone']

        contact = Contact.query.get(_id)

        if not contact:
            return {'message': 'Contact not found!'}

        if name:
            contact.name = name
        if cellphone:
            contact.cellphone = cellphone

        db.session.add(contact)
        db.session.commit()

        return marshal(contact, contact_field, 'contact')

    @jwt_required
    def delete(self, current_user):
        payload = requests.only(['id'])
        _id = payload['id']

        contact = Contact.query.get(_id)

        if not contact:
            return {'message': 'Contact not found!'}

        db.session.delete(contact)
        db.session.commit()

        return marshal(contact, contact_field, 'contact')
