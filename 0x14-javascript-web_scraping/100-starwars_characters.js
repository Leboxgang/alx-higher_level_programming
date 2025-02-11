#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  try {
    const data = JSON.parse(body);
    const characters = data.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, function (err, response, body) {
        if (!err) {
          try {
            console.log(JSON.parse(body).name);
          } catch (parseError) {
            console.error('Error parsing character data:', parseError);
          }
        } else {
          console.error('Error fetching character:', err);
        }
      });
    });
  } catch (parseError) {
    console.error('Error parsing movie data:', parseError);
  }
});
