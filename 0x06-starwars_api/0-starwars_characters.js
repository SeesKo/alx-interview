#!/usr/bin/node

const request = require('request');

const BASE_URL = 'https://swapi.dev/api/films/';

// Function to fetch data from API
function fetchData(url, callback) {
  request(url, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error fetching data:', error);
      callback(null);
      return;
    }
    if (response.statusCode !== 200) {
      console.error(`HTTP error! status: ${response.statusCode}`);
      callback(null);
      return;
    }
    callback(body);
  });
}
