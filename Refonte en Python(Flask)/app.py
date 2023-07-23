from flask import Flask, render_template, request, jsonify
from models import db  # Importez db à partir de models.py
from models import TitleBasics, NameBasics, TitlePrincipals  # Importez db à partir de models.py
import random

import psycopg2

app = Flask(__name__)

# Configuration de la base de données SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:shiva1507@localhost:5432/Movies'  # Remplacez avec votre URL de connexion
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisez l'extension SQLAlchemy en lui passant l'application Flask
db.init_app(app)

# Configuration de la connexion à la base de données PostgreSQL
# conn = psycopg2.connect(
#     user='postgres',
#     host='localhost',
#     database='Movies',
#     password='shiva1507',
#     port='5432'
# )

# @app.route('/testdb')
# def test_db_connection():
#     try:
#         cursor = conn.cursor()
#         cursor.execute('SELECT 1')
#         result = cursor.fetchone()
#         cursor.close()
#         if result and result[0] == 1:
#             return 'La connexion à la base de données est réussie.'
#         else:
#             return 'Impossible de se connecter à la base de données.'
#     except Exception as e:
#         return f'Erreur lors de la connexion à la base de données : {str(e)}', 500
    
@app.route('/films')
def get_filtered_films():
    search_term = request.args.get('search', '').lower()  # Récupérer la valeur du paramètre de recherche et la convertir en minuscules
    try:
        # Rechercher les titres de films dont le titre original commence par la lettre saisie
        films = TitleBasics.query.filter(
            TitleBasics.originaltitle.ilike(f'{search_term}%')  # Commence par la lettre saisie (en minuscules)
        ).limit(100).all()

        return jsonify({'films': [film.originaltitle for film in films]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/actors')
def get_actors_by_letter():
    search_term = request.args.get('search', '').lower()  # Récupérer la lettre recherchée en minuscules
    try:
        # Rechercher les acteurs dont le nom commence par la lettre saisie
        actors = NameBasics.query.filter(
            NameBasics.primaryname.ilike(f'{search_term}%')  # Commence par la lettre saisie (en minuscules)
        ).limit(100).all()

        return jsonify({'actors': [actor.primaryname for actor in actors]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    

# @app.route('/films')
# def get_filtered_films():
#     search_term = request.args.get('search', '')  # Récupérer la valeur du paramètre de recherche
#     try:
#         cursor = conn.cursor()
        
#         # Rechercher les titres de films dont le titre original ou le titre principal contient le terme de recherche
#         cursor.execute('SELECT originaltitle FROM title_basics WHERE originaltitle ILIKE %s OR primarytitle ILIKE %s', [search_term + '%', search_term + '%'])
#         films = cursor.fetchall()

#         # Rechercher tous les noms d'acteurs dont le nom principal contient le terme de recherche
#         cursor.execute('SELECT primaryname FROM name_basics WHERE primaryname ILIKE %s', [search_term + '%'])
#         all_actors = cursor.fetchall()

#         cursor.close()

#         # Générer aléatoirement 100 noms d'acteurs parmi les acteurs filtrés
#         random_actors = random.sample(all_actors, min(100, len(all_actors)))

#         # Générer aléatoirement 100 titres de films parmi les titres filtrés
#         random_films = random.sample(films, min(100, len(films)))

#         return jsonify({'films': random_films, 'actors': random_actors})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# Créer la route test
@app.route('/test')
def test_route():
    try:
        # Exemple de requête simple pour récupérer les 10 premières lignes de la table title_basics
        results = TitlePrincipals.query.limit(10000).all()

        return render_template('test.html', results=results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
    
@app.route('/common_actors')
def find_common_actors():
    film1_title = request.args.get('film1_title', '').strip()
    film2_title = request.args.get('film2_title', '').strip()

    try:
        # Rechercher les acteurs pour chaque film
        film1 = TitleBasics.query.filter_by(originaltitle=film1_title).first()
        film2 = TitleBasics.query.filter_by(originaltitle=film2_title).first()

        if not film1 or not film2:
            return jsonify({'error': 'Les titres de film spécifiés n\'existent pas.'}), 404

        # Extraire les noms des acteurs pour chaque film
        film1_actors = set()
        film2_actors = set()

        for principal in TitlePrincipals.query.filter_by(tconst=film1.tconst).all():
            actor = NameBasics.query.filter_by(nconst=principal.nconst).first()
            if actor:
                film1_actors.add(actor.primaryname)

        for principal in TitlePrincipals.query.filter_by(tconst=film2.tconst).all():
            actor = NameBasics.query.filter_by(nconst=principal.nconst).first()
            if actor:
                film2_actors.add(actor.primaryname)

        # Trouver les acteurs en commun entre les deux films
        common_actors = list(film1_actors.intersection(film2_actors))

        return jsonify({'common_actors': common_actors})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/search')
def search_films():
    return render_template('search.html')


# Route pour la page de recherche d'acteurs et d'actrices
@app.route('/actors')
def actors_page():
    return render_template('actors.html')

# Route pour récupérer les acteurs et actrices en fonction du film recherché
@app.route('/actors', methods=['GET'])
def get_actors_by_film():
    film_title = request.args.get('film', '').strip()

    try:
        # Rechercher les acteurs et actrices pour le film spécifié
        film = TitlePrincipals.query.filter_by(primarytitle=film_title).first()

        if film:
            actors = [actor.primaryname for actor in film.actors]
            return jsonify({'actors': actors})
        else:
            return jsonify({'error': 'Film non trouvé.'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# import random

# @app.route('/search2')
# def search_films():
#     search_term = request.args.get('search', '')
    
#     try:
#         cursor = conn.cursor()

#         # Utiliser une requête préparée pour éviter les problèmes de sécurité liés aux injections SQL
#         cursor.execute('SELECT primarytitle FROM title_basics WHERE primarytitle ILIKE %s', [search_term + '%'])
#         films = cursor.fetchall()
#         cursor.close()

#         # Filtrer les films dont le titre commence par la lettre saisie
#         filtered_films = [film[0] for film in films if film[0].lower().startswith(search_term.lower())]

#         # Générer aléatoirement 100 titres de films parmi les films filtrés
#         random_films = random.sample(filtered_films, min(100, len(filtered_films)))

#         return jsonify(random_films)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500





