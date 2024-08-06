#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    process.exit(1);
  }

  const data = JSON.parse(body);
  const characterUrls = data.characters;

  characterUrls.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
