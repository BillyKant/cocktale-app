from venv import create
from flask import Blueprint, jsonify, redirect, render_template, url_for
from flask_login import current_user, AnonymousUserMixin


import requests
import json

from drink_inventory.forms import UserSearchForm1, AddDrinkForm
# from drink_inventory.api.routes import create_drink
from drink_inventory.helpers import token_required, create_my_drink
from drink_inventory.models import db, User, Drink, drink_schema, drinks_schema

site = Blueprint('site', __name__, template_folder='site_templates')

class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'

# HOME PAGE ROUTE
@site.route('/', methods=['POST', 'GET'])
def home():
    if current_user.is_authenticated:
        # Search Form Code
        form = UserSearchForm1()
        form2= AddDrinkForm()
        drink = form.drink_name.data
        req = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink}")
        data = json.loads(req.content)
        
        # Add Drink Form Code   
        create_my_drink()      

        return render_template('index.html', data=data['drinks'], form=form, form2=form2)

    else:
        return redirect(url_for('auth.signin'))

# PROFILE PAGE ROUTE
@site.route('/profile', methods=['GET', 'POST'])
def profile():
        owner = current_user.token
        drinks = Drink.query.filter_by(user_token = owner).all()
        response = drinks_schema.dump(drinks)
        if response:
            print(response[0]['name'])
            for drink in response:
                print(drink['name'])

        return render_template('profile.html', response=response)
