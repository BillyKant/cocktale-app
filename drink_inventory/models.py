from dis import Instruction
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime

# Flask Security for Passwords
from werkzeug.security import generate_password_hash, check_password_hash

#Secrets Module (from by Python)
import secrets

# Imports for Flask_Login
from flask_login import UserMixin, LoginManager

# Import for Flask-Marshmallow
from flask_marshmallow import Marshmallow

db=SQLAlchemy()
login_manager=LoginManager()
ma=Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(250), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True)
    date_create = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    drink = db.relationship('Drink', backref = 'owner', lazy = True)


    def __init__(self, email, first_name ='', last_name='',id='',password='',token='',g_auth_verify=False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f"User {self.email} has been added to the database"    

class Drink(db.Model):
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(150))
    instructions = db.Column(db.String(5000))
    image = db.Column(db.String(200))
    ingredient1 = db.Column(db.String(100))
    measure1 = db.Column(db.String(100))
    ingredient2 = db.Column(db.String(100))
    measure2 = db.Column(db.String(100))
    ingredient3 = db.Column(db.String(100))
    measure3 = db.Column(db.String(100))
    ingredient4 = db.Column(db.String(100))
    measure4 = db.Column(db.String(100))
    ingredient5 = db.Column(db.String(100))
    measure5 = db.Column(db.String(100))
    ingredient6 = db.Column(db.String(100))
    measure6 = db.Column(db.String(100))
    ingredient7 = db.Column(db.String(100))
    measure7 = db.Column(db.String(100))
    ingredient8 = db.Column(db.String(100))
    measure8 = db.Column(db.String(100))
    ingredient9 = db.Column(db.String(100))
    measure9 = db.Column(db.String(100))
    ingredient10 = db.Column(db.String(100))
    measure10 = db.Column(db.String(100))
    ingredient11 = db.Column(db.String(100))
    measure11 = db.Column(db.String(100))
    ingredient12 = db.Column(db.String(100))
    measure12 = db.Column(db.String(100))
    ingredient13 = db.Column(db.String(100))
    measure13 = db.Column(db.String(100))
    ingredient14 = db.Column(db.String(100))
    measure14 = db.Column(db.String(100))
    ingredient15 = db.Column(db.String(100))
    measure15 = db.Column(db.String(100))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    

    def __init__(self, name, instructions, image, ingredient1, measure1, ingredient2, measure2, ingredient3, measure3, ingredient4, measure4, ingredient5, measure5, ingredient6, measure6, ingredient7, measure7, ingredient8, measure8, ingredient9, measure9, ingredient10, measure10, ingredient11, measure11, ingredient12, measure12, ingredient13, measure13, ingredient14, measure14, ingredient15, measure15, user_token, id = ''):
        self.id = self.set_id()
        self.name = name
        self.instructions = instructions
        self.image = image
        self.ingredient1 = ingredient1
        self.measure1 = measure1
        self.ingredient2 = ingredient2
        self.measure2 = measure2
        self.ingredient3 = ingredient3
        self.measure3 = measure3
        self.ingredient4 = ingredient4
        self.measure4 = measure4
        self.ingredient5 = ingredient5
        self.measure5 = measure5
        self.ingredient6 = ingredient6
        self.measure6 = measure6
        self.ingredient7 = ingredient7
        self.measure7 = measure7
        self.ingredient8 = ingredient8
        self.measure8 = measure8
        self.ingredient9 = ingredient9
        self.measure9 = measure9
        self.ingredient10 = ingredient10
        self.measure10 = measure10
        self.ingredient11 = ingredient11
        self.measure11 = measure11
        self.ingredient12 = ingredient12
        self.measure12 = measure12
        self.ingredient13 = ingredient13
        self.measure13 = measure13
        self.ingredient14 = ingredient14
        self.measure14 = measure14
        self.ingredient15 = ingredient15
        self.measure15 = measure15
        self.user_token = user_token

    def __repr__(self):
        return f"The following Drink has been added: {self.name}"

    def set_id(self):
        return secrets.token_urlsafe()

class DrinkSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'instructions', 'image', 'ingredient1', 'measure1', 'ingredient2', 'measure2','ingredient3', 'measure3','ingredient4', 'measure4','ingredient5', 'measure5','ingredient6', 'measure6','ingredient7', 'measure7','ingredient8', 'measure8','ingredient9', 'measure9','ingredient10', 'measure10','ingredient11', 'measure11','ingredient12', 'measure12','ingredient13', 'measure13','ingredient14', 'measure14','ingredient15', 'measure15',]

drink_schema = DrinkSchema()
drinks_schema = DrinkSchema(many = True)




