//define variables used throughout game
var colors = ["blue", "red", "yellow", "pink"];
var values = [0];
var pile = [];
var topCardInPile = '';
var numTurns = 0;
var colorToPlay = '';
var valToPlay = '';
var Players = [];

//prepares values and colors lists
for (var i = 1; i < 10; i++)
{
  values.push(i);
  values.push(i);
}
var special = ['draw 2', 'reverse', 'skip'];
for (i in special)
{
  values.push(special[i]);
  values.push(special[i]);
}

// defines a card object
function card(color, value){
  this.color = color;
  this.value = value;
}

//turns card object into string form
function cardToString(card){
  var toReturn = card.color + '_' + card.value;
  return toReturn;
}

function printPile(pileOfCards){
  console.log('printing pile');
  for (x in pileOfCards){
    console.log(pileOfCards[x]);
  }
}

//creates a deck of cards
function create_deck(){
  var deck = [];
  for (x in colors){
    for (y in values){
      var newcard = new card(colors[x], values[y]);
      deck.push(newcard);
    }
  }
  var wild = new card('wild', '');
  var superwild = new card('wild', 'draw 4');
  for (var i = 0; i <4; i++){
    deck.push(wild);
    deck.push(superwild);
  }
  return deck;
}

function shuffle(o){
    for(var j, x, i = o.length; i; j = Math.floor(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
    return o;
}

//defines player object (name = string, human = boolean)
function player(name, human){
  this.name = name;
  this.human = human;
  this.goesFirst = false;
  this.cards = [];
}

//returns array of indices at which there is a valid card to be played
//returns all wild and cards with the same color/value
function checkValid(person){
  var valid = [];
  for (x in person.cards){
    if (person.cards[x].color == 'wild' || person.cards[x].color == colorToPlay
      || person.cards[x].value == valToPlay){
          valid.push(x);
      }
  }
  return valid;
}


//plays card, adds to pile, subtracts from hand
function playCard(person, num){
  var toPlay = person.cards.splice(num, 1)[0];
  pile.push(toPlay);
}

function getTopCard(){
  return pile[pile.length - 1];
}

//prepares game, doesn't return anything
//modifies deck + player's hands
function prepareGame(){

  //creates and shuffles deck
  deck = shuffle(create_deck());
  //deals 7 cards each to players
  //console.log('players: ' + Players[0])
  for (x in Players){
    //console.log('name' + Players[x].name);
    //console.log('cards:' + Players[x].cards);
    for (var i = 0; i <7; i++){
      Players[x].cards.push(deck.pop());
    }
  }
  //adds top card to pile
  pile.push(deck.pop());
  //defines top card of pile
  topCardInPile = getTopCard();
  colorToPlay = topCardInPile.color;
  valToPlay = topCardInPile.value;
  return topCardInPile;
}

function fillDeck(){
  var arr = pile.splice(0, 9);
  for (x in arr){
    deck.push(arr[x])
  }
  shuffle(deck);
}


function add_card(card){
  console.log('showing card');
  $('#hand').append('<div id =' + cardToString(card) +
    ' class= "card'+ card.color + '" ><div class = "cardOval"><h3 class= "cardText">' +
      card.value + '</h3></div></div>');
  $('.card' + card.color).delay(200).fadeIn();
}

//prints the cards that a player has
function showHand(person){
  for (x in person.cards){
    add_card(person.cards[x]);
  }
}

//handles turn
//if human, uses console
function turnOfPlayer(num){
  //updates total number of turns
  numTurns++;
  var player = Players[num];
  topCardInPile = getTopCard();
  var valid = checkValid(player, topCardInPile);
  //if can't play cards, draws more until can
  while (valid.length ==0){
    player.cards.push(deck.pop());
    valid = checkValid(player, topCardInPile);
  }
  //handles human turn
  if (player.human == true){
    showHand(player);
    playCard(player, input);
    console.log('you played ' + cardToString(pile[pile.length - 1]));
  }
  //handles computer turn
  else{
    //plays randomly chosen card out of valid list
    cardnum = parseInt(valid[Math.floor((Math.random() * valid.length))]);
    playCard(player, cardnum);
    console.log(player.name + ' played ' + cardToString(pile[pile.length - 1]));
  }
  //if player is out of cards, game is over
  if (player.cards.length == 0){
    gameOver = true;
    console.log(player.name + ' is the winner!');
    return;
  }
  //updates information
  topCardInPile = getTopCard();
  //updates color and value to play
  colorToPlay = topCardInPile.color;
  valToPlay = topCardInPile.value;
  //returns card just played
  return topCardInPile;
  //SHOULD SHOW WHICH CARD played
}

//handles the special cards in deck
//takes index of player who just played as a parameter
//returns index of next player
//updates colorToPlay, if necessary
function handleCardAction(num){
  topCardInPile = getTopCard();
  //handles skip
  if (topCardInPile.value == 'skip'){
    numTurns++;
  }
  //handles reverse
  if (topCardInPile.value == 'reverse'){
    Players.reverse();
  }
  //handles wild cards
  nextPlayer = Players[numTurns % Players.length];
  if (topCardInPile.color == 'wild'){
      if (topCardInPile.value == 'draw 4'){
        for (var i =0; i<4; i++){
          nextPlayer.cards.push(deck.pop());
        }
      }
      if(Players[(numTurns-1)%Players.length].human == false){
        colorToPlay = colors[Math.floor(Math.random() * 4)];
        console.log('new color is: ' + colorToPlay);
      }
      else{
        var col = prompt('choose which color (0) blue 1) red 2) yellow 3) pink)');
        colorToPlay = colors[parseInt(col)];
        console.log('new color is: ' + colorToPlay);
      }
  }
  //handles +2
  else if(topCardInPile.value == 'draw 2'){
    for (var i =0; i<2; i++){
      nextPlayer.cards.push(deck.pop());
    }
  }
  return numTurns % Players.length;
}

function playGame(players){
  //defines boolean which tells whether the game is over or not
  var gameOver = false;
  Players = players;
  topCardInPile = prepareGame();
  console.log('top card is: ' + cardToString(topCardInPile));
  numTurns = Math.floor(Math.random()*Players.length);
  var num = numTurns;
  console.log(num);
  while (gameOver == false){
    var result = turnOfPlayer(num);
    if (null != result){
      topCard = result
      console.log(cardToString(topCard));
      num = handleCardAction(num);
      if (pile.length > 10){
        fillDeck();
      }
    }
    else{
      break;
    }
  }

}

var player1 = new player('CHUMP THE CHIPMUNK', false);
var player2 = new player('Chumpina the first lady', false);
var player3 = new player('little chumpy the baby', false);

var card1 = new card('yellow', '+2');
var card2 = new card('yellow', '+3');
var card3 = new card('yellow', '+4');
var card4 = new card('yellow', '+5');
var card5 = new card('yellow', '+6');


player1.cards = [card1, card2, card3];
$( document ).ready(function() {
  console.log('showing player1s hand')
  showHand(player1)

});




//end of game
