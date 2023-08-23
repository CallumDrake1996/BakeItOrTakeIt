from flask import Flask, render_template, url_for

app = Flask(__name__)


# this file can be used to store .routes to all templates



from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

@app.route('/shop')
def shop():
    return render_template('shopping_cart.html')

@app.route('/login')
def login():
    return render_template('LogIn.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

if __name__ == '__main__':
    app.run(debug=True)

