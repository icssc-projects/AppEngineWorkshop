from google.appengine.ext import ndb

class User(ndb.Model):
    """ Data model for a user """
    user_id = ndb.StringProperty(indexed = True)
    nickname = ndb.StringProperty(indexed = False)
