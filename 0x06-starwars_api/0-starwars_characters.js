#!/usr/bin/node

const axios = require('axios');

/**
 * Fetches and logs the names of characters from a Star Wars movie.
 * @param {number} movieId - The ID of the Star Wars movie.
 * @returns {Promise<void>} - A promise that resolves once all character names are logged.
 */
async function getMovieCharacters(movieId) {
    try {
        const movieResponse = await axios.get(`https://swapi.dev/api/films/${movieId}/`);
        const characterUrls = movieResponse.data.characters;
        
        for (const url of characterUrls) {
            try {
                const characterResponse = await axios.get(url);
                console.log(characterResponse.data.name);
            } catch (error) {
                console.error(`Failed to fetch character data: ${error}`);
            }
        }
    } catch (error) {
        console.error(`Failed to fetch movie data for movie ID ${movieId}: ${error}`);
    }
}

const movieId = process.argv[2];
if (!movieId) {
    console.error('Usage: node script.js <movie_id>');
    process.exit(1);
}

getMovieCharacters(movieId);