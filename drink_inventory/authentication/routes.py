import imp
from flask import Blueprint, render_template, request, redirect, url_for, flash
from drink_inventory.forms import UserLoginForm, UserSignupForm
from drink_inventory.models import User, db, check_password_hash, login_manager

#Import from flask login
from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint('auth', __name__, template_folder = 'auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserSignupForm()

    try:
        if request.method == "POST" and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            print(email, password, first_name, last_name)

            user = User(email, first_name=first_name, last_name=last_name, password = password)

            db.session.add(user)
            db.session.commit()

            flash(f"You have successfully created a user account {first_name}", 'user-created')

            return redirect(url_for('auth.signin'))

    except:
        raise Exception('Invalid Form Data: Please Check Your Form')

    return render_template('signup.html', form=form)

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()

    try:
        if request.method == "POST" and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)

            logged_user = User.query.filter(User.email == email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('You were successfully logged in in via Email/Password', 'auth-success')
                return redirect(url_for('site.profile'))
            else:
                flash('Your Email/Password is incorrect', 'auth-failed')
                return redirect(url_for('auth.signin'))
    except:
        raise Exception('Invalid Form Data: Please Check Your Form')

    return render_template('signin.html', form=form)

# @auth.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('site.home'))

