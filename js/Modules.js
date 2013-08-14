var MODULES = {};
MODULES.COMMON = {};
MODULES.MAIN = {};

MODULES.COMMON.HttpRequest = (function()
{
	//private:
	var target = "";

	var o = {};
	//public:
	o.execute = function(type, target, message)
	{
		var request = new XMLHttpRequest();

		if(type == "POST" | "post")
		{
			request.onload = function() { console.log(this.responseText); };
			request.open(type, target, true);
			request.send(message);
			console.log(message);
		}

		else if(type == "GET" | "get")
		{
			request.onload = function() { console.log(this.responseText); };
			request.open(type, "/" + target + '?' + message, true);
			request.send();
			console.log(message);
		}
	};
	return o;
}());

MODULES.MAIN.GameGenerator = (function()
{
	//private:
	function newGame(players)
	{
		MODULES.COMMON.HttpRequest.execute("GET", "newgame", "player1=" + players["player1"] + "&player2=" + players["player2"]);
	};

	var players = { player1:"notSet", player2:"notSet" };

	var o = {};
	//public:
	o.addPlayer = function(player)
	{
		if(players["player1"] == "notSet")
			players["player1"] = player;

		else
		{
			players["player2"] = player;
			newGame(players);
		}
	};

	return o;
}());
