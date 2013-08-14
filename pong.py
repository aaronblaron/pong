import urllib
import cgi
import json
from model import game

import webapp2

MAIN = ""

with open("html/Main.html", "r") as f:
	MAIN = f.read()


class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write(MAIN)

class RunningGame(webapp2.RequestHandler):
	def get(self):
		pill = json.loads( self.request.get('pill') )
		instance = game.retrieve( pill['guid'] )
		pill['content'] = instance.state()
		self.response.write( json.dumps( pill ))

	def put(self):
		pill = json.loads( self.request.get('pill') )
		pill['guid'] = game.create( pill['content'] )
		self.response.write( json.dumps( pill ))

	def post(self):
		pill = json.loads( self.request.get('pill') )
		game.retrieve( pill['guid'] ).point( pill['content'] )
		self.response.write( json.dumps( pill ))


application = webapp2.WSGIApplication([
	('/', MainPage),
	('/game', RunningGame),
], debug=True)
