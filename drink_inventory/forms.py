from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators= [DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired()])
    submit_button = SubmitField()

class UserSignupForm(FlaskForm):
    # email, password, submit_button
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First_Name', validators=[DataRequired()])
    last_name = StringField('Last_Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()

class UserSearchForm1(FlaskForm):
    drink_name = StringField('drink', validators=[DataRequired()])
    submit_button = SubmitField()

class UserSearchForm2(FlaskForm):
    ingredient_name = StringField('ingredient', validators=[DataRequired()])
    submit_button = SubmitField()

class UserSearchForm3(FlaskForm):
    random = StringField('random', validators=[DataRequired()])
    submit_button = SubmitField()

class AddDrinkForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])  
    instructions = StringField('instructions', validators=[DataRequired()]) 
    image = StringField('instructions', validators=[DataRequired()]) 
    ingredient1 = StringField('ingredient1', validators=[DataRequired()])  
    measure1 = StringField('measure1', validators=[DataRequired()]) 
    ingredient2 = StringField('ingredient2', validators=[DataRequired()])  
    measure2 = StringField('measure2', validators=[DataRequired()]) 
    ingredient3 = StringField('ingredient3', validators=[DataRequired()])  
    measure3 = StringField('measure3', validators=[DataRequired()]) 
    ingredient4 = StringField('ingredient4', validators=[DataRequired()])  
    measure4 = StringField('measure4', validators=[DataRequired()]) 
    ingredient5 = StringField('ingredient5', validators=[DataRequired()])  
    measure5 = StringField('measure5', validators=[DataRequired()]) 
    ingredient6 = StringField('ingredient6', validators=[DataRequired()])  
    measure6 = StringField('measure6', validators=[DataRequired()]) 
    ingredient7 = StringField('ingredient7', validators=[DataRequired()])  
    measure7 = StringField('measure7', validators=[DataRequired()]) 
    ingredient8 = StringField('ingredient8', validators=[DataRequired()])  
    measure8 = StringField('measure8', validators=[DataRequired()]) 
    ingredient9 = StringField('ingredient9', validators=[DataRequired()])  
    measure9 = StringField('measure9', validators=[DataRequired()]) 
    ingredient10 = StringField('ingredient10', validators=[DataRequired()])  
    measure10 = StringField('measure10', validators=[DataRequired()]) 
    ingredient11 = StringField('ingredient11', validators=[DataRequired()])  
    measure11 = StringField('measure11', validators=[DataRequired()]) 
    ingredient12 = StringField('ingredient12', validators=[DataRequired()])  
    measure12 = StringField('measure12', validators=[DataRequired()]) 
    ingredient13 = StringField('ingredient13', validators=[DataRequired()])  
    measure13 = StringField('measure13', validators=[DataRequired()]) 
    ingredient14 = StringField('ingredient14', validators=[DataRequired()])  
    measure14 = StringField('measure14', validators=[DataRequired()]) 
    ingredient15 = StringField('ingredient15', validators=[DataRequired()])  
    measure15 = StringField('measure15', validators=[DataRequired()]) 
    submit_button = SubmitField()

class DeleteDrinkForm(FlaskForm):
    id = StringField('id', validators=[DataRequired()])  
    submit_button = SubmitField()
