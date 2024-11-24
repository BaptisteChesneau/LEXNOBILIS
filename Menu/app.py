from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

# Configuration du répertoire de téléchargement
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Liste pour stocker les informations des documents (à remplacer par une base de données pour une application réelle)
documents = []

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Ajoutez ici la logique pour vérifier les informations de connexion
        return redirect(url_for('espace_client'))
    return render_template('login.html')

@app.route('/espace_client')
def espace_client():
    return render_template('espace_client.html')

@app.route('/suivi_dossier')
def suivi_dossier():
    return render_template('suivi_dossier.html', documents=documents)

@app.route('/envoie_documents', methods=['GET', 'POST'])
def envoi_documents():
    if request.method == 'POST':
        if 'document' not in request.files:
            return 'No file part'
        file = request.files['document']
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            documents.append({'filename': filename, 'path': os.path.join(app.config['UPLOAD_FOLDER'], filename)})
            return redirect(url_for('suivi_dossier'))
    return render_template('envoie_documents.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

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
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)