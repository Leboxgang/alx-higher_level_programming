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
    console.log(data.title);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
