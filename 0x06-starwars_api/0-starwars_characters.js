#!/usr/bin/node

const request = require('request');
const API_URL = 'https://swapi.dev/api';

if (process.argv.length !== 3) {
    console.log('Usage: ./script.js <movie_id>');
    process.exit(1);
}

const movieId = process.argv[2];

request(`${API_URL}/films/${movieId}/`, (err, _, body) => {
    if (err) {
        console.error('Error:', err);
        process.exit(1);
    }

    const charactersURL = JSON.parse(body).characters;

    const getCharacterName = url => {
        return new Promise((resolve, reject) => {
            request(url, (err, _, body) => {
                if (err) {
                    reject(err);
                    return;
                }
                resolve(JSON.parse(body).name);
            });
        });
    };

    const characterNamePromises = charactersURL.map(getCharacterName);

    Promise.all(characterNamePromises)
        .then(names => {
            console.log(names.join('\n'));
        })
        .catch(err => {
            console.error('Error:', err);
            process.exit(1);
        });
});
