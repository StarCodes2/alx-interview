#!/usr/bin/node
const request = require('request');

// Function to get characters from a specified Star Wars movie
function getMovieCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.error(`Failed to retrieve data for movie ID ${movieId}:`, error.message);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Failed to retrieve data for movie ID ${movieId}. Status Code: ${response.statusCode}`);
      return;
    }

    const data = JSON.parse(body);
    const characters = data.characters;

    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Failed to retrieve character data:', error.message);
          return;
        }

        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  });
}

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: script.js <Movie ID>');
  process.exit(1);
}

getMovieCharacters(movieId);
