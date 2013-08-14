var CONTROL = {};
var GAME = {};

httpRequest = function(callback, type, target, pill)
{
	var request = new XMLHttpRequest();

	request.onreadystatechange = function() 
	{
		if (request.readyState == 4)
		{
			console.log(this.responseText);
			callback( JSON.parse( this.responseText ));
		}
	};

	request.open( type, "/" + target + '?pill='+ JSON.stringify( pill ), true );
	request.send();
};

CONTROL.PlayerRoster = (function()
{
	//private:
	var players = {}, o = {};

	//public:
	o.register = function(player)//creates game once 2 players are registered
	{
		if(!players["player1"]) players["player1"] = player;

		else
		{
			players["player2"] = player;

			httpRequest(GAME.Game.importGame,"PUT", "game", {"content": players});//pill origin

			players = {};
		}
	};
	return o;
}());

GAME.Game = (function()
{
	//private:
	var setElements = function(newPill) //callback from Game.importGame's httpRequest
	{
		pill = newPill;
	};

	var pill = {}, o = {};

	//public:
	o.importGame = function(pill) //callback from PlayerRoster's httpRequest
	{
		httpRequest( setElements, "GET", "game", pill);
	};

	o.point = function(victor)
	{
		pill['content'] = pill['content'][victor];
		httpRequest( o.importGame,"POST","game", pill);
	}

	return o;
}());

