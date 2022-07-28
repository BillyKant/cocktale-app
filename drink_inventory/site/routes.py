from venv import create
from flask import Blueprint, jsonify, redirect, render_template, url_for, request
from flask_login import current_user, AnonymousUserMixin


import requests
import json

from drink_inventory.forms import DeleteDrinkForm, UserSearchForm1, AddDrinkForm, UserSearchForm2, UserSearchForm3
from drink_inventory.helpers import delete_my_drink, token_required, create_my_drink, delete_my_drink
from drink_inventory.models import db, User, Drink, drink_schema, drinks_schema

site = Blueprint('site', __name__, template_folder='site_templates')

class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'

# HOME PAGE ROUTE
@site.route('/', methods=['POST', 'GET'])
def home():
    if current_user.is_authenticated:
        # Search by Drink name
        form = UserSearchForm1()
        drink = form.drink_name.data
        req = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink}")
        data = json.loads(req.content)


        # Get a Random drink
        form4 = UserSearchForm3()
        rand_drink = form4.random.data
        print(rand_drink)
        req4 = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/{rand_drink}.php")
        print(req4)
        # data4 = json.loads(req4.content)
        # print(data4)
        

        # Add drink  
        form2 = AddDrinkForm()
        create_my_drink()      


        # form3 = UserSearchForm2()
        # ingredient = form3.ingredient_name.data
        # print(ingredient)
        # req2 = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}")
        # data2 = json.loads(req2.content)
        # drinks = data2['drinks']
        # for each in drinks:
        #     print(each['idDrink'])
        #     req3 = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={each}")
        #     data3 = json.loads(req3.content)
        #     print(data3)

        

        return render_template('index.html', data=data['drinks'], form=form, form2=form2, form4=form4)

    else:
        return redirect(url_for('auth.signin'))

# PROFILE PAGE ROUTE
@site.route('/profile', methods=['GET', 'POST'])
def profile():
        form = DeleteDrinkForm()
        
        if request.method == 'POST':
            delete_my_drink()
        owner = current_user.token
        drinks = Drink.query.filter_by(user_token = owner).all()
        response = drinks_schema.dump(drinks)
        if response:
            print(response[0]['name'])
            for drink in response:
                print(drink['name'])


        return render_template('profile.html', response=response, form=form)


