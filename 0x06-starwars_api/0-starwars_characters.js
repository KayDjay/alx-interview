#!/usr/bin/node
const request = require('request');
/**
 * Retrieves and prints the names of characters from a Star Wars movie.
 * @param {number} movieId - The ID of the Star Wars movie.
 */
getMovieCharacters(movieId);

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
    } else {
        const film = JSON.parse(body);
        const characters = film.characters;

        characters.forEach((characterUrl) => {
            request(characterUrl, (error, response, body) => {
                if (error) {
                    console.error('Error:', error);
                } else {
                    const character = JSON.parse(body);
                    console.log(character.name);
                }
            });
        });
    }
});