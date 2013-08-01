#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

print """\
Content-Type: text/html\n
<!DOCTYPE html>

<html>
<head>
<script>

var game;

function Game(player1, player2)
{
    this.player1 = player1;
    this.player2 = player2;
    this.guid = new Date().getTime();
    this.date = new Date();
    this.rallies = [];
    this.victor = undefined;

    this.player1Scores = function()
    {
        this.rallies[this.rallies.length] = new Rally(this.getCurrentServer(), player1, this.rallies.length +1);
    };
    this.player2Scores = function()
    {
        this.rallies[this.rallies.length] = new Rally(this.getCurrentServer(), player2, this.rallies.length +1);
    };

    // player1 begins by serving on endA
    this.getPlayer1End = function()
    {
        if (this.rallies.length >= 5)
            return "endB";
        else
            return "endA";
    };
    
    this.getPlayer2End = function()
    {
        if (this.rallies.length >= 5)
            return "endA";
        else
            return "endB";
    }

    this.getCurrentServer = function()
    {
        if (this.rallies.length <= 1)
            return this.player1;

        else if (this.rallies.length <= 3)
            return this.player2;

        else if ((this.rallies.length % 2.0) == 0.0)
            return this.rallies[this.rallies.length - 3]['server'];

        else
            return this.rallies[this.rallies.length - 1]['server'];
    }

    this.getPlayer1Score = function()
    {
        var score = 0;
        for (var i=0; i<= this.rallies.length-1; i++)
        {
            if (this.rallies[i]['victor'] == player1)
                score ++
        }
        return score;
    }

    this.getPlayer2Score = function()
    {
        var score = 0;
        for (var i=0; i<= this.rallies.length-1; i++)
        {
            if (this.rallies[i]['victor'] == player2)
                score ++
        }
        return score;
    }

}

function Rally(server, victor, number)
{
    this.server = server;
    this.victor = victor;
    this.rallyNumber = number;
}

function updateGameServer(game)
{
    var request = new XMLHttpRequest();
    var url = 'pongRecieve.py?game=' + JSON.stringify(game);
    console.log(url);
    request.open("GET", url);
    request.send();
}

function newGame()
{
    game = new Game(playerAInput.value,playerBInput.value);
//    console.log(JSON.stringify(game));
    updateGameServer(game);
    updateScoreCard(game);
}

function player1Scores()
{
    game.player1Scores();
//    console.log(JSON.stringify(game));
    updateGameServer(game);
    updateScoreCard(game);

}
function player2Scores()
{
    game.player2Scores();
    console.log(JSON.stringify(game));
    updateGameServer(game);
    updateScoreCard(game);

}
function updateScoreCard(game)
{
    var scoreCard = document.getElementById("scoreCard");
    
    scoreCard.innerHTML = "player1:  " + game.player1 + ": " + game.getPlayer1Score() + " side: " + game.getPlayer1End() +  "<br/>";
    scoreCard.innerHTML += "player2: " + game.player2 + ": " + game.getPlayer2Score() + " side: " + game.getPlayer2End() +  "<br/>";
    scoreCard.innerHTML += "server: " + game.getCurrentServer() + "<br/>";

    //document.getElementById("scoreCard").innerHTML = "player1: " + game.player1 + ": " + game.getPlayer1Score();

}

</script>
</head>
<body>

<input id="playerAInput" value="dude"/>
<input id="playerBInput" value="bro"/>
<button type="button" onclick="newGame()">newGame()</button>
<button type="button" onclick="player1Scores()">player1Scores()</button>
<button type="button" onclick="player2Scores()">player2Scores()</button><br/>

<span id="scoreCard"></span>


</body>
</html> """

