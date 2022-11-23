from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import SignUpForm, LogInForm, ReferralScreeningForm
from app.models import User, Tool
from flask_login import login_user, logout_user, current_user, login_required



@app.route('/')
def index():
    # user = form.username.data
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
        # Check to see if we have a user with username and/or password:
        check_user = User.query.filter( (User.username == username) | (User.email == email) ).first()
        if check_user is not None:
            flash('User with username and/or email already exists', 'danger')
            return redirect(url_for('signup'))
        # Add a new user to the database
        new_user = User(email=email, username=username, password=password)
        # Flash a success message
        flash(f"{new_user} has successfully signed up!", "success")
        #Redirect back to home
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)





@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        # Get the form data
        username = form.username.data
        password = form.password.data

        # Check to see if there is a user with that username and password
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            # log the user in
            login_user(user)
            flash(f"{user} is now logged in.", 'primary')
            return redirect(url_for('index'))
        else:
            flash('Incorrect username and/or password. Please try again.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html', form=form)   
    
@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))


@app.route('/screening', methods=['GET', 'POST'])
@login_required
def screening():
    form = ReferralScreeningForm()
    if form.validate_on_submit():
        print('You Have Finished Screening3')

        #Get Screening Results
        firstname = form.firstname.data
        lastname = form.lastname.data
        question1 = form.question1.data
        question2 = form.question2.data
        question3 = form.question3.data
        question4 = form.question4.data
        question5 = form.question5.data
        question6 = form.question6.data
        question7 = form.question7.data
        question8 = form.question8.data
        question9 = form.question9.data
        question10 = form.question10.data
        question11 = form.question11.data
        question12 = form.question12.data
        question13 = form.question13.data
        question14 = form.question14.data
        question15 = form.question15.data
        question16 = form.question16.data
        question17 = form.question17.data
        question18 = form.question18.data
        question19 = form.question19.data
        question20 = form.question20.data
        question21 = form.question21.data
        question22 = form.question22.data
        question23= form.question23.data
        question24= form.question24.data

        # Create a new instance of Post with the info from the form
        fresh_tool = Tool(firstname = firstname, lastname= lastname, question1 = question1, question2=question2, question3 = question3, 
        question4 = question4, question5 = question5, question6 = question6, question7 = question7, question8 = question8,
        question9 = question9, question10 = question10, question11 = question11, question12 = question12, question13 = question13,
        question14 = question14, question15 = question15, question16=question16, question17 = question17, 
        question18 = question18, question19 = question19, question20 = question20, question21 = question21, 
        question22 = question22, question23 = question23,
        question24 = question24, user_id=current_user.id)
        
        # flash a message of success
        flash(f"Screening for patient # {fresh_tool.firstname}{fresh_tool.lastname} is complete.", "success")
        # Redirect back to the home pag
        return redirect(url_for('index'))

    return render_template('screeningtool.html', form=form)
    #     flash('You have finished screening', 'info')
    #     return redirect(url_for('index'))
    # return render_template('screeningtool.html', title = 'Referral Screening Tool', form=form)

@app.route('/posts/<tool_id>')
@login_required
def get_patient(tool_id):
    form = ReferralScreeningForm()
    tool = Tool.query.get(tool_id)
    if not tool:
        flash(f"No Patient with id #{tool_id} has been screened. Please complete their screening ASAP", "warning")
        return redirect(url_for('index'))
    return render_template('screeningtool.html', form = form)

@app.route('/posts/<tool_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_patient(tool_id):
    form = ReferralScreeningForm()
    tool = Tool.query.get(tool_id)
    if not tool:
        flash(f"No Patient with id #{tool_id} has been screened", "warning")
        return redirect(url_for('index'))
    # if post.author != current_user:
    #     flash('You do not have permission to edit this post', 'danger')
    #     return redirect(url_for('index'))
    form = ReferralScreeningForm()
    if form.validate_on_submit():
        # Get the form data
        new_firstname = form.firstname.data
        new_lastname = form.lastname.data
        new_question1 = form.question1.data
        new_question2 = form.question2.data
        new_question3 = form.question3.data
        new_question4 = form.question4.data
        new_question5 = form.question5.data
        new_question6 = form.question6.data
        new_question7 = form.question7.data
        new_question8 = form.question8.data
        new_question9 = form.question9.data
        new_question10 = form.question10.data
        new_question11 = form.question11.data
        new_question12 = form.question12.data
        new_question13 = form.question13.data
        new_question14 = form.question14.data
        new_question15 = form.question15.data
        new_question16 = form.question16.data
        new_question17 = form.question17.data
        new_question18 = form.question18.data
        new_question19 = form.question19.data
        new_question20 = form.question20.data
        new_question21 = form.question21.data
        new_question22 = form.question22.data
        new_question23= form.question23.data
        new_question24= form.question24.data
        # update the tool
        flash(f"You have updated the Screening Results for Patient {tool.firstname}{tool.lastname}  ", "success")


        Tool(firstname = new_firstname, lastname= new_lastname, question1 =new_question1, question2=new_question2, 
        question3 = new_question3, 
        question4 = new_question4, question5 = new_question5, question6 = new_question6, question7 = new_question7, 
        question8 = new_question8,
        question9 = new_question9, question10 = new_question10, question11 = new_question11, question12 = new_question12,
        question13 = new_question13,
        question14 = new_question14, question15 = new_question15, question16=new_question16, question17 = new_question17, 
        question18 = new_question18, question19 = new_question19, question20 = new_question20, question21 = new_question21, 
        question22 = new_question22, question23 = new_question23,
        question24 = new_question24, user_id=current_user.id)
        flash(f"You have updated the Screening Results for Patient {tool.firstname}{tool.lastname}  ", "success")
        return redirect(url_for('index', tool_id=tool.id))
    return render_template('edit_post.html', post=tool, form=form)



