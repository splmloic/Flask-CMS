from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET','POST'])
def login():
    return render_template('login.html')

@auth.route("/logout")
def logout():
    return "<p>logout</p>"

@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        data = request.form
        print(data)
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 2 characters.', category='error')
        elif password != confirm_password:
            flash('Your passwords dont match', category='error')
        elif len(password) < 6:
            flash('Your password must be greater than 6 characters', category='error')
        else:
            # add user to database
            print('account created')
            flash('Account created!', category='success')

    return render_template('signup.html')