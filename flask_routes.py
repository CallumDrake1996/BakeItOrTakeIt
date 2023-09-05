from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from flask_mail import Mail, Message
from flask_session import Session
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib
# Route for handling the login page logic
app = Flask(__name__)

# Change this to your secret key (it can be anything, it's for extra protection)
app.secret_key = 'work'
bcrypt = Bcrypt(app)
# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'PASSWORD'
app.config['MYSQL_DB'] = 'MakeItOrTakeIt'

# config mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 't43797192@gmail.com'
app.config['MAIL_PASSWORD'] = 'vggxycrdbxtypako'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# Intialize MySQL
mysql = MySQL(app)



@app.route('/')
def index():
    session["loggedin"] = False
    session.modified = True
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        global username 
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Login WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            session['name'] = request.form.get('username')
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('LogIn.html', msg=msg)

<<<<<<< HEAD
=======
@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

@app.route('/home', methods=['GET', 'POST'])
def home():
    msg=''
    global username
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT first_name FROM Login WHERE username = %s', (username,))
    first_name = cursor.fetchone()
    username = first_name
    return render_template('home.html', msg = msg,username = username)




@app.route('/SignUp', methods=['GET', 'POST'])
def SignUp():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'Firstname' in request.form and 'Lastname' in request.form:
        username = request.form['username']
        password = request.form['password']
        firstname = request.form['Firstname']
        lastname = request.form['Lastname']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Login WHERE username = %s', (username))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not firstname or not lastname:
            msg = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO Login (email, username, password, first_name, last_name) VALUES (%s,%s, %s,%s,%s)', (username, username, password,firstname, lastname))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
            return render_template('register.html', msg=msg)
    return render_template('register.html', msg=msg)


@app.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPass():
    msg = ''
    if request.method == 'POST' and 'email' in request.form:
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Login WHERE email = %s', (email,))
        account = cursor.fetchone()
        if account:
            cursor.execute('Select password from Login where email = %s', (email,))
            password = cursor.fetchone()
            msg = 'Email sent! Please check your inbox(spam folder too) for password'
            text_body = render_template('email_template.html', password=password)
            text = Message(subject='Password', html=text_body, sender =('BakeItOrTakeIt', 't43797192@gmail.com'), recipients = [email])
            mail.send(text)
        else:
            msg = 'Email does not exist!'
    return render_template('forgotPassword.html', msg=msg)

@app.route('/mail', methods=['GET', 'POST'])
def email():
   msg = Message('Hello', sender = 't43797192@gmail.com', recipients = ['t43797192@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"

 
>>>>>>> e03a5f632362c1ea96ce4b15de8fa349296e8481
@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

if __name__ == '__main__':
    app.run(debug=True)