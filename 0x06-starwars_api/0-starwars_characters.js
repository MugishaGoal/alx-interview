#!/usr/bin/node

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  // Setting rejectUnauthorized to false to ignore SSL certificate verification
  // This is necessary due to the expired SSL certificate error
  request.defaults({rejectUnauthorized: false});

  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.error(err);
      return;
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
            return;
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.error(allErr));
  });
} else {
  console.error("Usage: ./0-starwars_characters.js <movie_id>");
}
