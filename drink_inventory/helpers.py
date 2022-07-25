from functools import wraps
from json import JSONEncoder

from flask import request, jsonify, json
from flask_login import current_user

from drink_inventory.models import Drink, User
from drink_inventory.forms import AddDrinkForm
from drink_inventory.models import db, User, Drink, drink_schema, drinks_schema

import decimal

def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split(' ')[1]
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            current_user_token = User.query.filter_by(token = token).first()
            print(current_user_token)
            if not current_user_token or current_user_token.token != token:
                return jsonify({'message':'Token is invalid'})

        except:
            owner = User.query.filter_by(token = token).first()

            if token != owner.token and secrets.compare_digest(token, owner.token):
                return jsonify({'message': 'Token is invalid!'})
        return our_flask_function(current_user_token, *args, **kwargs)
    return decorated

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            #Convert decimal instances into strings
            return str(obj)
        return super(JSONEncoder, self).default(obj)

def create_my_drink():
        form2= AddDrinkForm()
        name = form2.name.data
        instructions = form2.instructions.data
        image = form2.image.data
        ingredient1 = form2.ingredient1.data
        measure1 = form2.measure1.data
        ingredient2 = form2.ingredient2.data
        measure2 = form2.measure2.data
        ingredient3 = form2.ingredient3.data
        measure3 = form2.measure3.data
        ingredient4 = form2.ingredient4.data
        measure4 = form2.measure4.data
        ingredient5 = form2.ingredient5.data
        measure5 = form2.measure5.data
        ingredient6 = form2.ingredient6.data
        measure6 = form2.measure6.data
        ingredient7 = form2.ingredient7.data
        measure7 = form2.measure7.data
        ingredient8 = form2.ingredient8.data
        measure8 = form2.measure8.data
        ingredient9 = form2.ingredient9.data
        measure9 = form2.measure9.data
        ingredient10 = form2.ingredient10.data
        measure10 = form2.measure10.data
        ingredient11 = form2.ingredient11.data
        measure11 = form2.measure11.data
        ingredient12 = form2.ingredient12.data
        measure12 = form2.measure12.data
        ingredient13 = form2.ingredient13.data
        measure13 = form2.measure13.data
        ingredient14 = form2.ingredient14.data
        measure14 = form2.measure14.data
        ingredient15 = form2.ingredient15.data
        measure15 = form2.measure15.data
        user_token = current_user.token

        my_drink = Drink(name, instructions, image, ingredient1, measure1, ingredient2, measure2, ingredient3, measure3, ingredient4, measure4, ingredient5, measure5, ingredient6, measure6, ingredient7, measure7, ingredient8, measure8, ingredient9, measure9, ingredient10, measure10, ingredient11, measure11, ingredient12, measure12, ingredient13, measure13, ingredient14, measure14, ingredient15, measure15, user_token = user_token)

        drinks_db = Drink.query.all()
        # for drink in drinks_db:
        #     print(f'db drink{drink.name}')
        #     print(f'new drink{my_drink.name}')
        #     if my_drink.name:
        #         print('already exists')
        #     else:
        #         if my_drink.name:
        #             db.session.add(my_drink)
        #             db.session.commit()
        
        if my_drink.name in drinks_db:
            print (f'{my_drink.name} already has already been added')
        elif my_drink.name:
            print(f'adding {my_drink.name}')
            db.session.add(my_drink)
            db.session.commit()


        
        # db.session.add(my_drink)
        # db.session.commit()
        # response = drink_schema.dump(my_drink)

        return my_drink