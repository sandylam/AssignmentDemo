import webapp2
from google.appengine.ext.webapp.util import login_required
from google.appengine.api import users

# this is the "/" page, do not modify. This page is not part of the assignment
class MainHandler(webapp2.RequestHandler):
    @login_required
    def get(self):       
        user = users.get_current_user()
        self.response.out.write('Hello, ' + user.nickname())  
        self.response.write('<br>Upload <a href="/file/upload">files</a>')        
                
app = webapp2.WSGIApplication([('/*.', MainHandler)], debug=True)
