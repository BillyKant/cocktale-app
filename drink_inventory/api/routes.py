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

#create Drink Endpoint
# @api.route('/drinks', methods = ['POST'])
# @token_required
# def create_drink(current_user_token):
#     name = request.json['name']
#     instructions = request.json['instructions']
#     image = request.json['image']
#     ingredient1 = request.json['ingredient1']
#     measure1 = request.json['measure1']
#     ingredient2 = request.json['ingredient2']
#     measure2 = request.json['measure2']
#     ingredient3 = request.json['ingredient3']
#     measure3 = request.json['measure3']
#     ingredient4 = request.json['ingredient4']
#     measure4 = request.json['measure4']
#     ingredient5 = request.json['ingredient5']
#     measure5 = request.json['measure5']
#     ingredient6 = request.json['ingredient6']
#     measure6 = request.json['measure6']
#     ingredient7 = request.json['ingredient7']
#     measure7 = request.json['measure7']
#     ingredient8 = request.json['ingredient8']
#     measure8 = request.json['measure8']
#     ingredient9 = request.json['ingredient9']
#     measure9 = request.json['measure9']
#     ingredient10 = request.json['ingredient10']
#     measure10 = request.json['measure10']
#     ingredient11 = request.json['ingredient11']
#     measure11 = request.json['measure11']
#     ingredient12 = request.json['ingredient12']
#     measure12 = request.json['measure12']
#     ingredient13 = request.json['ingredient13']
#     measure13 = request.json['measure13']
#     ingredient14 = request.json['ingredient14']
#     measure14 = request.json['measure14']
#     ingredient15 = request.json['ingredient15']
#     measure15 = request.json['measure15']
#     user_token = current_user_token.token

#     print(f"BIG TESTER: {current_user_token.token}")

#     drink = Drink(name, instructions, image, ingredient1, measure1, ingredient2, measure2, ingredient3, measure3, ingredient4, measure4, ingredient5, measure5, ingredient6, measure6, ingredient7, measure7, ingredient8, measure8, ingredient9, measure9, ingredient10, measure10, ingredient11, measure11, ingredient12, measure12, ingredient13, measure13, ingredient14, measure14, ingredient15, measure15, user_token = user_token)

#     db.session.add(drink)
#     db.session.commit()

#     response = drink_schema.dump(drink)

#     return jsonify(drink)