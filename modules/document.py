from google.appengine.ext import ndb

class Document(ndb.Model):
    """ Data model for a single document """
    text = ndb.StringProperty(indexed = False)
    online = ndb.JsonProperty(indexed = False)
