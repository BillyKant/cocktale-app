from flask import Blueprint, render_template
import requests
import json
from drink_inventory.forms import UserSearchForm1

site = Blueprint('site', __name__, template_folder='site_templates')

# @site.route('/', methods=['GET'])
# def home():

#     req = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita')
#     data = json.loads(req.content)
#     return render_template('index.html', data=data['drinks'])
    

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/', methods=['GET', 'POST'])
def home():
    form = UserSearchForm1()
    drink = form.drink_name.data
    print(drink)

    req = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink}")
    data = json.loads(req.content)
    print(data['drinks'])
    return render_template('index.html', data=data['drinks'], form=form)
