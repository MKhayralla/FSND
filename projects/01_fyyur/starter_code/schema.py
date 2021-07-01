from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(120)))
    seeking_talent = db.Column(db.Boolean)
    seeking_talent_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref = 'venue', lazy = True)
    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(120)))
    seeking_venue = db.Column(db.Boolean)
    seeking_venue_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref = 'artist', lazy = True)

class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key = True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable = False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable = False)
    starts_at = db.Column(db.Date, nullable = False)    

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
