from flask import Flask, render_template, request, redirect, url_for
# Route for handling the login page logic
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    return render_template('HomePage.html', error = error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('LogIn.html', error=error)

# debug for flask 
if __name__ == '__main__':
    app.run(debug=True)


                <div class="form-check d-flex justify-content-start mb-4">
                  <input class="form-check-input" type="checkbox" value="" id="form1Example3" />
                  <label class="form-check-label" for="form1Example3"> Remember password </label>
                </div>
