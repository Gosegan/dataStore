# Modelo

from google.appengine.ext import ndb

class EcoDto(ndb.Model):
    text = ndb.StringProperty(required=True)
    hours = ndb.DateTimeProperty(auto_now_add=True)
    author = ndb.StringProperty()