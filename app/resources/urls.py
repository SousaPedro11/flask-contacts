from app import api

from . import contacts, auth

api.add_resource(auth.Login, '/api/v1/login/')
api.add_resource(auth.Register, '/api/v1/register/')
api.add_resource(contacts.Contacts, '/api/v1/contacts/')
