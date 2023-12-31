from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from flask_mail import Mail, Message
from flask_session import Session
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib
import math
from flask import Flask,render_template,request,redirect,flash
from flask import jsonify



global log
log = 0
global total_price
global username 
global total_items
username = 'no'
total_price = 0
total_items = 0



cart_contents = []
products = [
    {"id": 1, "name": "Bakewell tart", "price": 11.50, 'image': '/static/recipe_img/Bakewell.jpeg'},
    {"id": 2, "name": "Banana Bread", "price": 12.03, 'image': '/static/recipe_img/Bananabread.jpeg'},
    {"id": 3, "name": "Belgian buns", "price": 21.24, 'image': '/static/recipe_img/bellgianbread.jpeg'},
    {"id": 4, "name": "Chocolate Brownies", "price": 20.60, 'image': '/static/recipe_img/chocolatebrownies.jpeg'},
    {"id": 5, "name": "Chocolate Chip Cookies", "price": 10.20, 'image': '/static/recipe_img/chocochipcookies.jpeg'},
    {"id": 6, "name": "Cinnamon rolls", "price": 20.33, 'image': '/static/recipe_img/fudgybrownies.jpeg'},
    {"id": 7, "name": "Fudgy brownies", "price": 22.71, 'image': '/static/recipe_img/fudgybrownies.jpeg'},
    {"id": 8, "name": "Iced buns with cream & jam", "price": 18.99, 'image': '/static/recipe_img/icedbunswithcreamandjam.jpeg'},
    {"id": 9, "name": "lemon baked cheesecake", "price": 4.20, 'image': '/static/recipe_img/lemonbakedcheesecake.jpeg'},
    {"id": 10, "name": "Red velvet cupcakes", "price": 19.65, 'image': '/static/recipe_img/Red-Velvet-Cupcakes.jpeg'},
    {"id": 11, "name": "Rhubarb & custard sandwich biscuits", "price": 14.0, 'image': '/static/recipe_img/RubarbandCustard.jpeg'},
    {"id": 12, "name": "Triple choco peanut butter layer cake", "price": 12.20, 'image': '/static/recipe_img/triplechocolateandpeanutbutterlayercake.jpeg'},
    {"id": 13, "name": "Tropical upside-down cake", "price": 12.40, 'image': '/static/recipe_img/tropical-upside-down-cake.jpeg'},]

def get_total_items(cart):
    global total_items
    total_items = sum(item["quantity"] for item in cart)
    return total_items

def calculate_total_price(cart):
    global total_price
    total_price = sum(item["price"] * item["quantity"] for item in cart)
    return total_price

def get_product_by_id(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None

# Route for handling the login page logic
app = Flask(__name__)

# Change this to your secret key (it can be anything, it's for extra protection)
app.secret_key = 'work'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
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

# session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def index():
    global username
    session["loggedin"] = False
    session.modified = True
    global log
    log = 0
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
        session['loggedin'] = True
        global log
        log = 1
        if account:
            session['name'] = request.form.get('username')
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('LogIn.html', msg=msg)

@app.route("/logout")
def logout():
    global username
    global total_price
    global total_items
    global cart_contents
    global log
    log = 0
    username = 'no'
    total_price = 0
    total_items = 0
    cart_contents = []
    session["loggedin"] = False
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
    return render_template('home.html', msg = msg ,username = username, total_items=total_items)

@app.route('/SignUp', methods=['GET', 'POST'])
def SignUp():
    global username
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'Firstname' in request.form and 'Lastname' in request.form:
        username = request.form['username']
        password = request.form['password']
        firstname = request.form['Firstname']
        lastname = request.form['Lastname']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Login WHERE email = %s', (username,))       
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
            text_body = render_template('email_Welcome.html', name=firstname)
            text = Message(subject='Welcome', html=text_body, sender =('BakeItOrTakeIt', 't43797192@gmail.com'), recipients = [username])
            mail.send(text)
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
    return render_template('forgotPassword.html', msg=msg,)

@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    msg=""
    if request.method == 'POST' and 'email' and 'message' in request.form:
        email = request.form['email']
        contact = request.form['message']
        msg = 'Email sent! Thank you we will be right on it :)'
        text_body = render_template('email_contact_us.html',email = email, message= contact)
        text_body2 = render_template('email_contact_response.html',email = email, message= contact)
        text = Message(subject='contact us', html=text_body, sender =('BakeItOrTakeIt', 't43797192@gmail.com'), recipients = ['t43797192@gmail.com'])
        text2 = Message(subject='contact us', html=text_body, sender =('BakeItOrTakeIt', 't43797192@gmail.com'), recipients = [email])
        mail.send(text)
    return render_template('contact_us.html', msg = msg, username = username, total_items=total_items)


@app.route('/about')
def about():
    return render_template('about.html', username = username, total_items=total_items)

@app.route('/recipes')
def recipes():
    return render_template('Recipes.html', username = username, total_items=total_items)

@app.route('/shop', methods=['GET', 'POST'])
def shop():
    global total_items
    global username
    in1= False
    out1 = False
    if log == 0:
        out1 = True
    else:
        in1 = True
    return render_template('shop.html', username= username, total_items=total_items, products=products, in1 =in1, out1=out1)

@app.route('/cart')
def cart():
    global cart_contents
    global products
    msg ='Invalid Promo Code!'
    total_price = calculate_total_price(cart_contents)
    total_items = get_total_items(cart_contents)
    basket_amount = total_price
    basket_amount_delivery= float(basket_amount + 2.50)
    format(basket_amount_delivery, '.2f')
    return render_template('shopping_cart.html', username= username, total_price = format(basket_amount, '.2f'), total_price_delivery =  format(basket_amount_delivery, '.2f'), total_items=total_items, msg= msg,)

@app.route('/totalitems')
def totalitems():
    global total_items
    total_items = get_total_items(cart_contents)
    return redirect(url_for('shop'))    

@app.route('/shop/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = get_product_by_id(product_id)
    if product:
        for item in cart_contents:
            if item['id'] == product_id:
                item['quantity'] += 1
                flash('Item added to basket')
                session['cart'] = cart_contents
                session.modified = True
                break
        else:
            cart_contents.append({"id": product_id, "name": product['name'], "price": product['price'], "quantity": 1})
            flash('Item added to basket')
            session['cart'] = cart_contents
            session.modified = True
    return redirect(url_for('totalitems'))

@app.route('/shop/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    return redirect(url_for('cart'))

@app.route('/clear_cart')
def clear_cart():
    global cart_contents
    cart_contents = []  # Clear the cart by setting it to an empty list
    return redirect(url_for('cart'))

@app.route('/update_cart', methods=['POST', 'GET'])
def update_cart():
    global cart_contents

    for item in cart_contents:
        product_id = item['id']
        quantity_key = f'quantity_{product_id}'
        new_quantity = request.form.get(quantity_key, 0)
        
        # Ensure the new_quantity is an integer
        try:
            new_quantity = int(new_quantity)
        except ValueError:
            new_quantity = 0

        # Update the quantity in the cart
        item['quantity'] = new_quantity

    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)