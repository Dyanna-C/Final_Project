# from app import app
# from flask import render_template, flash, redirect, url_for
# from app.forms import SignUpForm, LogInForm
# # from app.models import User, Post



from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import SignUpForm, LogInForm, ReferralScreeningForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)
    

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print('You Are Officially Signed Up')
        # Get data from form
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(email, username, password)
        # # Check to see if we have a user with username and/or password:
        # check_user = User.query.filter( (User.username == username) | (User.email == email) ).first()
        # if check_user is not None:
        #     flash('User with username and/or email already exists', 'danger')
        #     return redirect(url_for('signup'))
        # # Add a new user to the database
        # new_user = User(email=email, username=username, password=password)
        # # Flash a success message
        # flash(f"{new_user} has successfully signed up!", "success")
        # Redirect back to home
        # return redirect(url_for('index'))

    return render_template('signup.html', form=form)



@app.route('/login')
def login():
    form = LogInForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        # return redirect('/index')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LogInForm()
#     if form.validate_on_submit():
#         # Get the form data
#         username = form.username.data
#         password = form.password.data

        # Check to see if there is a user with that username and password
        # user = User.query.filter_by(username=username).first()
        # if user is not None and user.check_password(password):
        #     # log the user in
        #     login_user(user)
        #     flash(f"{user} is now logged in.", 'primary')
        #     return redirect(url_for('index'))
        # else:
        #     flash('Incorrect username and/or password. Please try again.', 'danger')
        #     return redirect(url_for('login'))

    # return render_template('login.html', form=form)

@app.route('/screening', methods=['GET', 'POST'])
def screening():
    form = ReferralScreeningForm()
    return render_template('screeningtool.html', title = 'Referral Screening Tool', form=form)
   
    