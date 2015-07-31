import webapp2
import urllib2
import jinja2
import os
import random

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
    def get(self):
        dumpPreview = jinja_environment.get_template('templates/dumppreview.html')
        #self.response.write(dumpPreview.render(self.request.POST))
        self.response.write(dumpPreview.render())
    def post(self):
        msgInput = self.request.get('msgInput')
        emailInput= self.request.get('emailInput')
        # msgInput = 'poop'
        # emailInput = 'pooooop'
        urllist = [
            "../pictures/breakuppic2.jpg",
            "../pictures/breakuppic3.jpg",
            "../pictures/breakuppic4.jpg",
            "../pictures/breakuppic5.jpg",
            "../pictures/breakuppic6.jpg"]
        dict_words = {'msgInput': msgInput, 'emailInput': emailInput, "imageurl": random.choice(urllist)}
        #"imageurl" = random.choice(urllist)
        dumpPreview = jinja_environment.get_template('templates/dumppreview.html')
        #self.response.write(dumpPreview.render(self.request.POST))
        self.response.write(dumpPreview.render(dict_words))

class videoHandler(webapp2.RequestHandler):
    def get(self):
        randomNumber = random.randint(0,35)
        videoSearch = jinja_environment.get_template('templates/videoSearch.html')
        self.response.write(videoSearch.render())

class aboutHandler(webapp2.RequestHandler):
    def get(self):
        aboutPage = jinja_environment.get_template('templates/about.html')
        self.response.write(aboutPage.render())

class loseHandler(webapp2.RequestHandler):
    def get(self):
        losePage = jinja_environment.get_template('templates/unolose.html')
        self.response.write(losePage.render())

class winHandler(webapp2.RequestHandler):
    def get(self):
        winPage = jinja_environment.get_template('templates/unowin.html')
        self.response.write(winPage.render())

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
    ('/videos', videoHandler),
    ('/about', aboutHandler),
    ('/lose', loseHandler),
    ('/win', winHandler)
], debug=True)
