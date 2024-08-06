#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(movieUrl, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error(`Error fetching film data: ${error || response.statusCode}`);
    return;
  }

  const film = JSON.parse(body);
  const characterUrls = film.characters;

  // Create a list of promises to fetch character data
  const characterPromises = characterUrls.map((characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error || response.statusCode !== 200) {
          reject(new Error(`Error fetching character data from ${characterUrl}: ${error || response.statusCode}`));
        } else {
          const character = JSON.parse(body);
          resolve(character.name);
        }
      });
    });
  });

  // Once all promises resolve, print the character names
  Promise.all(characterPromises)
    .then((characterNames) => {
      characterNames.forEach((name) => {
        console.log(name);
      });
    })
    .catch((error) => {
      console.error(error.message);
    });
});
