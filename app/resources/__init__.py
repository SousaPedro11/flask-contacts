from flask import Blueprint

contacts_api = Blueprint('contacts_api', __name__)

from . import urls
