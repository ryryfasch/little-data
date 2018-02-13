var Twitter = require('twitter');
const cfg = require("./cred.json");
var fs = require('fs');

var client = new Twitter({
  consumer_key: cfg.twitter.key,
  consumer_secret: cfg.twitter.key_secret,
  access_token_key: cfg.twitter.token,
  access_token_secret: cfg.twitter.token_secret
});

/**
 * Stream statuses filtered by keyword
 * number of tweets per second depends on topic popularity
 **/
client.stream('statuses/filter', {track: 'fortnite'},  function(stream) {
  stream.on('data', function(tweet) {
    console.log(tweet.text);
  });

  stream.on('error', function(error) {
    console.log(error);
  });
});
