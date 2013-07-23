#!/usr/bin/python
import cgi
import json
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
game = form.getfirst('game', 'empty')
#game = cgi.escape(game)

gamesJson = json.loads(game)

def mergeGames(games, newGame):
    foundMatch = False

    for oldGame in games:
        if(oldGame["guid"] == newGame["guid"]):
            oldGame["rallies"] = newGame["rallies"]
            foundMatch = True
            break

    if(not foundMatch):
        games.append(newGame)

    return games

with open("games.json","r+") as f:
    newBody = json.dumps(mergeGames(json.load(f), gamesJson))
    f.truncate(0)
    f.seek(0)
    f.write(newBody)

