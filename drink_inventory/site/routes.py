from venv import create
from flask import Blueprint, render_template

import requests
import json
from drink_inventory.forms import UserSearchForm1, AddDrinkForm
# from drink_inventory.api.routes import create_drink
from drink_inventory.helpers import token_required, create_my_drink
from drink_inventory.models import db, User, Drink, drink_schema, drinks_schema

site = Blueprint('site', __name__, template_folder='site_templates')

# HOME PAGE ROUTE
@site.route('/', methods=['POST', 'GET'])
def home():
    # Search Form Code
    form = UserSearchForm1()
    form2= AddDrinkForm()
    drink = form.drink_name.data
    print(drink)
    req = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink}")
    data = json.loads(req.content)
    
    

    # Add Drink Form Code   
    create_my_drink()      


    return render_template('index.html', data=data['drinks'], form=form, form2=form2)

# PROFILE PAGE ROUTE
@site.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')
