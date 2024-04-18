#!/usr/bin/node

const axios = require('axios');

async function getMovieCharacters(movieId) {
    try {
        const response = await axios.get(`https://swapi.dev/api/films/${movieId}/`);
        const characters = response.data.characters;

        for (const characterUrl of characters) {
            const characterResponse = await axios.get(characterUrl);
            console.log(characterResponse.data.name);
        }
    } catch (error) {
        console.error("Error:", error.message);
    }
}

if (process.argv.length !== 3) {
    console.log("Usage: node script.js <movie_id>");
    process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId);
