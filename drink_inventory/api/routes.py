import imp
from urllib import response
from flask import Blueprint, request, jsonify
from drink_inventory.helpers import token_required
from drink_inventory.models import db, User, Drink, drink_schema, drinks_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
@token_required
def getdata(current_user_token):
    return {'some':'value'}