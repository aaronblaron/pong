from google.appengine.ext import ndb
import random
import re
import json
import time

class Game(ndb.Model):
	player1 = ndb.StringProperty()
	player2 = ndb.StringProperty()
	victor = ndb.StringProperty()
	rallies = ndb.JsonProperty()

	server = ndb.ComputedProperty( lambda self:\
		self.player1 if not self.rallies or len(self.rallies) <= 1\
			else self.player2 if len(self.rallies) <= 3\
				else self.rallies[-4]["server"] )

	def state(self):
		return {
			'player1': self.player1,
			'player2': self.player2,
			'player1Points': len(re.findall('[\"|\']victor[\"|\']:\s?[\"|\']' + self.player1 + '[\"|\']', json.dumps(self.rallies))),
			'player2Points': len(re.findall('[\"|\']victor[\"|\']:\s?[\"|\']' + self.player2 + '[\"|\']', json.dumps(self.rallies))),
			'server': self.server
		}

	def point(self, victor):
		if not self.rallies: self.rallies = [{'victor': victor, 'server': self.server}]
		else: self.rallies.append({'victor': victor, 'server': self.server})
#		return self.state()
		self.put()


def retrieve(key):
	return ndb.Key(urlsafe=key).get()

def create(players): #returns urlsafe key
	players = sorted([players['player1'], players['player2']], key=lambda k: random.random())
	return Game(player1=players[0], player2=players[1]).put().urlsafe()
