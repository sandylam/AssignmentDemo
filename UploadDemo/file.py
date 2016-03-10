import webapp2
from google.appengine.ext import ndb
from google.appengine.api import users
import os
import jinja2

# for logging message to server log
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

from google.appengine.ext.webapp.util import login_required
        
# import the models from another python file
from models import Account
from models import DatastoreFile
    
class UploadHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        
        # check if there is an account
        # use .get() because there should 1 record only
        
        acct = Account.query(Account.userId == user.user_id()).get()
        if not acct:
            # create one
            Account(name=user.nickname(), userId=user.user_id(), email= user.email()).put()
        
        template = JINJA_ENVIRONMENT.get_template('upload.html')        
        self.response.out.write(template.render({}))
    
    
    def post(self):
        user = users.get_current_user()        
        file = self.request.POST['file']
        
        # no need to retrieve the Account entity, just link it by userId which is the key
        entity = DatastoreFile(data=file.value, mimetype=file.type, userId=user.user_id())
        entity.put()
        file_url = "http://%s/file/download/%d" % (self.request.host, entity.key.id())
        
        # or you can link this entity to other entity (e.g. link to an album)
        self.response.out.write("Your uploaded file is now available at <a href='%s'>%s</a>" % (file_url,file_url))        

# serve the file with the id with this url  http://<server>/file/<file key id>
# you can configure the path to suit your API
class DownloadHandler(webapp2.RequestHandler):
    def get(self, id):
        # can use get_by_id if you know the number id of the entity
        entity = DatastoreFile.get_by_id(int(id))
        self.response.headers['Content-Type'] = str(entity.mimetype)
        self.response.out.write(entity.data)        

# Exercise
# How to list all uploaded files by the same user? 

app = webapp2.WSGIApplication([
    ('/file/upload', UploadHandler),
    ('/file/download/(\d+)', DownloadHandler)
], debug=True)
