from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = 'mediocrity'

# Hardcoded username and password
const_username = '1234'
const_password = '1234'

# Routes...

@app.route('/')
@app.route('/home')
def home():
    # Check if the user is logged in
    if 'loggedin' in session:
        # User is logged in
        return render_template('index.html', username=session['username'])
    # User is not logged in
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong
    msg = ''
    # Check if "username", "password" and "email" POST requests exist
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # For simplicity, let's just print the registration information
        print(f"Username: {username}, Password: {password}, Email: {email}")

        # Your registration logic goes here, without the database interaction

        msg = 'You have successfully registered!'

    elif request.method == 'POST':
        # Form is empty
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Output a message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist 
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']

        # Check hardcoded username and password
        if username == const_username and password == const_password:
            # Simulate a successful login
            session['loggedin'] = True
            session['username'] = username

            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Incorrect username/password
            msg = 'Incorrect username/password!'
    
    # Show the login form with the message (if any)
    return render_template('login.html', msg=msg)

# Other routes...

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
