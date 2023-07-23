from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Définition des classes de modèles pour les différentes tables

class TitleBasics(db.Model):
    __tablename__ = 'title_basics'
    tconst = db.Column(db.String, primary_key=True)
    titletype = db.Column(db.String)
    primarytitle = db.Column(db.String)
    originaltitle = db.Column(db.String)
    isadult = db.Column(db.Boolean)
    startyear = db.Column(db.String)
    endyear = db.Column(db.String)
    runtimeminutes = db.Column(db.Integer)
    genres = db.Column(db.String)  

class NameBasics(db.Model):
    __tablename__ = 'name_basics'
    nconst = db.Column(db.String, primary_key=True)
    primaryname = db.Column(db.String)
    birthyear = db.Column(db.String)
    deathyear = db.Column(db.String)
    primaryprofession = db.Column(db.String)  
    knownfortitles = db.Column(db.String)  

class TitleCrew(db.Model):
    __tablename__ = 'title_crew'
    tconst = db.Column(db.String, primary_key=True)
    directors = db.Column(db.ARRAY(db.String))  # Notez l'utilisation de db.ARRAY pour les tableaux de chaînes
    writers = db.Column(db.ARRAY(db.String))  

class TitleEpisode(db.Model):
    __tablename__ = 'title_episode'
    tconst = db.Column(db.String, primary_key=True)
    parenttconst = db.Column(db.String)
    seasonnumber = db.Column(db.Integer)
    episodenumber = db.Column(db.Integer)

class TitlePrincipals(db.Model):
    __tablename__ = 'title_principals'
    tconst = db.Column(db.String, primary_key=True)
    ordering = db.Column(db.Integer)
    nconst = db.Column(db.String)
    category = db.Column(db.String)
    job = db.Column(db.String)
    characters = db.Column(db.String)

class TitleRatings(db.Model):
    __tablename__ = 'title_ratings'
    tconst = db.Column(db.String, primary_key=True)
    averagerating = db.Column(db.Float)
    numvotes = db.Column(db.Integer)

class TitleAkas(db.Model):
    __tablename__ = 'title_akas'
    titleId = db.Column(db.String, primary_key=True)
    ordering = db.Column(db.Integer)
    title = db.Column(db.String)
    region = db.Column(db.String)
    language = db.Column(db.String)
    types = db.Column(db.ARRAY(db.String))  
    attributes = db.Column(db.ARRAY(db.String)) 
    isoriginaltitle = db.Column(db.Boolean)
