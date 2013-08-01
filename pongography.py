import cgi
import urllib

from google.appengine.api import users

import webapp2

MAIN = ""

with open("Main.html", "r") as f:
	MAIN = f.read()


class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write(MAIN)

class NewGame(webapp2.RequestHandler):
	def get(self):
		self.response.write("<html><body><pre>")
		self.response.write(self.request.get("player1"))
		self.response.write("</pre></body></html>")

application = webapp2.WSGIApplication([
	('/', MainPage),
	('/newgame', NewGame),
], debug=True)
