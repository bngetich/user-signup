from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def display_index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index():
    username = ''
    password = ''
    verify_password = ''
    email = ''
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''
    title = 'User Signup'

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    if not username:
        username_error = 'Username cannot be left empty.'
    
    for i in username:
        if username and i.isspace():
            username_error = 'Username cannot contain a space character.'

    if username and len(username) < 3 or len(username) > 20:
        username_error = 'Username must be between 3-20 characters.'

    if not password:
        password_error = 'Password cannot be left empty.'
        password = ''

    for i in password:
        if password and i.isspace():
            password_error = 'Password cannot contain a space character.'
            password = ''

    if password and len(password) < 3 or len(password) > 20:
        password_error = 'Password must be between 3-20 characters.'
        password = ''

    if password != verify_password and not password_error:
        verify_password_error = 'Password do not match.'
        password = ''
        verify_password = ''

    if email != '' and not re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email):
        email_error = 'Not a valid email.'

    if not username_error and not password_error and not verify_password_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))

    else:
        return render_template('index.html', title=title, username=username, email=email,
                               username_error=username_error, password_error=password_error,
                               verify_password_error=verify_password_error, email_error=email_error)


@app.route('/welcome')
def welcome():
    title = 'Welcome'
    username = request.args.get('username')
    return render_template('welcome.html', username=username, title=title)


if __name__ == "__main__":
    app.run()
