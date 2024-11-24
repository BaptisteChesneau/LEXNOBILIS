from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

# Configuration du répertoire de téléchargement
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Liste pour stocker les informations des documents (à remplacer par une base de données pour une application réelle)
documents = []

# Articles de blog fictifs
articles = [
    {'id': 1, 'title': 'L\'importance du droit civil', 'description': 'Un aperçu du droit civil et de son importance dans la société.', 'content': 'Contenu détaillé de l\'article sur le droit civil.', 'image': 'civil_law.jpg'},
    {'id': 2, 'title': 'Les défis du droit pénal', 'description': 'Une exploration des défis rencontrés dans le domaine du droit pénal.', 'content': 'Contenu détaillé de l\'article sur le droit pénal.', 'image': 'criminal_law.jpg'},
    {'id': 3, 'title': 'La montée en puissance du droit des affaires', 'description': 'Comment le droit des affaires évolue et s\'adapte aux nouvelles réalités économiques.', 'content': 'Contenu détaillé de l\'article sur le droit des affaires.', 'image': 'business_law.jpg'},
    {'id': 4, 'title': 'L\'évolution du droit de la famille', 'description': 'Les changements dans le droit de la famille et leur impact sur la société.', 'content': 'Contenu détaillé de l\'article sur le droit de la famille.', 'image': 'family_law.jpg'},
    {'id': 5, 'title': 'Le droit international en perspective', 'description': 'Un regard sur les enjeux actuels du droit international.', 'content': 'Contenu détaillé de l\'article sur le droit international.', 'image': 'international_law.jpg'},
    {'id': 6, 'title': 'Les nouveaux défis du droit environnemental', 'description': 'Comment le droit environnemental s\'attaque aux problèmes mondiaux.', 'content': 'Contenu détaillé de l\'article sur le droit environnemental.', 'image': 'environmental_law.jpg'},
    {'id': 7, 'title': 'Le rôle des avocats dans la société moderne', 'description': 'La place et l\'influence des avocats dans le monde d\'aujourd\'hui.', 'content': 'Contenu détaillé de l\'article sur le rôle des avocats.', 'image': 'lawyers_role.jpg'},
    {'id': 8, 'title': 'Les technologies et le droit', 'description': 'L\'impact des nouvelles technologies sur la pratique du droit.', 'content': 'Contenu détaillé de l\'article sur les technologies et le droit.', 'image': 'tech_law.jpg'}
]

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
    return render_template('blog.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = next((a for a in articles if a['id'] == article_id), None)
    if article is None:
        return "Article non trouvé", 404
    return render_template('article.html', article=article)

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
