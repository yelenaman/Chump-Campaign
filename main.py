import webapp2
import urllib2
import jinja2
import os

class landingHandler(webapp2.RequestHandler):
    def get(self):
        landing = jinja_environment.get_template('templates/landing.html')
        self.response.write(landing.render())
class homeHandler(webapp2.RequestHandler):
    def get(self):
        homePage = jinja_environment.get_template('templates/home.html')
        self.response.write(homePage.render())

class unoHomeHandler(webapp2.RequestHandler):
    def get(self):
        unoHome = jinja_environment.get_template('templates/unohome.html')
        self.response.write(unoHome.render())

class unoInstructionsHandler(webapp2.RequestHandler):
    def get(self):
        unoInstructions = jinja_environment.get_template('templates/unoinstructions.html')
        self.response.write(unoInstructions.render())

class unoGameHandler(webapp2.RequestHandler):
    def get(self):
        unoGame = jinja_environment.get_template('templates/unogame.html')
        self.response.write(unoGame.render())

class locatorHandler(webapp2.RequestHandler):
    def get(self):
        locator = jinja_environment.get_template('templates/locator.html')
        self.response.write(locator.render())

class dumpHandler(webapp2.RequestHandler):
    def get(self):
        dump = jinja_environment.get_template('templates/dump.html')
        self.response.write(dump.render())

class dumpSentHandler(webapp2.RequestHandler):
    def get(self):
        dumpSent = jinja_environment.get_template('templates/dumpsent.html')
        self.response.write(dumpSent.render())

class dumpPreviewHandler(webapp2.RequestHandler):
    def post(self):
        msgInput = self.request.get('msgInput')
        emailInput= self.request.get('emailInput')
        dict_words = {'msgInput': msgInput, 'emailInput': emailInput}
        dumpPreview = jinja_environment.get_template('templates/dumppreview.html')
        self.response.write(dumpPreview.render(dict_words))

class videoHandler(webapp2.RequestHandler):
    def get(self):
        videoSearch = jinja_environment.get_template('templates/videoSearch.html')
        self.response.write(videoSearch.render())

jinja_environment = jinja2.Environment(loader=
jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', landingHandler),
    ('/home', homeHandler),
    ('/unohome', unoHomeHandler),
    ('/unoinstructions', unoInstructionsHandler),
    ('/unogame', unoGameHandler),
    ('/locations', locatorHandler),
    ('/breakup', dumpHandler),
    ('/breakupsent', dumpSentHandler),
    ('/breakuppreview', dumpPreviewHandler),
    ('/videos', videoHandler)
], debug=True)
