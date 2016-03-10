from google.appengine.ext import ndb

class Account(ndb.Model):
    name = ndb.StringProperty()  #nickname
    userId = ndb.StringProperty() #unique userid, will not change
    email = ndb.StringProperty() #user email
 
class DatastoreFile(ndb.Model):
    data = ndb.BlobProperty(default=None)  # max size  < 1mb
    mimetype = ndb.StringProperty(required=True)    
    # add userId to link file to a user    
    userId = ndb.StringProperty()