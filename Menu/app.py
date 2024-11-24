from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Ajoutez ici la logique pour enregistrer les informations du compte
        return redirect(url_for('signup_confirmation'))
    return render_template('signup.html')

@app.route('/signup_confirmation')
def signup_confirmation():
    return render_template('signup_confirmation.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/nous')
def nous():
    return "Nous Page"

@app.route('/nos_avocats')
def nos_avocats():
    return "Nos Avocats Page"

@app.route('/blog')
def blog():
    return "Blog Page"

@app.route('/formulaire')
def formulaire():
    return "Formulaire Page"

@app.route('/paiement')
def paiement():
    return "Paiement Page"

@app.route('/chatbot')
def chatbot():
    return "Chatbot Page"

if __name__ == '__main__':
    app.run(debug=True)