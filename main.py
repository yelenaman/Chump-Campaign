import webapp2
import urllib2
import jinja2
import os

class landingHandler(webapp2.RequestHandler):
    def get(self):
        landingPage = jinja_environment.get_template('landing.html')
        self.response.write(landingPage.render())
class HomeHandler(webapp2.RequestHandler):
    def get(self):
        homePage = jinja_environment.get_template('home.html')
        self.response.write(homePage.render())

class unoHomeHandler(webapp2.RequestHandler):
    def get(self):
        unoHome = jinja_environment.get_template('unohome.html')
        self.response.write(unoHome.render())

class unoInstructionsHandler(webapp2.RequestHandler):
    def get(self):
        unoInstructions = jinja_environment.get_template('unoinstructions.html')
        self.response.write(unoInstructions.render())

class unoGameHandler(webapp2.RequestHandler):
    def get(self):
        unoGame = jinja_environment.get_template('unogame.html')
        self.response.write(unoGame.render())

class locatorHandler(webapp2.RequestHandler):
    def get(self):
        locator = jinja_environment.get_template('locator.html')
        self.response.write(locator.render())

class dumpHandler(webapp2.RequestHandler):
    def get(self):
        dump = jinja_environment.get_template('dump.html')
        self.response.write(dump.render())

class dumpSentHandler(webapp2.RequestHandler):
    def get(self):
        dumpSent = jinja_environment.get_template('dumpsent.html')
        self.response.write(dumpSent.render())

class dumpPreviewHandler(webapp2.RequestHandler):
    def get(self):
        dumpPreview = jinja_environment.get_template('dumppreview.html')
        self.response.write(dumpPrevieHandler())

jinja_environment = jinja2.Environment(loader=
jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', landingHandler),
    ('/home', HomeHandler),
    ('/unohome', unoHomeHandler),
    ('/locations', locatorHandler),
    ('/breakup', dumpHandler),
    ('/breakupsent', dumpSentHandler),
    ('/breakuppreview', dumpPreviewHandler)
], debug=True)
