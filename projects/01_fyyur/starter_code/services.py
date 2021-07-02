'''
an abstraction layer between the database model and the app
also contains helper functions for the app
'''
#Imports
import dateutil.parser
import babel
from schema import *

#Functions
def format_datetime(value, format='medium'):
    date = dateutil.parser.parse(value)
    if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
      format="EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format, locale='en')

def get_boolean(s):
    if s is None:
        return False
    return True

def add_venue(name, genres, address, city, state, phone, website, facebook_link, seeking_talent, seeking_description, image_link):
    '''
    adds a new venue to the database given data extracted from the form
    '''
    venue = Venue(name = name,
    city = city,
    state = state,
    address = address,
    phone = phone,
    image_link = image_link,
    facebook_link = facebook_link,
    website = website,
    genres = genres,
    seeking_talent = seeking_talent,
    seeking_talent_description = seeking_description)
    try:
        db.session.add(venue)
        db.session.commit()
    except Exception as e:
        print(e)
        return db.session.rollback()
    return venue

def add_artist(name, genres, city, state, phone, website, facebook_link, seeking_venue, seeking_description, image_link):
    '''
    adds a new artist to the database given data extracted from the form
    '''
    artist = Artist(name = name,
    city = city,
    state = state,
    phone = phone,
    image_link = image_link,
    facebook_link = facebook_link,
    website = website,
    genres = genres,
    seeking_venue = seeking_venue,
    seeking_venue_description = seeking_description)
    try:
        db.session.add(artist)
        db.session.commit()
    except Exception as e:
        print(e)
        return db.session.rollback()
    return artist

def add_show(artist_id, venue_id, start_date):
    show = Show(artist_id = artist_id, venue_id = venue_id, starts_at = start_date)
    try:
        db.session.add(show)
        db.session.commit()
    except Exception as e:
        print(e)
        return db.session.rollback()
    return show